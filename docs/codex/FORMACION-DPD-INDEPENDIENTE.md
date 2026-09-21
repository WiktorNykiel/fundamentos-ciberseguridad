# Encargo actualizado: awesome-dpd independiente

Este documento es únicamente un traspaso de instrucciones. El curso DPD NO debe alojarse en este repositorio. Sustituye el encargo anterior de integración y la ruta de publicación anterior.

## Destino obligatorio

Repositorio público propio: `smartkea-cyberinnovation/awesome-dpd`.
URL: `https://smartkea.com/formacion-dpd/`.
Worker: `smartkea-formacion-dpd`.

`smartkea-cyberinnovation/fundamentos-ciberseguridad` puede enlazarse como complemento educativo. No es repositorio padre, submódulo, dependencia de compilación ni origen de datos. No hay que fusionar este PR ni desplegar Fundamentos para publicar el curso independiente.

## Material de esta entrega

Utiliza el paquete `awesome-dpd-independiente-2026-09-21.zip` o el bundle `awesome-dpd-independiente-2026-09-21.bundle` adjunto a la conversación. No supongas que enlaces sandbox de otras conversaciones están disponibles en tu entorno. Comprueba los archivos presentes.

El bundle contiene una historia completa e independiente con main en `a54824969ffd8fda64889e4fd9b5adea5ca2619e`. Su árbol tiene 119 archivos versionados. Se clonó en un directorio separado y allí se repitieron las 190 pruebas unitarias y la compilación sin ningún checkout de Fundamentos.

La entrega incorpora 16 unidades, 120 horas propuestas de autoestudio, 180 preguntas originales, 12 casos con ramas, seis itinerarios, 24 prácticas guiadas, 36 preguntas de diagnóstico adicionales y los materiales complementarios. El README está dirigido al estudio; LICENCIA.md, PRIVACIDAD.md, TECNICO.md y DESPLIEGUE.md separan las otras funciones.

## Ejecución

Clona el bundle en un directorio vacío. El remote generado por git clone apunta al archivo local: elimínalo antes de utilizar el helper de creación. Lee AGENTS.md y ejecuta el encargo completo incluido en `docs/PROMPT-CODEX-FORMACION-DPD.md`.

Comprueba si el repositorio de destino existe. Si no existe y dispones de autorización administrativa, créalo público con el helper `tools/create_repository.py --apply`, que requiere main limpio y ausencia de remotes. Si existe, revisa su contenido y reconcilia con rama/PR, sin sobreescritura o force-push. No crees otra carpeta DPD dentro de Fundamentos para sortear un bloqueo administrativo.

No incorpores datos personales, documentos empresariales, contratos, auditorías, certificados reales, URLs privadas ni preguntas de exámenes reservados. Solo contenido original y ejemplos sintéticos; no basta renombrar un expediente real. No impongas licencias a material previo o ajeno sin decisión del titular.

Ejecuta `npm test`, `npm run check:public` y `npm run build`. Resuelve y fija una versión revisada de Wrangler con lockfile real en un entorno con npm disponible; ejecuta npm ci y dry-run. La entrega no inventa un lockfile ni afirma haber ejecutado el runtime de Workers.

El build de la raíz autónoma genera `public/formacion-dpd/`. Usa exclusivamente las rutas `smartkea.com/formacion-dpd` y `smartkea.com/formacion-dpd/*`, ASSETS y un Worker propio. No captures el apex, no uses `/formacion-dpd*` ni cambies DNS/WAF globales. Revisa normalización exacta de la entrada sin barra con query, prioridad de redirects y baseline del resto del sitio. La regla de ejemplo está desactivada y Wrangler no la aplica automáticamente.

Completa CI y un único controlador de release protegido. Utiliza solo secretos y sesiones ya autorizados, sin copiarlos fuera de su ámbito ni publicarlos. Prueba con navegación real en Chromium y WebKit sobre Wrangler y preview antes de producción. Los 12 escenarios DOM de esta entrega no equivalen a esa aceptación: la navegación HTTP local del entorno de autoría está bloqueada por política administrativa, que se ha respetado.

Publica primero preview sin rutas de smartkea.com. Después del preflight y la aceptación, despliega producción y verifica externamente inicio, unidades, examen, casos, healthz, MIME, HEAD y 404, así como la entrada sin barra con query. Confirma que portada y rutas hermanas no cambian. Conserva commit, huella, versión y deployment; revierte solo los cambios DPD capturados ante una regresión.

## Estado verificable

El repositorio remoto independiente y el Worker NO se han creado desde el conector de esta entrega: el conector no expone creación administrativa de repositorios y no hay una sesión Cloudflare autorizada. El proyecto local y el bundle sí están creados y validados. No interpretar esta actualización documental como publicación del curso ni utilizar los resultados de este PR antiguo como aceptación de producción.
