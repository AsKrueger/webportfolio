# Issue #8 - Publicacion y verificacion

Fecha: 2026-09-22

## Estado

**VERIFICACION DE PRODUCCION EN CURSO.** GitHub Pages ya responde en la URL publica y la nueva build esta publicada en `gh-pages`. El workflow de Pages del ultimo commit se encontraba `in_progress` durante la primera comprobacion del CV; se repite la comprobacion despues de su finalizacion.

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

- `main`: pendiente del commit final de esta verificacion
- `gh-pages`: `15d044e0` (publicacion de la build con `public_url`)

El commit de `main` fue enviado a `origin/main` antes de publicar `dist/`.

## URL esperada

Por el nombre del repositorio, la URL esperada de GitHub Pages seria:

```text
https://askrueger.github.io/webportfolio/
```

La URL publica verificada responde:

- sitio raiz: HTTP 200
- `robots.txt`: HTTP 200
- `sitemap.xml`: HTTP 200 despues de la propagacion de Pages

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

`public_url` esta configurada en `data.json` con la URL real. La build local contiene canonical, `og:url`, `robots.txt` y `sitemap.xml` con URLs bajo `https://askrueger.github.io/webportfolio/`.

## Problemas encontrados

- La primera respuesta del CV servido por Pages permanecia cacheada mientras el workflow de despliegue estaba `in_progress`.

## Correcciones realizadas

- Se configuro `public_url` con la URL real.
- Se regenero el sitio y se publico el contenido generado de `dist/` en `gh-pages`.
- Se corrigio el desbordamiento responsive de `curriculum.html` a 320px.
- Se eliminaron enlaces de descarga PDF que apuntaban a un archivo inexistente.
- Se actualizo README con la URL publica real.

## Limitaciones

Lighthouse, axe, Node.js, npm y npx no estan disponibles. La verificacion de consola y responsive se realiza con Playwright y comprobaciones HTTP directas.

## Resultado

- Build: **VERIFICADO**
- Fuente `main` publicada: **PENDIENTE DEL COMMIT FINAL**
- Rama `gh-pages` publicada: **VERIFICADO**
- URL publica: **VERIFICADO**
- Canonical y `og:url` reales: **VERIFICADO EN LA BUILD Y EN PAGINAS SERVIDAS**
- Sitemap publico: **VERIFICADO**
- Robots publico: **VERIFICADO**
- Rutas y assets principales: **VERIFICADO HTTP 200**
- HTTPS y ausencia de mixed content: **VERIFICADO EN LAS RESPUESTAS AUDITADAS**
- Responsive: **PENDIENTE DE REPETIR DESPUES DEL WORKFLOW FINAL**
- Consola: **SIN ERRORES EN LA AUDITORIA REALIZADA**
