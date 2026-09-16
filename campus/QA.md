# Aceptación del campus y preparación de Pages

## Campus 2.1 · 16 de septiembre de 2026

El commit `d03f94062ed7ce887fe1ca0f7badb950c0eb84a2` superó el workflow [35089428413](https://github.com/WiktorNykiel/fundamentos-ciberseguridad/actions/runs/35089428413): compilación del curso real, validador de release, pruebas de estado/navegación, aceptación Chromium y regresiones del kit y planificación. La revisión posterior de este documento vuelve a ejecutar la CI; la conclusión de cada head se consulta en Actions.

| Grupo | Casos definidos y ejecutados en esa aceptación |
|---|---:|
| Compilador y release | 26 |
| Estado e importación | 22 |
| Navegación | 8 |
| Chromium: escritorio, presentación, prácticas, móvil y pestañas | 30 |
| **Campus** | **86** |

Se mantienen las regresiones independientes del kit y de planificación. Estas cifras no son horas impartidas, pruebas de penetración ni prácticas nativas Windows/macOS ejecutadas.

## Qué se comprueba

Catálogo de M01–M32; 96 fichas; 480 horas, 168 de teoría y 312 de práctica; 20 referencias con D01–D18 preservados; 8 guías ampliadas; navegación por índices, teoría, prácticas y revisión; búsqueda de varias palabras; presentación; persistencia local; exportación/importación Unicode; ausencia de bucles entre pestañas; conservación del punto de continuación local; notas tratadas como texto; CSP y ausencia de solicitudes externas de la aplicación durante las pruebas.

El validador `check_release.py` contrasta activos, manifiesto SHA-256, cabeceras y contenido exacto del ZIP frente al directorio de salida. Rechaza archivos modificados, activos ausentes y rutas incoherentes. No valida por sí solo la configuración que se introduzca después en una cuenta Cloudflare.

## Evidencias y artefactos

`campus-diagnostics` conserva logs y capturas incluso si hay fallos. `cloudflare-pages-ready` contiene `pages-ready.zip` únicamente después de superar las pruebas. `campus-web-v2` conserva las fuentes seleccionadas y el sitio validado. Los artefactos tienen retención limitada; conservar el ZIP aceptado antes de que caduquen.

`build-info.json` contiene la versión, cifras del catálogo, hash del catálogo y `sourceCommit` si Actions o Cloudflare proporcionan un SHA válido. En un evento pull_request ese SHA puede ser el merge de prueba; no debe confundirse con el head del PR o el merge definitivo. En local se registra null si no se proporciona el contexto, en lugar de inventarlo.

## Aplicación Next.js independiente

El workflow `Legacy app - dependency acceptance` comprueba npm ci, lint, tipos, compatibilidad y build. Ejecuta auditoría de producción y auditoría completa aunque una comprobación anterior falle, siempre que la instalación haya terminado correctamente. Los informes de auditoría se conservan como artefactos. Una auditoría sin hallazgos es el resultado de esa ejecución, no garantía de ausencia de vulnerabilidades.

Durante la revisión se detectó y corrigió una prueba que resolvía `@humanfs/node` con condiciones CommonJS pese a ser ESM-only. La corrección utiliza el export público de importación declarado por el paquete y conserva la prueba de lectura JSON, sin suprimirla ni asumir que todas las dependencias están elevadas al primer nivel de node_modules.

## Límites

No se ha desplegado automáticamente en Cloudflare, asignado dominio ni publicado una terminal remota. El asistente es una guía manual; el progreso es autodeclarado y vive en localStorage, sin sincronización entre dispositivos ni cifrado de notas. No se afirma haber ejecutado las 96 prácticas nativas, Docker/Swarm, modelos de IA o una cohorte docente.

La compilación local y las pruebas unitarias se ejecutaron también en el entorno de edición. Su navegador bloqueó la navegación local por política; no se alteró esa política. La aceptación visual se realiza en el runner de GitHub Actions y se conserva con sus capturas y logs.
