#!/usr/bin/env python3
"""
Script para generar el portafolio web estático desde Python.
Mantiene la generación estática del sitio pero añade una estructura
más clara de rutas y templates reutilizables para la arquitectura de navegación.
"""

import json
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
import requests

BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
OUTPUT_DIR = BASE_DIR / "dist"

OUTPUT_DIR.mkdir(exist_ok=True)
(OUTPUT_DIR / "static").mkdir(exist_ok=True)
(OUTPUT_DIR / "static" / "css").mkdir(exist_ok=True)
(OUTPUT_DIR / "static" / "js").mkdir(exist_ok=True)

env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    autoescape=select_autoescape(["html", "xml"]),
)

def url_for(endpoint, **values):
    if endpoint == "static":
        return f"static/{values.get('filename', '')}"
    raise ValueError("Only 'static' endpoint is supported in static generation")

env.globals["url_for"] = url_for


def cargar_datos():
    """Carga los datos del portafolio desde data.json"""
    with open(BASE_DIR / "data.json", "r", encoding="utf-8") as f:
        return json.load(f)


def obtener_proyectos_github(usuario):
    """Obtiene una vista rápida de repositorios desde la API de GitHub."""
    try:
        url = f"https://api.github.com/users/{usuario}/repos"
        params = {"sort": "updated", "per_page": 6}
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"[!] Error al traer proyectos de GitHub: {e}")
    return []


def construir_project_cards(proyectos_api, proyectos_curados):
    """Normalizes API projects and keeps generation useful when the API is unavailable."""
    if proyectos_api:
        return proyectos_api
    return [
        {
            "name": project.get("name"),
            "description": project.get("summary"),
            "html_url": project.get("repository"),
            "language": (project.get("technologies") or [None])[0],
        }
        for project in proyectos_curados
    ]


def copiar_archivos_estaticos():
    """Copia los archivos estáticos al directorio de salida."""
    if STATIC_DIR.exists():
        for item in STATIC_DIR.iterdir():
            dest = OUTPUT_DIR / "static" / item.name
            if item.is_file():
                shutil.copy2(item, dest)
            elif item.is_dir():
                if dest.exists():
                    shutil.rmtree(dest)
                shutil.copytree(item, dest)


def relative_root(depth):
    return "../" * max(depth, 0)


def public_page_url(public_url, target_file):
    """Builds a public URL only when the deployment URL is explicitly configured."""
    if not public_url:
        return ""
    normalized = target_file.replace("\\", "/")
    if normalized == "index.html":
        suffix = ""
    elif normalized.endswith("/index.html"):
        suffix = normalized[:-len("index.html")]
    else:
        suffix = normalized
    return f"{public_url.rstrip('/')}/{suffix.lstrip('/')}"


def render_page(template_name, target_file, depth=0, **context):
    template = env.get_template(template_name)
    page_context = dict(context)
    page_context["site_root"] = relative_root(depth)
    page_context["page_url"] = public_page_url(
        page_context.get("public_url", ""), target_file
    )
    target_path = OUTPUT_DIR / target_file
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(template.render(**page_context), encoding="utf-8")


def generar_archivos_seo(public_url, projects):
    """Generates crawl controls and a sitemap when the public URL is known."""
    robots_lines = ["User-agent: *", "Allow: /"]
    sitemap_path = OUTPUT_DIR / "sitemap.xml"

    if public_url:
        public_url = public_url.rstrip("/")
        robots_lines.append(f"Sitemap: {public_url}/sitemap.xml")
        public_pages = [
            "index.html",
            "sobre-mi/index.html",
            "proyectos/index.html",
            "experiencia/index.html",
            "formacion/index.html",
            "contacto/index.html",
            "curriculum.html",
        ]
        project_pages = [
            f"proyectos/{project['slug']}/index.html"
            for project in projects
            if project.get("slug")
        ]
        urls = [public_page_url(public_url, page) for page in public_pages + project_pages]
        sitemap = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        sitemap += "".join(f"  <url><loc>{url}</loc></url>\n" for url in urls)
        sitemap += "</urlset>\n"
        sitemap_path.write_text(sitemap, encoding="utf-8")
    elif sitemap_path.exists():
        sitemap_path.unlink()

    (OUTPUT_DIR / "robots.txt").write_text(
        "\n".join(robots_lines) + "\n", encoding="utf-8"
    )


def generar_sitio():
    """Genera el sitio web estático con estructura de rutas clara."""
    print("[*] Generando portafolio...")
    datos = cargar_datos()
    github_user = datos.get("github_user", "AsKrueger")

    print("[+] Cargando proyectos de GitHub...")
    proyectos_api = obtener_proyectos_github(github_user)
    datos["project_cards"] = construir_project_cards(
        proyectos_api, datos.get("projects", [])
    )
    datos["featured_projects"] = [
        project for project in datos.get("projects", []) if project.get("featured")
    ]

    print("[+] Copiando archivos estáticos...")
    copiar_archivos_estaticos()

    print("[+] Generando páginas principales...")
    render_page("index.html", "index.html", depth=0, **datos)
    render_page("sobre.html", "sobre-mi/index.html", depth=1, **datos)
    render_page("experiencia.html", "experiencia/index.html", depth=1, **datos)
    render_page("formacion.html", "formacion/index.html", depth=1, **datos)
    render_page("contacto.html", "contacto/index.html", depth=1, **datos)
    render_page("proyectos.html", "proyectos/index.html", depth=1, **datos)
    render_page("curriculum.html", "curriculum.html", depth=0, **datos)

    for legacy_page in (OUTPUT_DIR / "sobre.html", OUTPUT_DIR / "proyectos.html"):
        if legacy_page.exists():
            legacy_page.unlink()

    print("[+] Generando páginas de proyecto...")
    for project in datos.get("projects", []):
        slug = project.get("slug")
        if not slug:
            continue
        render_page(
            "proyecto.html",
            f"proyectos/{slug}/index.html",
            depth=2,
            project=project,
            **datos,
        )

    generar_archivos_seo(datos.get("public_url", "").strip(), datos.get("projects", []))

    cname_file = BASE_DIR / "CNAME"
    if cname_file.exists():
        shutil.copy2(cname_file, OUTPUT_DIR / "CNAME")

    print("[OK] Portafolio generado exitosamente!")
    print(f"[*] Archivos en: {OUTPUT_DIR}")
    print("   - index.html")
    print("   - sobre-mi/index.html")
    print("   - proyectos/index.html")
    print("   - experiencia/index.html")
    print("   - formacion/index.html")
    print("   - contacto/index.html")
    print("\n[INFO] Proximos pasos:")
    print("   1. Verifica el contenido en 'dist/'")
    print("   2. Comprueba los enlaces internos y las rutas")
    print(f"   3. Publica 'dist/' en GitHub Pages si procede")


if __name__ == "__main__":
    generar_sitio()
