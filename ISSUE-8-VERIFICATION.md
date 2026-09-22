# Issue #8 - Publicacion y verificacion

Fecha: 2026-09-22

## Estado

**BLOQUEADA para cierre de produccion.** El build y la publicacion de las ramas se realizaron, pero GitHub Pages no esta habilitado o no es accesible para verificacion desde este entorno. No se declara una URL publica operativa sin evidencia HTTP real.

## Metodo de publicacion

Se mantuvo la arquitectura estatica existente:

```text
data.json + templates/ + static/ + generate_site.py
                      -> dist/
                      -> gh-pages
```

La fuente de verdad sigue siendo el codigo fuente. `dist/` continua ignorado por Git y se publica con `ghp-import`, sin editar manualmente las paginas generadas.

Comandos ejecutados:

```text
python generate_site.py
ghp-import -n -p -f dist
```

## Evidencia de build

La generacion termino correctamente con:

```text
[OK] Portafolio generado exitosamente!
```

La salida contiene las rutas publicas esperadas, CSS, JavaScript, `robots.txt` y `.nojekyll` en la rama de despliegue.

## Commits publicados

- `main`: `aa1498c8c1e2ac4faeb814630579e1a043523ed9`
- `gh-pages`: `5e113c37d1d5a92cd3a20319252b419128b18336`

El commit de `main` fue enviado a `origin/main` antes de publicar `dist/`.

## URL esperada

Por el nombre del repositorio, la URL esperada de GitHub Pages seria:

```text
https://askrueger.github.io/webportfolio/
```

Esta URL no se considera publica/verificada todavia. Las comprobaciones realizadas devolvieron:

- sitio raiz: HTTP 404
- `robots.txt`: HTTP 404
- `sitemap.xml`: HTTP 404
- API de Pages: HTTP 404

El repositorio HTTP tampoco pudo ser consultado anonimamente desde este entorno, aunque Git pudo publicar mediante las credenciales configuradas localmente. Esto impide distinguir de forma independiente entre Pages deshabilitado, repositorio privado o una configuracion de hosting no disponible.

## Rutas y assets preparados

La rama `gh-pages` contiene:

- `index.html`
- `proyectos/index.html`
- `proyectos/3d-cost-manager/index.html`
- `proyectos/explorersaga/index.html`
- `sobre-mi/index.html`
- `experiencia/index.html`
- `formacion/index.html`
- `contacto/index.html`
- `curriculum.html`
- `static/css/style.css`
- `static/js/main.js`
- `robots.txt`
- `.nojekyll`

## SEO de produccion

No se configuro `public_url` porque la URL no esta verificada. Por tanto, no se generaron canonical, `og:url` ni `sitemap.xml` con una URL inventada.

Cuando GitHub Pages este habilitado y la URL responda correctamente:

1. añadir `"public_url": "https://askrueger.github.io/webportfolio/"` en `data.json`;
2. ejecutar `python generate_site.py`;
3. volver a publicar `dist/` en `gh-pages`;
4. comprobar canonical, `og:url`, sitemap y robots desde HTTPS.

## Problemas encontrados

- GitHub Pages no responde en la URL esperada.
- `robots.txt` y `sitemap.xml` tampoco son accesibles en produccion.
- No fue posible ejecutar una auditoria de navegador sobre una URL publica real.
- No fue posible afirmar HTTPS, ausencia de mixed content, errores de consola ni rendimiento de produccion.

## Correcciones realizadas

- Se publico `main` con el estado verificado de Issues anteriores.
- Se publico el contenido generado de `dist/` en `gh-pages`.
- Se corrigio en README la URL esperada de `portfolio` a `webportfolio`.
- No se agrego `public_url` hasta disponer de una URL real verificada.

## Limitaciones

Lighthouse, axe, Node.js, npm y npx no estan disponibles. La validacion responsive y de accesibilidad existe para el entorno local, pero no se puede trasladar a produccion mientras Pages no sirva el sitio.

## Resultado

- Build: **VERIFICADO**
- Fuente `main` publicada: **VERIFICADO**
- Rama `gh-pages` publicada: **VERIFICADO**
- URL publica: **PENDIENTE / BLOQUEADA**
- Canonical y `og:url` reales: **PENDIENTE**
- Sitemap publico: **PENDIENTE**
- Robots publico: **PENDIENTE**
- Rutas, assets, HTTPS y consola en produccion: **PENDIENTE**

La Issue #8 no debe marcarse como `CLOSED` hasta que GitHub Pages este habilitado y la URL esperada devuelva el sitio generado mediante HTTPS.
