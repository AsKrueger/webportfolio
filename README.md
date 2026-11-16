# Alonso Amador Sánchez · Portfolio

[![Build & deploy](https://github.com/AsKrueger/webportfolio/actions/workflows/deploy.yml/badge.svg)](https://github.com/AsKrueger/webportfolio/actions/workflows/deploy.yml)

**Desarrollador de Software Junior · Backend con Java y Spring Boot · Android con Kotlin** · Mérida, Extremadura · Disponibilidad inmediata

🌐 **[askrueger.github.io/webportfolio](https://askrueger.github.io/webportfolio/)** ([English](https://askrueger.github.io/webportfolio/en/)) · [CV en PDF](https://askrueger.github.io/webportfolio/cv/alonso-amador-sanchez-cv.pdf) · [LinkedIn](https://www.linkedin.com/in/alonso-amador) · [Email](mailto:alonsoamadorsanchez@gmail.com)

[![Vista previa del portfolio](static/img/og.png)](https://askrueger.github.io/webportfolio/)

---

## Proyectos destacados

| Proyecto | Qué es | Stack principal |
| --- | --- | --- |
| [**ExplorerSaga Extremadura**](https://github.com/AsKrueger/ExplorerSaga-Extremadura) | Guía turística de toda Extremadura sin conexión, con contenido generado por una fábrica de datos en Python (empezó como mi TFG) | Kotlin · Jetpack Compose · Room · MapLibre · Python |
| [**3D Cost Manager**](https://github.com/AsKrueger/Calculadora3D) | Coste real y precio de venta de cada impresión 3D, presupuestos en PDF e importación de G-code y 3MF, todo en el móvil (empezó como backend Spring Boot) | Kotlin · Jetpack Compose · Room |
| **AnimeWatchlist** (repositorio privado) | Listas de anime, calendario semanal de estrenos y dónde verlo | Kotlin · Jetpack Compose · Room · AdMob |
| **Training Arc** (repositorio privado) | Registro de entrenamientos convertido en un RPG con estética anime | Kotlin · Jetpack Compose · Room · ML Kit |
| [**BingoGoals**](https://github.com/AsKrueger/BingoGoals) | Metas en forma de cartón de bingo: app Android nativa con tests de capturas, más una PWA con API NestJS | Kotlin · Jetpack Compose · React · NestJS |

Las cinco apps están en prueba cerrada en Google Play. Cada una tiene en la web su caso técnico: el problema, **un fragmento de código real**, capturas o **diagrama de arquitectura** y el estado real del proyecto.

---

## Sobre este repositorio

El sitio es estático y lo genera un script de Python pequeño. No usa framework de frontend ni llama a APIs durante el build: el contenido sale de [`data.json`](data.json) y los textos de la interfaz de [`ui.json`](ui.json), así que el resultado es siempre el mismo.

```
data.json + ui.json + snippets/ ──► build.py (Jinja2 + Pygments) ──► dist/ (es + en + PDF) ──► GitHub Actions ──► gh-pages
```

```
.
├── build.py                 # generador: valida, traduce, resalta código, sitemap, PDF
├── data.json                # contenido; cada texto traducible es {"es": …, "en": …}
├── ui.json                  # textos de la interfaz en los dos idiomas
├── snippets/                # fragmentos literales de los repos que se enseñan en la web
├── templates/
│   ├── base.html            # layout, SEO, Open Graph, hreflang, selector de idioma
│   ├── index.html           # portada de una sola página
│   ├── project.html         # caso técnico → /proyectos/<slug>/ y /en/projects/<slug>/
│   ├── cv.html              # CV de una página A4 (también se exporta a PDF)
│   ├── diagrams/*.svg       # diagramas de arquitectura, adaptados al tema claro/oscuro
│   ├── 404.html · redirect.html · _macros.html
├── static/                  # CSS, JS sin dependencias, fuentes (OFL) e imágenes
├── tools/                   # plantilla y script de la imagen para redes (og.png)
└── .github/workflows/deploy.yml
```

### Detalles

- **Bilingüe**: español en `/` e inglés en `/en/`, con `hreflang` y selector de idioma en cada página.
- **CV en PDF**: `build.py --pdf` imprime `/cv/` con Chrome headless; el workflow lo hace en cada despliegue.
- **Código real con resaltado**: Pygments en tiempo de build, sin JavaScript.
- **Diagramas SVG en línea** que cambian de color con el tema.
- **Tema claro/oscuro**: sigue al sistema y recuerda la elección.
- **Accesibilidad**: HTML semántico, enlace para saltar al contenido, foco visible, `prefers-reduced-motion`, diagramas con descripción.
- **SEO y redes**: canonical, Open Graph con imagen 1200×630, `sitemap.xml`, `robots.txt` y JSON-LD `Person`.
- **Rendimiento**: fuentes alojadas en el propio sitio, sin librerías de terceros.
- **Enlaces antiguos**: `/sobre-mi/`, `/curriculum.html`, etc. redirigen a la sección nueva.
- **Validación**: el build falla si falta un campo obligatorio, si hay slugs repetidos o si un fragmento no existe.

## Desarrollo local

```bash
pip install -r requirements.txt
python build.py --serve          # http://localhost:8000
python build.py --pdf --serve    # también genera los PDF (necesita Chrome)
python tools/make_og.py          # regenera static/img/og.png
```

Para añadir un proyecto, añade un objeto a `projects` en `data.json`. Con `"featured": true` aparece en grande en la portada. Para que tenga diagrama, crea `templates/diagrams/<slug>.svg`; para enseñar código, añade un fichero en `snippets/` y una clave `snippet`.

## Despliegue

Cada push a `main` ejecuta [`deploy.yml`](.github/workflows/deploy.yml), que genera el sitio y los PDF y publica `dist/` en la rama `gh-pages`. En los pull requests solo se comprueba que el build funciona.

## Licencia

Código bajo [MIT](LICENSE) © Alonso Amador Sánchez. Fuentes Inter y JetBrains Mono bajo SIL Open Font License.
