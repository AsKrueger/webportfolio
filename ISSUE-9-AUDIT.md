# Issue #9 - Auditoria transversal del ecosistema profesional

Fecha de auditoria: 2026-09-22
Estado: **OPEN - AUDIT PASSED WITH CORRECTIONS REQUIRED**
Tipo: auditoria de consistencia, evidencia y posicionamiento

## Alcance y fuentes

Se revisaron:

- PortfolioWeb local y publicado en `https://askrueger.github.io/webportfolio/`.
- `data.json`, templates y README del repositorio `webportfolio`.
- GitHub Profile `AsKrueger`.
- Repositorios publicos `Calculadora3D`, `ExplorerSaga-Extremadura`, `webportfolio` y `Alonso-Amador`.
- CV generado en `curriculum.html`.
- URL de LinkedIn configurada en el portfolio.

La auditoria de LinkedIn no pudo completarse porque LinkedIn redirige a un auth wall de registro. No se infieren datos no visibles.

## Resultado ejecutivo

La identidad principal es coherente en tres superficies verificables:

```text
Junior Software Developer
Java / Spring Boot / SQL / REST / PostgreSQL
```

GitHub Profile muestra exactamente esa orientacion y tiene fijados `Calculadora3D` y `ExplorerSaga-Extremadura`. El repositorio `Alonso-Amador` repite el titular, presenta Calculadora3D como Java/Spring/PostgreSQL y ExplorerSaga como Kotlin/Android/Compose. PortfolioWeb mantiene la misma direccion general.

El resultado no es un `AUDIT PASSED` limpio porque existen dos zonas que requieren correccion o evidencia adicional:

1. ExplorerSaga aparece en PortfolioWeb como proyecto con backend Java/Spring Boot en evolucion, pero su README publico verificable lo presenta como aplicacion Android nativa en Kotlin, Jetpack Compose, MVVM, Room y OpenStreetMap. No documenta un backend Java/Spring Boot activo.
2. PortfolioWeb muestra para 3D Cost Manager `JPA / Hibernate`, `Flyway` y `Maven`, y describe arquitectura, persistencia y API con mas detalle del que confirma el README publico revisado. El README confirma Java, Spring Boot, PostgreSQL, Docker, Git/GitHub, JUnit, Mockito y OpenAPI/Swagger, pero no esos tres elementos concretos.

No se realizaron cambios de produccion como parte de esta auditoria.

## Evidencia por activo

### GitHub Profile

Resultado: coherente con el posicionamiento.

Evidencia visible:

- Nombre: Alonso Amador.
- Titular: `Junior Software Developer Java · Spring Boot · SQL · REST · PostgreSQL`.
- Repositorios fijados: `ExplorerSaga-Extremadura` y `Calculadora3D`.
- Descripciones fijadas: turismo en Kotlin para ExplorerSaga y calculadora de impresion 3D en Java para Calculadora3D.
- El perfil muestra cuatro repositorios publicos.

Gap:

- El perfil no fija `webportfolio` ni `Alonso-Amador`, aunque ambos son activos de presentacion relevantes.
- Prioridad: P2. No bloquea la comprension del perfil porque los dos proyectos tecnicos principales si estan visibles.

### PortfolioWeb

Resultado: posicionamiento claro, con claims tecnicos que requieren ajuste de evidencia.

Aciertos:

- Titular principal: `Junior Software Developer`.
- Orientacion: `Backend Java / Spring Boot`.
- Diferencia explicitamente experiencia de practicas, formacion y proyectos.
- Incluye paginas de proyecto, repositorios, contacto, CV, SEO y publicacion estatica.
- La pagina de proyectos marca ambos proyectos como `En evolucion`, evitando presentarlos como terminados.

Discrepancias:

- La tarjeta y detalle de ExplorerSaga incluyen Java, Spring Boot, PostgreSQL, JUnit y Docker dentro de una narrativa backend, mientras el README publico revisado describe principalmente el cliente Android y deja el backend fuera de la implementacion documentada.
- El detalle de 3D Cost Manager afirma JPA/Hibernate, Flyway y Maven, pero el README publico revisado no los enumera.
- La portada consume repositorios recientes de GitHub y puede mostrar `webportfolio`, `Alonso-Amador` y `Calculadora3D`, mientras `/proyectos/` presenta la seleccion curada de 3D Cost Manager y ExplorerSaga. La diferencia es explicable por la integracion API, pero reduce la coherencia de la primera impresion.

### Calculadora3D / 3D Cost Manager

README publico verificable:

- Dominio: gestion y estimacion de costes de impresion 3D y postprocesado.
- Estado: `Proyecto en desarrollo`.
- Tecnologias declaradas: Java, Spring Boot, PostgreSQL, Docker, Git/GitHub, JUnit, Mockito, OpenAPI/Swagger.
- El repositorio contiene `backend/`, `android/`, `docker-compose.yml`, `.env.example` y tiene una Issue abierta visible.

Claims respaldados por README:

- Java: implementado/documentado.
- Spring Boot: implementado/documentado.
- PostgreSQL: implementado/documentado.
- Docker: implementado/documentado.
- JUnit y Mockito: documentados; debe confirmarse cobertura real en codigo si se quiere elevar el claim.
- OpenAPI/Swagger: documentado.

Claims que requieren comprobacion adicional antes de mostrarlos como evidencia publica:

- JPA/Hibernate.
- Flyway.
- Maven.
- REST como implementacion concreta, aunque OpenAPI/Swagger aporta una señal compatible.
- BigDecimal.
- Arquitectura de dominio/capas.

Clasificacion: proyecto **En evolucion**. No debe presentarse como terminado.

### ExplorerSaga-Extremadura

README publico verificable:

- TFG sobre desarrollo de aplicaciones moviles Android.
- Kotlin y Jetpack Compose.
- MVVM.
- Navegacion Compose.
- OpenStreetMap mediante `osmdroid-android`.
- Room para persistencia local, segun las lineas de trabajo documentadas.
- Funcionalidades implementadas: bienvenida, contexto historico, categorias, listados y mapa.
- Testing aparece como tarea pendiente (`[ ]`).
- El repositorio contiene una aplicacion Gradle/Android y un archivo `kotlin_errors.txt`, que deberia revisarse como posible artefacto de desarrollo.

Claims respaldados:

- Kotlin: implementado/documentado.
- Android: implementado/documentado.
- Jetpack Compose: implementado/documentado.
- MVVM: documentado.
- Room: documentado como persistencia prevista/implementada en la lista de trabajo.
- OpenStreetMap/osmdroid: implementado/documentado.

Claims no respaldados por el README publico revisado:

- Backend Java/Spring Boot.
- PostgreSQL.
- JUnit en backend.
- Docker como despliegue backend.
- APIs REST propias.

Clasificacion: proyecto Android/TFG **En evolucion**. Debe separarse claramente de la evidencia backend Java.

### PortfolioWeb como proyecto

Resultado: coherente si se presenta como herramienta de generacion y publicacion, no como backend Java.

Evidencia:

- README: Python, Jinja2, HTML/CSS/JavaScript, Requests, GitHub API y GitHub Pages.
- Codigo: generacion estatica hacia `dist/`, templates Jinja2, fallback local y publicacion en `gh-pages`.
- Produccion: `https://askrueger.github.io/webportfolio/`.
- SEO, responsive, accesibilidad y despliegue estan documentados en los informes de Issues anteriores.

No debe mezclarse con la evidencia de Java/Spring Boot.

### Alonso-Amador

Resultado: coherente y util como README de perfil.

Evidencia visible:

- Titular: `Junior Software Developer | Java · Spring Boot · SQL · REST`.
- Resumen: formacion DAM, experiencia practica y especializacion actual en backend.
- Calculadora3D: Java / Spring Boot / PostgreSQL.
- ExplorerSaga: Kotlin / Android / Jetpack Compose.
- Tecnologias separadas entre stack backend y tecnologias complementarias.
- Enlace visible a LinkedIn, aunque la pagina no fue auditable por auth wall.

Este README distingue mejor que PortfolioWeb el cliente Android de la especializacion backend.

### CV

Se audito el CV generado en `curriculum.html`, no un PDF externo.

Coherencias:

- Titulo `Junior Software Developer`.
- Experiencia de practicas separada de proyectos personales.
- Formacion DAM.
- Contacto y navegacion hacia GitHub/LinkedIn.

Limitaciones:

- El CV generado no contiene una seccion explicita de proyectos tecnicos con enlaces a Calculadora3D, ExplorerSaga, PortfolioWeb o LinkedIn dentro del contenido principal.
- El enlace PDF fue retirado porque no existia un archivo publico verificable en `static/cv/`.
- Las habilidades se mantienen principalmente en `data.json`; su representacion en el CV debe confirmarse si se pretende usarlo como documento de candidatura.

Prioridad: P1 para mejorar la evidencia de proyectos en el CV; no es una contradiccion factual.

### LinkedIn

Resultado: no verificable desde esta auditoria.

La URL configurada es:

```text
https://www.linkedin.com/in/alonso-amador-sanchez
```

La peticion publica redirige a LinkedIn auth wall. No se puede confirmar el titular, About, experiencia, skills, proyectos o enlaces actuales. Esto debe quedar como pendiente de verificacion manual por el propietario de la cuenta.

## Matriz de coherencia

| Afirmacion | GitHub Profile | PortfolioWeb | CV generado | LinkedIn | Evidencia actual | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| Junior Software Developer | Si | Si | Si | No verificable | Profile, README, portfolio y CV | Implementado |
| Backend Java / Spring Boot | Si | Si | Parcial | No verificable | Profile, README de perfil y Calculadora3D | Implementado en posicionamiento; evidencia de proyecto parcial |
| Java | Si | Si | Parcial | No verificable | Profile, Alonso-Amador, Calculadora3D | Implementado/documentado |
| Spring Boot | Si | Si | Parcial | No verificable | Profile, Alonso-Amador, Calculadora3D | Implementado/documentado |
| REST | Si | Si | No visible como seccion propia | No verificable | Profile y PortfolioWeb; OpenAPI/Swagger en Calculadora3D | Documentado; requiere verificar endpoints |
| PostgreSQL | Si | Si | No visible como seccion propia | No verificable | Profile, Alonso-Amador, Calculadora3D | Implementado/documentado |
| JPA / Hibernate | No visible | Si | No visible | No verificable | Solo claim de PortfolioWeb/data.json | Requiere evidencia |
| Flyway | No visible | Si | No visible | No verificable | Solo claim de PortfolioWeb/data.json | Requiere evidencia |
| Maven | No visible | Si | No visible | No verificable | Solo claim de PortfolioWeb/data.json | Requiere evidencia |
| Docker | Si en stack de perfil | Si | No visible | No verificable | Calculadora3D README y perfil Alonso-Amador | Implementado/documentado |
| JUnit | Si en stack de perfil | Si | No visible | No verificable | Calculadora3D README | Documentado; cobertura pendiente |
| Mockito | No visible en perfil | Si | No visible | No verificable | Calculadora3D README | Documentado; cobertura pendiente |
| Kotlin / Android | Si por repositorio fijado | Si | No visible | No verificable | ExplorerSaga README y perfil | Implementado/documentado |
| Jetpack Compose | Si por repositorio | Si | No visible | No verificable | ExplorerSaga README | Implementado/documentado |
| MVVM | No visible | No | No visible | No verificable | ExplorerSaga README | Implementado/documentado en Android |
| C# / .NET / Unity | No visible en titular | Si en experiencia | En experiencia | No verificable | `data.json` y README de perfil | Experiencia de practicas declarada |
| Portfolio estatico Python/Jinja2 | No | Si | No | No verificable | README y codigo webportfolio | Implementado |

## Clasificacion de claims

### Implementado/documentado

- Perfil Junior Software Developer.
- Java y Spring Boot como orientacion profesional.
- Calculadora3D con Java, Spring Boot, PostgreSQL, Docker, JUnit, Mockito y OpenAPI/Swagger, segun su README.
- ExplorerSaga como aplicacion Android con Kotlin, Compose, MVVM, Room y OpenStreetMap, segun su README.
- PortfolioWeb como generador estatico Python/Jinja2 publicado en GitHub Pages.
- Experiencia de practicas con C#, Unity y .NET, segun `data.json` y README de perfil.

### En evolucion

- Calculadora3D: el propio README indica proyecto en desarrollo.
- ExplorerSaga: el README contiene lineas de trabajo futuras, incluyendo testing y accesibilidad.
- Especializacion backend de Alonso: posicionamiento valido, pero la evidencia publica principal se concentra en Calculadora3D.

### Requiere evidencia antes de elevar el claim

- JPA/Hibernate, Flyway, Maven y BigDecimal en Calculadora3D.
- Backend Java/Spring Boot, PostgreSQL, Docker y JUnit propios de ExplorerSaga.
- REST como API implementada en cada proyecto, frente a documentacion OpenAPI o cliente Retrofit.
- Cobertura de tests, especialmente en ExplorerSaga, cuyo README marca testing como pendiente.

### Planificado o no verificable

- Mejoras futuras enumeradas en ExplorerSaga: multimedia, rutas, i18n y accesibilidad.
- LinkedIn: titular, About, skills y experiencia no verificables sin acceso autenticado.

## Inconsistencias priorizadas

### P1 - ExplorerSaga se presenta parcialmente como backend Java/Spring

- Ubicacion: `data.json`, `templates/proyecto.html`, pagina publicada de ExplorerSaga.
- Problema: PortfolioWeb incluye Java, Spring Boot, PostgreSQL, JUnit y Docker en el proyecto, pero el README publico revisado documenta un TFG Android/Kotlin/Compose/MVVM y no documenta backend Java/Spring.
- Impacto: puede hacer que un revisor atribuya experiencia backend no demostrada al proyecto.
- Evidencia: README publico de ExplorerSaga y pagina de proyecto del portfolio.
- Recomendacion: separar explicitamente `Cliente Android / Kotlin` de `Backend en evolucion` y marcar cualquier backend como planificado o no verificable hasta aportar codigo, README y endpoints.

### P1 - Claims de Calculadora3D mas amplios que su README publico

- Ubicacion: `data.json`, pagina de detalle y tarjeta de proyectos.
- Problema: PortfolioWeb muestra JPA/Hibernate, Flyway y Maven, mientras el README publico enumera Java, Spring Boot, PostgreSQL, Docker, Git/GitHub, JUnit, Mockito y OpenAPI/Swagger.
- Impacto: riesgo de sobrepresentar tecnologias no comprobadas por la documentacion principal.
- Evidencia: README publico de Calculadora3D frente a `data.json`.
- Recomendacion: auditar el codigo del repositorio y, si no hay evidencia directa, mover esas tecnologias a aprendizaje/en evolucion o retirarlas de la presentacion publica.

### P1 - CV con poca evidencia de proyectos

- Ubicacion: `templates/curriculum.html` y `dist/curriculum.html`.
- Problema: el CV publico muestra experiencia, formacion y certificaciones, pero no presenta una seccion clara de proyectos con enlaces.
- Impacto: el documento no aprovecha la evidencia tecnica que sostiene el posicionamiento backend.
- Recomendacion: Issue independiente para añadir proyectos reales y enlaces, sin inventar resultados ni tecnologias.

### P2 - Primera impresion mezcla repositorios dinamicos y proyectos curados

- Ubicacion: `templates/index.html` frente a `templates/proyectos.html`.
- Problema: la portada puede mostrar repositorios recientes genericos, mientras `/proyectos/` muestra los dos proyectos seleccionados como evidencia profesional.
- Impacto: menor control narrativo y posible confusion sobre cuales son los proyectos principales.
- Recomendacion: decidir si la portada debe mostrar solo `featured_projects` curados o etiquetar claramente la seccion API como repositorios recientes.

### P2 - LinkedIn no verificable

- Ubicacion: `data.json`, `templates/base.html`, `templates/contacto.html`.
- Problema: la URL es valida como enlace, pero el contenido profesional no pudo auditarse por auth wall.
- Impacto: no se puede confirmar consistencia entre LinkedIn, CV, GitHub y PortfolioWeb.
- Recomendacion: auditoria manual autenticada por el propietario y posterior correccion independiente si aparecen diferencias.

### P2 - Artefacto de desarrollo visible en ExplorerSaga

- Ubicacion: repositorio publico `ExplorerSaga-Extremadura`, archivo `kotlin_errors.txt`.
- Problema: un archivo con nombre de errores de Kotlin es visible en la raiz del repositorio.
- Impacto: puede transmitir estado de depuracion no resuelto y reduce la presentacion profesional.
- Recomendacion: revisar si es necesario; eliminarlo solo en una Issue posterior y despues de confirmar que no contiene informacion util o necesaria.

## Enlaces auditados

Verificados como accesibles o referenciados correctamente:

- PortfolioWeb publico.
- GitHub Profile.
- `Calculadora3D`.
- `ExplorerSaga-Extremadura`.
- `webportfolio`.
- `Alonso-Amador`.
- LinkedIn: enlace configurado, contenido no verificable por auth wall.

No se detectaron en la fuente del PortfolioWeb URLs `localhost` o de ejemplo dentro de la navegacion publicada.

## Plan de correccion propuesto

No se implementan correcciones dentro de esta auditoria. Se proponen Issues posteriores en este orden:

1. **Issue futura P1 - Alinear ExplorerSaga con su evidencia real**: distinguir Android/cliente de backend; revisar technologies, testing, Room y estado.
2. **Issue futura P1 - Verificar y ajustar claims de Calculadora3D**: confirmar JPA/Hibernate, Flyway, Maven, BigDecimal, REST y arquitectura directamente en codigo/configuracion.
3. **Issue futura P1 - Mejorar CV con proyectos reales**: añadir Calculadora3D, ExplorerSaga y PortfolioWeb con enlaces y estados honestos.
4. **Issue futura P2 - Decidir estrategia de proyectos destacados**: curar la portada o rotular los repositorios API como recientes.
5. **Issue futura P2 - Revisar higiene publica de ExplorerSaga**: evaluar `kotlin_errors.txt`, Issues, README y estado de testing.
6. **Tarea manual P2 - Auditar LinkedIn autenticado**: contrastar titular, About, experiencia, skills, proyectos y enlaces.

## Veredicto

**AUDIT PASSED WITH CORRECTIONS REQUIRED**

La identidad profesional central es consistente y creible, pero no debe cerrarse la Issue #9 como `AUDIT PASSED` limpio hasta resolver o aceptar formalmente los claims de ExplorerSaga y las tecnologias no confirmadas de Calculadora3D. La auditoria no modifico codigo, contenido profesional ni repositorios externos.
