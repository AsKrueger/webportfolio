# AsKrueger Portfolio 🚀

Portafolio web profesional desarrollado con **Python** y generado de forma estática para GitHub Pages.

## 🎯 Características

- **Desarrollado en Python** - Script que genera HTML estático
- **Dinámico** - Trae proyectos automáticamente de GitHub API
- **Responsive** - Diseño adaptable a cualquier dispositivo
- **Fácil de personalizar** - Edita `data.json` y ejecuta el generador
- **GitHub Pages** - Despliegue gratuito y automático
- **SEO técnico** - Metadatos por página y `robots.txt` generado

## 📋 Secciones

- **Inicio**: Hero section con descripción y CTA
- **Sobre mí**: Información personal, habilidades y educación
- **Proyectos**: Galería de proyectos traídos de GitHub API
- **CV**: Experiencia y educación
- **GitHub**: Botón directo al perfil

## 🚀 Cómo Funciona

1. **Desarrollo**: Edita `data.json` con tu información
2. **Generación**: Ejecuta `python generate_site.py`
3. **Salida**: Los archivos se generan en la carpeta `dist/`
4. **Despliegue**: Sube `dist/` a GitHub Pages

El generador crea `robots.txt` permitiendo el rastreo. Si se confirma la URL pública
del despliegue, la configuración actual utiliza `"public_url": "https://askrueger.github.io/webportfolio/"` en `data.json`.
Con esa URL se generan las URLs canónicas, `og:url` y `sitemap.xml`.

## 💻 Instalación Local

### 1. Clona el repositorio
```bash
git clone https://github.com/AsKrueger/webportfolio.git
cd webportfolio
```

### 2. Instala dependencias
```bash
pip install -r requirements.txt
```

### 3. Personaliza tu información
Edita `data.json`:
```json
{
  "nombre": "Tu Nombre",
  "titulo": "Tu Título",
  "github_user": "tu_usuario_github",
  ...
}
```

### 4. Genera el sitio
```bash
python generate_site.py
```

### 5. Verifica localmente (opcional)
```bash
# Abre dist/index.html en tu navegador
# O usa un servidor local:
cd dist
python -m http.server 8000
```

## 📤 Desplegar en GitHub Pages

### Opción 1: Usando rama `gh-pages` (Recomendado)

```bash
# Instala ghp-import
pip install ghp-import

# Publica en gh-pages
ghp-import -p dist/
```

Tu portafolio está publicado en: `https://askrueger.github.io/webportfolio/`

### Opción 2: Configuración manual en GitHub

1. Ve a tu repositorio en GitHub
2. Abre **Settings** → **Pages**
3. En "Source", selecciona rama `gh-pages`
4. En "Directory", selecciona `/` (root)
5. Guarda

### Opción 3: Rama `main` + carpeta `docs`

1. Copia contenido de `dist/` a una carpeta `docs/`
2. Sube a GitHub
3. En Settings → Pages, elige `main` y `/docs/`

## 📝 Personalización

### Editar información
```bash
# data.json - Tu información personal
# templates/index.html - Estructura HTML
# static/css/style.css - Estilos
# static/js/main.js - Scripts
```

### Cambiar colores
Edita `static/css/style.css`:
```css
--color-primary: #0066cc; /* Cambia aquí */
```

### Agregar más proyectos
Los proyectos se traen **automáticamente** de tu GitHub API. Solo asegúrate de tener los repositorios públicos.

## 📦 Estructura del Proyecto

```
webportfolio/
├── generate_site.py          # Script principal
├── data.json                 # Tus datos personales
├── requirements.txt          # Dependencias Python
├── templates/
│   └── index.html           # Template del sitio
├── static/
│   ├── css/style.css        # Estilos
│   └── js/main.js           # Scripts
└── dist/                    # Salida (generado)
    ├── index.html
  ├── robots.txt
  ├── sitemap.xml           # Solo cuando public_url está configurada
    └── static/
```

## 🔧 Tecnologías

- **Python** - Lenguaje principal
- **Jinja2** - Motor de templates
- **Requests** - Para traer datos de GitHub API
- **HTML/CSS/JS** - Frontend
- **GitHub Pages** - Hosting gratuito

## ⚙️ Variables de `data.json`

```json
{
  "nombre": "Tu nombre",
  "titulo": "Tu profesión",
  "subtitulo": "Tecnologías que usas",
  "descripcion": "Descripción corta",
  "biografia": "Descripción larga",
  "habilidades": ["Skill1", "Skill2"],
  "github_user": "tu_usuario"
}
```

## 🚀 Workflow Típico

1. Haces cambios en `data.json` o templates
2. Ejecutas: `python generate_site.py`
3. Verifica los cambios en `dist/`
4. Ejecutas: `ghp-import -p dist/` para publicar
5. Tu portafolio se actualiza en GitHub Pages

## 📄 Licencia

MIT - Libre de usar y modificar

## 🤝 Soporte

Si tienes dudas, revisa:
- [GitHub API Docs](https://docs.github.com/en/rest)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)
- [GitHub Pages Docs](https://docs.github.com/en/pages)

---

**Hecho con ❤️ en Python**
