# Issue #10 - Reconciliacion tecnica y documental de ExplorerSaga

Fecha: 2026-09-25
Estado: **IMPLEMENTADA EN PORTFOLIOWEB; REPOSITORIO EXTERNO PENDIENTE DE DOCUMENTACION PROPIA**

## Veredicto

ExplorerSaga se presenta ahora como:

> Aplicacion turistica Android funcional que utiliza Kotlin, Jetpack Compose, MVVM, Room/SQLite, assets JSON y OpenStreetMap/osmdroid. El backend Java/Spring Boot es una linea de evolucion planificada y no una funcionalidad presente en el repositorio publico auditado.

No se ha implementado ningun backend para sostener un claim profesional.

## Evidencia auditada

El arbol publico de `AsKrueger/ExplorerSaga-Extremadura` contiene:

- proyecto Android/Gradle bajo `app/`;
- Kotlin, Compose, Navigation Compose y Material Design 3;
- ViewModels con Coroutines/StateFlow;
- `PlaceEntity`, `PlaceDao`, `AppDatabase` y Room;
- assets JSON para monumentos, gastronomia y tiendas;
- OpenStreetMap mediante osmdroid;
- tests unitarios e instrumentados de ejemplo;
- `PROJECT_STATUS.md`, `COMPLETED_ISSUES.md`, `README.md` y `kotlin_errors.txt`.

No se encontraron en el arbol publico auditado:

- proyecto Java/Spring Boot;
- `pom.xml` o modulo backend Maven;
- controllers REST;
- services/repositories Java;
- entidades JPA/Hibernate;
- migraciones Flyway;
- configuracion PostgreSQL;
- Dockerfile o `docker-compose.yml`;
- endpoints REST propios;
- tests backend JUnit/Mockito.

## Clasificacion de tecnologias

| Tecnologia | Estado | Evidencia |
| --- | --- | --- |
| Kotlin | Implementado | Codigo Android bajo `app/src/main` |
| Android | Implementado | Modulo Gradle y `MainActivity` |
| Jetpack Compose | Implementado | Pantallas Compose |
| Navigation Compose | Implementado | `AppNavigation.kt` |
| Material Design 3 | Implementado | Theme, Scaffold, Card, Button |
| MVVM | Implementado | ViewModels y estado Compose |
| Coroutines / StateFlow | Implementado | `PlacesViewModel.kt` |
| Room | Implementado | `AppDatabase`, `PlaceDao`, `PlaceEntity` |
| SQLite | Implementado mediante Room | Base de datos local `explorer_saga_database` |
| JSON local | Implementado | `app/src/main/assets/*.json` y `kotlinx.serialization` |
| OpenStreetMap / osmdroid | Implementado | `MapScreen.kt`, configuracion de User-Agent |
| REST propio | Planificado | No hay endpoints propios en el arbol auditado |
| Java / Spring Boot | Planificado | No hay modulo Java/Spring en el arbol auditado |
| PostgreSQL | Planificado | No hay configuracion PostgreSQL |
| JPA / Hibernate | Planificado | No hay entidades ni dependencias verificables |
| Flyway | Planificado | No hay migraciones ni configuracion |
| Docker | Planificado | No hay Dockerfile ni compose |
| JUnit / Mockito de backend | No implementado en este proyecto | Solo tests Android de ejemplo visibles |
| Retrofit | No verificado | No se encontro uso verificable en la auditoria |

## Integracion Android ↔ backend

No existe integracion real con una API REST propia en el repositorio auditado.

El flujo actual es local:

```text
assets JSON -> Repository -> Room/SQLite -> ViewModel -> Compose
```

La arquitectura cliente-servidor queda documentada como evolucion futura:

```text
Android/Kotlin/Compose -> API REST Java/Spring Boot -> PostgreSQL
```

No debe presentarse como una integracion ya operativa.

## Cambios aplicados en PortfolioWeb

Se actualizo `data.json` para que ExplorerSaga muestre:

- estado: `Android funcional · Backend planificado`;
- resumen centrado en Android/Kotlin/Compose/Room/OpenStreetMap;
- arquitectura Android actual y backend futuro claramente separado;
- tecnologias verificables del repositorio actual;
- testing limitado a tests de ejemplo, sin inventar cobertura;
- ausencia de API REST propia;
- despliegue Android/Gradle, sin Docker backend;
- tags Android/Kotlin/Compose/Room en lugar de backend Java/Spring.

Tambien se actualizo `ISSUE-9-AUDIT.md` para reflejar que el claim original era una discrepancia y que la correccion se realiza desde PortfolioWeb.

No se modifico el repositorio externo de ExplorerSaga desde este workspace.

## `kotlin_errors.txt`

El archivo existe en la raiz publica y tiene tamano relevante. Por su nombre y ubicacion se clasifica como posible artefacto de compilacion/desarrollo, no como documentacion de producto. No se elimina automaticamente porque la modificacion del repositorio externo no forma parte de este workspace.

Accion recomendada para una futura tarea del repositorio ExplorerSaga:

1. inspeccionar su contenido para confirmar que no contiene secretos;
2. decidir si aporta valor historico;
3. moverlo a documentacion o eliminarlo;
4. actualizar `.gitignore` para evitar nuevos artefactos equivalentes.

## Limitaciones

- No se ejecuto Android Studio/Gradle desde este workspace porque el repositorio ExplorerSaga no esta clonado localmente.
- La verificacion se hizo contra el arbol y archivos publicos de GitHub.
- No se puede confirmar el contenido de LinkedIn desde esta auditoria.
- No se publicaron cambios del PortfolioWeb todavía en esta Issue; la build/publicacion debe repetirse después de la correccion de `data.json`.

## Resultado

- Estado tecnico del cliente Android: **verificado**.
- Estado de Room/SQLite y assets JSON: **verificado**.
- Backend Java/Spring Boot: **no presente; correctamente clasificado como planificado**.
- Integracion Android/backend: **pendiente y correctamente declarada**.
- Claims del PortfolioWeb: **reconciliados en fuente**.
- README externo de ExplorerSaga: **pendiente de actualizar en su propio repositorio**.
- `kotlin_errors.txt`: **revisado como artefacto pendiente de decision**.
- Tests reales del proyecto: **limitados a ejemplos visibles; no se inventa cobertura**.
