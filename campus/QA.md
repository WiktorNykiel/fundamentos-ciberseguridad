# Aceptación del campus y preparación de Cloudflare

## Edición 2.2: alcance de las nuevas comprobaciones

Se añaden 13 contratos offline del wrapper de despliegue y conservación de rutas D01–D20, y ocho pruebas de filtros del índice. Las 31 pruebas de navegador existentes se amplían con seis casos: filtrado por bloque, texto y progreso, estado vacío/reinicio, nueva lección D21, filtros en móvil y salto a un bloque oculto por filtros previos.

El workflow `Cloudflare - static deployment acceptance` usa Wrangler 4.132.0 con `--dry-run` y runtime `--local`, sin credenciales Cloudflare ni cambios remotos. Comprueba contenido, MIME, CSP y HTTP 404. Los resultados se consultan en la ejecución concreta; ningún workflow de esta edición publica en una cuenta. Las pruebas unitarias no demuestran que el runtime o navegador se haya ejecutado.

El catálogo mantiene M01–M32, 96 fichas, 480 horas (168 teoría/312 práctica), ocho guías ampliadas y 170 secciones de presentación. La biblioteca pasa a 21 referencias sin alterar el significado de D01–D20. El índice permite filtros sin modificar el progreso.

## Qué se comprueba

Identidad y carga del catálogo; coincidencia de activos y ZIP; manifiesto SHA-256; cabeceras; navegación por índices, teoría, prácticas y revisión; búsqueda de varias palabras; presentación; persistencia local; exportación/importación Unicode; ausencia de bucles entre pestañas; conservación del punto de continuación local; notas tratadas como texto; CSP y ausencia de solicitudes externas de la aplicación durante las pruebas de navegador.

`cloudflare.py` verifica una configuración estática explícita, resuelve rutas desde el archivo y nunca construye comandos con shell. Un fallo de build o validación impide llamar a Wrangler. `deploy` y `preview` son acciones remotas explícitas; no se ejecutan durante CI. `dry-run` puede descargar la CLI, pero no publica una versión.

## Evidencias y artefactos

`campus-diagnostics` conserva logs y capturas incluso si hay fallos. `cloudflare-pages-ready` contiene `pages-ready.zip` únicamente después de superar las pruebas del campus. `campus-web-v2` conserva las fuentes seleccionadas y el sitio validado. El workflow independiente de Cloudflare conserva `cloudflare-static-diagnostics`. Los artefactos tienen retención limitada; conservar el ZIP aceptado antes de que caduquen.

`build-info.json` incluye versión, cifras, hash del catálogo y `sourceCommit` cuando puede determinarse. En pull_request puede identificar el merge de prueba: no confundirlo con el head del PR o el merge definitivo. En una copia local modificada o sin Git se utiliza null en lugar de atribuirle un commit limpio. Un manifiesto no demuestra autoría ni seguridad integral.

## Historial de aceptación 2.1

El commit `d03f94062ed7ce887fe1ca0f7badb950c0eb84a2` superó [35089428413](https://github.com/WiktorNykiel/fundamentos-ciberseguridad/actions/runs/35089428413). La revisión final `1388d1d619eef51b8f09bd277789f2a544d04ce2` añadió persistencia de la ruta propia en sessionStorage y superó [35090478719](https://github.com/WiktorNykiel/fundamentos-ciberseguridad/actions/runs/35090478719): 26 Python, 31 JavaScript y 31 Chromium. Su merge en main `ffb73a3cb659c34d9881396c7706df99fe2b1881` superó [35091157812](https://github.com/WiktorNykiel/fundamentos-ciberseguridad/actions/runs/35091157812). Estas ejecuciones históricas no certifican cambios posteriores.

## Aplicación Next.js independiente

Su workflow comprueba npm ci, lint, tipos, compatibilidad y build. Ejecuta auditoría de producción y completa aunque una comprobación anterior falle, siempre que la instalación haya terminado correctamente. La edición 2.2 no cambia esa aplicación ni sus dependencias; no se incorpora Next.js al campus. Una auditoría sin hallazgos es el resultado de una ejecución, no una garantía permanente.

## Límites

No se ha desplegado automáticamente en Cloudflare, asignado dominio ni publicado una terminal remota. El asistente es una guía manual; el progreso es autodeclarado y local, sin sincronización entre dispositivos ni cifrado de notas. No se afirma haber ejecutado los 96 laboratorios nativos, Docker/Swarm, modelos de IA o una cohorte docente.

El navegador del entorno de edición bloqueó la navegación local por política; no se alteró esa política. La aceptación visual se ejecuta en GitHub Actions y se conserva con capturas y logs. La aceptación del runtime local de Workers no sustituye la verificación de la URL tras el despliegue real.
