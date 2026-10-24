#!/usr/bin/env python3
"""Genera el portfolio estático en dist/ a partir de data.json, ui.json y templates/.

Uso:
    python build.py                # genera dist/
    python build.py --pdf          # además imprime el CV en PDF con Chrome/Chromium headless
    python build.py --serve        # genera y sirve en http://localhost:8000
"""

import argparse
import functools
import http.server
import json
import os
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
from markupsafe import Markup
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
OUTPUT_DIR = BASE_DIR / "dist"

# Español en la raíz (URLs ya publicadas), inglés bajo /en/.
LANGS = {
    "es": {"prefix": "", "projects": "proyectos", "locale": "es_ES"},
    "en": {"prefix": "en/", "projects": "projects", "locale": "en_GB"},
}
DEFAULT_LANG = "es"

# URLs publicadas en versiones anteriores del sitio -> destino actual (relativo a la raíz).
LEGACY_REDIRECTS = {
    "sobre-mi/index.html": "#about",
    "experiencia/index.html": "#experience",
    "formacion/index.html": "#education",
    "contacto/index.html": "#contact",
    "proyectos/index.html": "#projects",
    "curriculum.html": "cv/",
}

REQUIRED_PROJECT_KEYS = ("slug", "name", "tagline", "summary", "status", "repository")

CHROME_CANDIDATES = (
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
)


def localize(value, lang):
    """Sustituye recursivamente cada {"es": ..., "en": ...} por el valor del idioma."""
    if isinstance(value, dict):
        if value.keys() == LANGS.keys():
            return localize(value[lang], lang)
        return {key: localize(item, lang) for key, item in value.items()}
    if isinstance(value, list):
        return [localize(item, lang) for item in value]
    return value


def load_json(name):
    with open(BASE_DIR / name, encoding="utf-8") as f:
        return json.load(f)


def validate(data):
    slugs = set()
    for project in data["projects"]:
        missing = [key for key in REQUIRED_PROJECT_KEYS if not project.get(key)]
        if missing:
            sys.exit(f"[x] Proyecto '{project.get('slug', '?')}' sin campos: {', '.join(missing)}")
        if project["slug"] in slugs:
            sys.exit(f"[x] Slug duplicado: {project['slug']}")
        slugs.add(project["slug"])
        snippet = project.get("snippet")
        if snippet and not (BASE_DIR / snippet["file"]).exists():
            sys.exit(f"[x] No existe el fragmento {snippet['file']}")
        for shot in project.get("gallery", []):
            if not (STATIC_DIR / shot["src"]).exists():
                sys.exit(f"[x] No existe la captura {shot['src']}")


def prepare_projects(projects):
    """Resalta los fragmentos de código con Pygments y enlaza el diagrama de cada proyecto."""
    formatter = HtmlFormatter(nowrap=True)
    for project in projects:
        diagram = Path("diagrams") / f"{project['slug']}.svg"
        project["diagram"] = diagram.as_posix() if (TEMPLATES_DIR / diagram).exists() else None
        project.setdefault("gallery", [])
        snippet = project.setdefault("snippet", None)
        if snippet:
            code = (BASE_DIR / snippet["file"]).read_text(encoding="utf-8")
            snippet["html"] = Markup(highlight(code, get_lexer_by_name(snippet["lang"]), formatter))


def page_url(public_url, target):
    """URL pública de una página; '' si no hay public_url configurada."""
    if not public_url:
        return ""
    path = target[: -len("index.html")] if target.endswith("index.html") else target
    return public_url.rstrip("/") + "/" + path


def target_for(key, lang):
    """Fichero de salida de una página lógica ('home', 'cv', 'project:<slug>') en un idioma."""
    cfg = LANGS[lang]
    if key == "home":
        return f"{cfg['prefix']}index.html"
    if key == "cv":
        return f"{cfg['prefix']}cv/index.html"
    if key.startswith("project:"):
        return f"{cfg['prefix']}{cfg['projects']}/{key.split(':', 1)[1]}/index.html"
    raise ValueError(key)


def find_chrome():
    for candidate in [os.environ.get("CHROME", "")] + list(CHROME_CANDIDATES):
        if candidate and (shutil.which(candidate) or Path(candidate).exists()):
            return shutil.which(candidate) or candidate
    return None


class Site:
    def __init__(self, data, ui, with_pdf):
        self.data = data
        self.ui = ui
        self.with_pdf = with_pdf
        self.public_url = data["site"].get("public_url", "").strip()
        self.pages = []
        self.env = Environment(
            loader=FileSystemLoader(TEMPLATES_DIR),
            autoescape=select_autoescape(["html", "xml", "svg"]),
            undefined=StrictUndefined,
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def render(self, template, target, lang, key=None, indexable=True, root=None, **context):
        if root is None:
            root = "../" * target.count("/")
        alternates = {}
        if key:
            alternates = {
                code: {
                    "href": root + target_for(key, code).removesuffix("index.html"),
                    "url": page_url(self.public_url, target_for(key, code)),
                }
                for code in LANGS
            }
        html = self.env.get_template(template).render(
            **localize(self.data, lang),
            **context,
            t=localize(self.ui, lang),
            lang=lang,
            locale=LANGS[lang]["locale"],
            root=root,
            base=root + LANGS[lang]["prefix"],
            projects_dir=LANGS[lang]["projects"],
            alternates=alternates,
            page_url=page_url(self.public_url, target),
            public_url=self.public_url,
            has_pdf=self.with_pdf,
            build_year=date.today().year,
        )
        out = OUTPUT_DIR / target
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        if indexable:
            self.pages.append(target)

    def build(self):
        if OUTPUT_DIR.exists():
            shutil.rmtree(OUTPUT_DIR)
        shutil.copytree(STATIC_DIR, OUTPUT_DIR / "static")

        projects = self.data["projects"]
        for lang in LANGS:
            self.render("index.html", target_for("home", lang), lang, key="home")
            self.render("cv.html", target_for("cv", lang), lang, key="cv")
            for i, project in enumerate(projects):
                key = f"project:{project['slug']}"
                self.render(
                    "project.html",
                    target_for(key, lang),
                    lang,
                    key=key,
                    project=localize(project, lang),
                    prev_project=projects[i - 1] if i > 0 else None,
                    next_project=projects[i + 1] if i + 1 < len(projects) else None,
                )

        # GitHub Pages sirve 404.html en cualquier ruta: necesita enlaces absolutos.
        self.render("404.html", "404.html", DEFAULT_LANG, indexable=False, root=self.public_url or "/")
        for target, destination in LEGACY_REDIRECTS.items():
            self.render("redirect.html", target, DEFAULT_LANG, indexable=False, destination=destination)

        self.write_seo_files()
        (OUTPUT_DIR / ".nojekyll").touch()

    def write_seo_files(self):
        robots = ["User-agent: *", "Allow: /"]
        if self.public_url:
            robots.append(f"Sitemap: {page_url(self.public_url, 'sitemap.xml')}")
            urls = "".join(
                f"  <url><loc>{page_url(self.public_url, p)}</loc></url>\n" for p in self.pages
            )
            (OUTPUT_DIR / "sitemap.xml").write_text(
                '<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                f"{urls}</urlset>\n",
                encoding="utf-8",
            )
        (OUTPUT_DIR / "robots.txt").write_text("\n".join(robots) + "\n", encoding="utf-8")

    def print_pdfs(self, chrome):
        for lang in LANGS:
            page = OUTPUT_DIR / target_for("cv", lang)
            pdf = page.parent / self.data["site"]["cv_pdf"]
            subprocess.run(
                [
                    chrome,
                    "--headless=new",
                    "--disable-gpu",
                    "--no-sandbox",
                    "--no-pdf-header-footer",
                    "--virtual-time-budget=3000",
                    f"--print-to-pdf={pdf}",
                    page.resolve().as_uri(),
                ],
                check=True,
                capture_output=True,
            )
            if not pdf.exists():
                sys.exit(f"[x] Chrome no generó {pdf}")
            print(f"[OK] PDF: {pdf.relative_to(BASE_DIR)}")


def serve(port):
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=OUTPUT_DIR)
    with http.server.ThreadingHTTPServer(("127.0.0.1", port), handler) as httpd:
        print(f"[*] Sirviendo dist/ en http://localhost:{port} (Ctrl+C para parar)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--pdf", action="store_true", help="genera el CV en PDF (requiere Chrome)")
    parser.add_argument("--serve", action="store_true", help="sirve dist/ tras generarlo")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    chrome = None
    if args.pdf:
        chrome = find_chrome()
        if not chrome:
            sys.exit("[x] --pdf necesita Chrome/Chromium (o la variable CHROME con su ruta)")

    data = load_json("data.json")
    validate(data)
    prepare_projects(data["projects"])

    site = Site(data, load_json("ui.json"), with_pdf=bool(chrome))
    site.build()
    print(f"[OK] {len(site.pages)} paginas indexables generadas en {OUTPUT_DIR}")
    if chrome:
        site.print_pdfs(chrome)

    if args.serve:
        serve(args.port)


if __name__ == "__main__":
    main()
