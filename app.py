from flask import Flask, render_template
import json
import requests
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data.json"


def cargar_datos():
    """Carga los datos del portafolio desde data.json"""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"github_user": "AsKrueger", "linkedin_url": "https://www.linkedin.com/in/alonso-amador"}


def get_github_projects(usuario):
    """Obtiene los proyectos del usuario de GitHub"""
    try:
        response = requests.get(
            f"https://api.github.com/users/{usuario}/repos",
            params={"sort": "updated", "per_page": 6},
            timeout=5,
            headers={"User-Agent": "PortfolioApp"},
        )
        if response.status_code == 200:
            return response.json()
    except Exception:
        pass
    return []


@app.route('/')
def index():
    datos = cargar_datos()
    return render_template('index.html', **datos)


@app.route('/sobre')
def sobre():
    datos = cargar_datos()
    return render_template('sobre.html', **datos)


@app.route('/proyectos')
def proyectos():
    datos = cargar_datos()
    projects = get_github_projects(datos.get("github_user", "AsKrueger"))
    return render_template('proyectos.html', projects=projects, **datos)


@app.route('/curriculum')
def curriculum():
    datos = cargar_datos()
    return render_template('curriculum.html', **datos)


if __name__ == '__main__':
    app.run(debug=True)
