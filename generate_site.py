#!/usr/bin/env python3
"""
Script para generar el portafolio web estático desde Python
Ejecutar: python generate_site.py
"""

import json
import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
import requests

# Configuración
BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
OUTPUT_DIR = BASE_DIR / "dist"

# Crear directorio de salida
OUTPUT_DIR.mkdir(exist_ok=True)
(OUTPUT_DIR / "static").mkdir(exist_ok=True)
(OUTPUT_DIR / "static" / "css").mkdir(exist_ok=True)
(OUTPUT_DIR / "static" / "js").mkdir(exist_ok=True)

# Configurar Jinja2
env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    autoescape=select_autoescape(['html', 'xml'])
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
    """Obtiene los proyectos del usuario de GitHub"""
    try:
        url = f"https://api.github.com/users/{usuario}/repos"
        params = {"sort": "updated", "per_page": 6}
        response = requests.get(url, params=params, timeout=5)

        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"[!] Error al traer proyectos de GitHub: {e}")

    return []


def copiar_archivos_estaticos():
    """Copia los archivos estáticos (CSS, JS, imagenes)"""
    if STATIC_DIR.exists():
        import shutil
        for item in STATIC_DIR.iterdir():
            dest = OUTPUT_DIR / "static" / item.name
            if item.is_file():
                shutil.copy2(item, dest)
            elif item.is_dir():
                if dest.exists():
                    shutil.rmtree(dest)
                shutil.copytree(item, dest)


def generar_sitio():
    """Genera el sitio web estático"""
    print("[*] Generando portafolio...")

    # Cargar datos
    datos = cargar_datos()
    github_user = datos.get("github_user", "AsKrueger")

    # Obtener proyectos de GitHub
    print("[+] Cargando proyectos de GitHub...")
    proyectos = obtener_proyectos_github(github_user)
    datos["proyectos"] = proyectos
    datos["projects"] = proyectos

    # Copiar archivos estáticos
    print("[+] Copiando archivos estáticos...")
    copiar_archivos_estaticos()

    # Generar páginas HTML
    pages = [
        "index.html",
        "sobre.html",
        "proyectos.html",
        "curriculum.html",
    ]

    for page in pages:
        print(f"[+] Generando {page}...")
        template = env.get_template(page)
        html = template.render(**datos)

        with open(OUTPUT_DIR / page, "w", encoding="utf-8") as f:
            f.write(html)

    # Generar sobre.html
    print("[+] Generando sobre.html...")
    template = env.get_template("sobre.html")
    html = template.render(**datos)

    with open(OUTPUT_DIR / "sobre.html", "w", encoding="utf-8") as f:
        f.write(html)

    # Generar proyectos.html
    print("[+] Generando proyectos.html...")
    template = env.get_template("proyectos.html")
    html = template.render(**datos)

    with open(OUTPUT_DIR / "proyectos.html", "w", encoding="utf-8") as f:
        f.write(html)

    # Generar curriculum.html
    print("[+] Generando curriculum.html...")
    template = env.get_template("curriculum.html")
    html = template.render(**datos)

    with open(OUTPUT_DIR / "curriculum.html", "w", encoding="utf-8") as f:
        f.write(html)

    # Generar CNAME para dominio personalizado (opcional)
    cname_file = BASE_DIR / "CNAME"
    if cname_file.exists():
        import shutil
        shutil.copy2(cname_file, OUTPUT_DIR / "CNAME")

    print("[OK] Portafolio generado exitosamente!")
    print(f"[*] Archivos en: {OUTPUT_DIR}")
    print(f"   - index.html")
    print(f"   - sobre.html")
    print(f"   - proyectos.html")
    print(f"   - static/css/")
    print(f"   - static/js/")
    print("\n[INFO] Proximos pasos:")
    print("   1. Verifica los archivos en 'dist/'")
    print("   2. Sube 'dist/' a GitHub Pages en la rama 'gh-pages'")
    print(f"   3. Tu portafolio estara en: https://{github_user}.github.io/portfolio/")


if __name__ == "__main__":
    generar_sitio()
