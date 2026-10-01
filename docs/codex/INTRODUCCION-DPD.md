# Misión Codex: awesome-dpd público y smartkea.com/introduccion-dpd

Ejecuta la implementación, integración, configuración, pruebas y despliegue. No te
limites a recomendar pasos. Trabaja con las autorizaciones existentes y conserva
el trabajo ajeno. La autorización de despliegue corresponde a Introducción DPD:
no despliegues ni cambies el Worker de Fundamentos durante esta misión.

## Resultado requerido

Repositorio público canónico `smartkea-cyberinnovation/awesome-dpd`, aplicación
real en `https://smartkea.com/introduccion-dpd/`, entrada sin barra funcional,
contenido V2 reconciliado, CI comprobable, Worker independiente, evidencias y
rollback. No declares terminado mientras la URL no responda con la versión
correcta y las pruebas de aceptación no estén aprobadas. Si falta un permiso o
credencial, completa lo demás y entrega el bloqueo exacto; no inventes éxitos.

## Contexto que debes volver a comprobar

El repositorio accesible al preparar esta tarea era
`WiktorNykiel/fundamentos-ciberseguridad`. PR #22: integración de ramas, seis
perfiles y una primera versión de awesome-dpd, rama
`maintenance/rutas-dpd-integracion-20260918`, cabeza observada
`5aba8b141d12507fad2d87a48cca98e8be433b88`.

La rama `codex/introduccion-dpd-worker-20260920` parte de esa cabeza e incorpora el
overlay `deploy/dpd/`, sus pruebas y este encargo. Lee los commits posteriores y
el estado real: no fuerces un checkout antiguo ni elimines cambios concurrentes.
El PR #22 seguía abierto; no confundas su descripción con resultados actuales.

La V2 completa se entrega como archivo adjunto
`awesome-dpd-worker-2026-09-20.zip`; también puede encontrarse en el adjunto
anterior `smartkea-formacion-v2-2026-09-20.zip`. Los enlaces sandbox de otra
conversación NO son rutas de tu entorno. Comprueba qué archivos están realmente
adjuntos o en el checkout. No supongas que la V2 ya está en GitHub: esta rama
publica el despliegue y el encargo, no sustituye el catálogo existente.

La V2 tiene seis rutas, 24 prácticas/fases, 36 preguntas originales, 35 fuentes,
13 credenciales y 22 documentos prácticos. La versión de PR #22 usa otra
estructura y 26 etapas: compara por función y contenido, no por cantidad.
Preserva las aportaciones útiles de ambas sin duplicar horas ni inventar
acreditaciones. Si la V2 no está disponible, informa de esa dependencia concreta
antes de dar por cumplida la reconciliación; no la sustituyas por una landing.

## 1. Inventario y protección del trabajo

Lee AGENTS.md e instrucciones aplicables. Ejecuta git status, remotes, fetch,
inventario de ramas/PR y comparación de ancestros. Usa worktree o clon separado
si hay cambios locales. No uses reset --hard, force-push, merges con estrategia
ours indiscriminada, squash que pierda la integración, ni borres ramas.

Revisa los logs actuales del PR #22. Reproduce el fallo comunicado de búsqueda
M05: el índice dinámico devolvía módulos que mencionaban M05 como prerrequisito.
Corrige la causa en filterOutline y prueba identificadores exactos, búsqueda
libre, ES/EN, espacios y mayúsculas. No cambies una expectativa válida para hacer
pasar la prueba. Si ya está corregido, conserva y documenta la prueba de regresión.
Valida Fundamentos sin desplegar su Worker.

Escanea los archivos a publicar y el historial que vaya a exponerse para detectar
secretos, datos de alumnos, expedientes, documentos personales y contenido sin
permiso de redistribución. No publiques snapshots privados de infraestructura.
No copies secretos a logs, archivos temporales públicos, issues o frontend.

## 2. Reconciliar el producto, no regenerarlo desde cero

Preserva diseño claro, navegación accesible, buscador, selector de rol, rutas,
prerrequisitos, horas orientativas, prácticas, preguntas explicadas, repaso de
errores, comparador de certificaciones, glosario y documentos.

Perfiles obligatorios: DPD; legal/compliance; negocio/no técnicos;
sistemas/soporte; informática/desarrollo/cloud; ciberseguridad/Blue Team/GRC.
Respeta que las horas de rutas no se suman entre sí ni a las 480 horas de
Fundamentos. La formación es autoestudio propuesto, no acreditación AEPD-DPD.
No copies exámenes reservados ni documentos de pago. Mantén procedencia,
fecha y límites de las fuentes. No inventes equivalencias entre credenciales.

Preserva planificación por fases y semanas, exportación ICS de objetivos de día
completo, Markdown y progreso JSON con validación y confirmación al importar.
El guardado local será opt-in y con claves propias; no añadas cuentas,
telemetría, APIs de IA, bases de datos ni envío de expedientes. No presentes
localStorage como aislamiento entre aplicaciones del mismo dominio.

Conserva lectura útil sin JavaScript. ES/EN deben ser coherentes; indica que los
casos/plantillas extensos aún están en español donde corresponda. Mantén el caso
ficticio Aula Norte y todos los entregables aprovechables. La fuente canónica de
rutas y credenciales será una sola; genera las copias de Fundamentos con hash y
referencia de versión. No mantengas catálogos divergentes editados manualmente.

## 3. GitHub público y organización

Comprueba si existe `smartkea-cyberinnovation/awesome-dpd` y los permisos reales.
Si no existe, créalo público utilizando una sesión autorizada. Si existe, lee su
contenido y abre una rama/PR; no sobrescribas main ni importes un historial ajeno.
Separa el proyecto desde awesome-dpd conservando atribución y trazabilidad
(subtree split en clon desechable o importación con mapa de procedencia). Copia
el overlay deploy/dpd y adapta rutas relativas para el repositorio independiente.

No asignes una licencia nueva a materiales previos o ajenos. La publicación
pública está solicitada, pero cualquier decisión de licencia pendiente debe
quedar identificada. No llames open source al conjunto sin licencia adecuada.
Actualiza README, enlaces, SECURITY, CONTRIBUTING, documentación y referencias.

Integra los PR revisados con comprobaciones aprobadas, sin eludir protecciones.
La transferencia de Fundamentos a la organización debe ser nativa de GitHub,
preservando historial, issues e integraciones y comprobando posibles colisiones.
Si no hay permisos administrativos, deja ese paso separado; no bloquees por ello
el repositorio DPD ni suplantes la transferencia creando un duplicado.

## 4. Worker y montaje por subruta

Utiliza Cloudflare Workers con Static Assets, un Worker exclusivo
`smartkea-introduccion-dpd` y el prefijo `/introduccion-dpd/`. El overlay incluido
es la base, no una excusa para omitir su revisión o el dry-run real.

Compila primero las fuentes existentes: build.py -> dist en V2 o tools/render.py
-> site en el catálogo antiguo. Publica SOLO el sitio reconciliado en
`deploy/dpd/public/introduccion-dpd`. No subas el repo completo ni crees un dist
vacío para ocultar un fallo. Mantén el build hook de Wrangler para que deploy y
versions upload reconstruyan los assets; soluciona cualquier dependencia de cwd.

Configura ASSETS, run_worker_first=true, html_handling=none y
not_found_handling=none. Conserva respuestas 404 reales, HEAD, 405, CSP y MIME.
No uses fallback global a index.html para JS/CSS inexistentes. Conserva queries
en la redirección canónica, pero no las propagues junto con cookies o
Authorization al almacén estático. No añadas un proxy genérico a destinos de URL.

Solo se permiten las rutas `smartkea.com/introduccion-dpd` y
`smartkea.com/introduccion-dpd/*`. NO captures smartkea.com/*, NO pongas un Custom
Domain del Worker sobre el apex y NO uses /introduccion-dpd* porque captura rutas
hermanas. No modifiques DNS/WAF global ni purgues toda la zona.

ATENCIÓN: el matching de rutas Cloudflare incluye la query. La ruta exacta no
captura /introduccion-dpd?probe=1. Revisa el ejemplo de Redirect Rule, instala la
normalización del path exacto preservando query o integra ese caso en el router
existente. No amplíes el comodín para evitar esta revisión. El JSON de ejemplo
está desactivado y Wrangler no lo aplica por sí solo.

La portada smartkea.com redirigía a www al consultar. Inspecciona dónde se hace:
Redirect Rules, Bulk Redirects, Page Rules, Worker u origen. Aplica, si hace falta,
una excepción exclusivamente al path DPD exacto/subárbol en la redirección
anterior; mantén la conducta del resto del dominio. No crees bucles apex/www ni
aceptes silenciosamente www como sustituto de la URL requerida.

Antes de escribir en Cloudflare guarda inventario/snapshot privado de rutas,
IDs de versiones/deployments y reglas afectadas. Verifica cuenta, zona y DNS
proxied existente. Comprueba service workers existentes y servicios de inyección
de scripts del origen que puedan afectar CSP/progreso. No desactives controles
corporativos globales. Usa permisos de scripts/rutas y lectura acotados; edición
de redirects solo cuando sea necesaria. No uses Global API Key.

## 5. Toolchain y CI/CD

Desde deploy/dpd, verifica Node/Python y las versiones disponibles. Instala una
versión estable revisada de Wrangler 4, fíjala EXACTAMENTE y genera un lockfile
real. Revisa npm audit. Añade Playwright con versión exacta si no hay herramienta
compatible existente. No inventes package-lock ni digas npm ci aprobado sin
lockfile. Ejecuta las 39 pruebas incluidas y las pruebas del contenido V2.

Completa CI con unittest, pruebas JS, build, enlaces, sintaxis y dry-run de
Wrangler. Añade aceptación con navegador real. Fija actions por SHA verificado,
contents:read, persist-credentials:false y separación entre jobs de PR sin
secretos y publicación desde la rama aprobada.

Elige UN solo controlador de despliegue, preferentemente GitHub Actions con un
environment de producción y secretos acotados. No dejes a Workers Builds y
Actions compitiendo. Si se reutiliza Workers Builds, confirma raíz, nombre de
Worker y entorno: la configuración de preview no puede desplegar accidentalmente
el Worker de producción. Documenta los comandos efectivos y evita el error
versions upload sin generar antes los assets.

Usa únicamente credenciales ya autorizadas. En Codex cloud los secrets de setup
no están disponibles en la fase del agente: no los persistás ni copies a
.bashrc, ficheros o variables ordinarias para eludir ese límite. Despliega con un
job protegido que reciba sus propios secretos o desde Codex CLI local ya
autorizado. Verifica auth sin imprimir tokens. Si falta acceso, entrega los
nombres de variables/permisos necesarios, no solicites pegar secretos en el chat.

## 6. Pruebas y publicación

Primero ejecuta tests y build; después wrangler deploy --dry-run. Arranca Wrangler
local y navega de verdad a /introduccion-dpd/. No sustituyas la prueba con
page.setContent. Prueba Chromium y WebKit, escritorio/móvil; una emulación de
viewport no es una prueba en iPad físico.

Comprueba ambos idiomas, los seis perfiles, navegación anidada y atrás/adelante,
prácticas, cuestionarios/errores, presentación/teclado, planificación, ICS,
Markdown, JSON válido/inválido y persistencia opt-in tras recargar. Revisa errores
de consola, CSP y solicitudes. Mantén contraste, foco, etiquetas y ausencia de
desbordamientos. Ningún progreso debe enviarse al servidor.

Despliega primero el Worker de preview SIN rutas de smartkea.com. Ejecuta
smoke.mjs y aceptación en su origen real. Revisa las reglas/baselines y luego
promueve el commit revisado a producción usando las credenciales autorizadas.
Conserva IDs de versión/deployment y hash del árbol de assets. Una versión subida
no es una versión activada ni una URL validada.

Comprueba externamente, sin auto-seguir redirecciones en la primera observación:
- /introduccion-dpd -> 308 canónico, y lo mismo con ?probe=1 sin perder query;
- /introduccion-dpd/ y documentos reales -> 200 con tipo correcto;
- /introduccion-dpd/healthz -> identidad y SHA esperados;
- asset inexistente -> 404, nunca HTML 200; HEAD sin cuerpo;
- portada, otras formaciones y /introduccion-dpdx conservan su conducta previa.

Si falla el smoke o aparece regresión, revierte SOLO esta versión y los cambios
DPD registrados. En primera publicación retira únicamente las rutas/reglas
nuevas, sin borrar infra previa. El rollback requiere validar versión anterior y
mapeos; no basta cambiar una etiqueta en GitHub.

## 7. Cierre verificable

Entrega URL real, repo canónico, PR/commits, versión/deployment del Worker,
rutas/reglas cambiadas, fuentes reconciliadas, pruebas con logs y capturas,
configuración de CI y procedimiento de rollback. Distingue hecho, probado y
pendiente. Actualiza los textos antiguos que dicen no publicado solamente cuando
exista evidencia del nuevo estado. Mantén separado el resultado DPD del estado
de transferencia e integración de Fundamentos.

No termines solo con una lista de recomendaciones cuando puedas ejecutar la
tarea. Tampoco inventes un despliegue si hay un bloqueo de permisos o entorno.
