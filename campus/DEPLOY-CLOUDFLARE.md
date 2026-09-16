# Cloudflare: publicar el campus correcto

**Campus 2.2 · 16 de septiembre de 2026.** Hay dos productos válidos: **Workers Static Assets** y **Pages**. Ambos publican `campus/dist/`, no la aplicación Next.js de la raíz. Selecciona una ruta y no mezcles sus comandos. Esta guía no acredita un despliegue en ninguna cuenta.

## A. Corregir el Worker de los logs recibidos

Los registros del 16 de septiembre muestran comandos de **Workers Builds**, no una compilación de Pages. A las 11:03 UTC se ejecutó `npx wrangler deploy` en la raíz, se autodetectó Next.js y se introdujo OpenNext. El fallo final fue un binding `WORKER_SELF_REFERENCE` hacia `frontend`, que no existía. A las 11:28 UTC se ejecutó `npx wrangler versions upload` sin definir un script o directorio de activos. Estos son dos errores distintos; los avisos anteriores de npm no son el fallo final observado.

Los logs originales no se copian al repositorio: contienen identificadores de cuenta y rutas del proveedor. La configuración nueva `wrangler.jsonc` declara únicamente nombre, fecha de compatibilidad y activos estáticos. No necesita `WORKER_SELF_REFERENCE`, R2, Images, OpenNext ni `nodejs_compat`.

### Ajustes del Worker existente

En **Workers & Pages → fundamentos-ciberseguridad → Settings → Build**, configura:

| Campo | Valor |
|---|---|
| Repositorio | `WiktorNykiel/fundamentos-ciberseguridad` |
| Rama de producción | `main` |
| Root directory | Raíz del repositorio: vacío o `/`, no `campus` |
| Build command | Vacío: el comando siguiente compila y valida |
| Deploy command | `python3 campus/cloudflare.py deploy` |
| Non-production branch deploy command | `python3 campus/cloudflare.py preview` |
| Build variable | `SKIP_DEPENDENCY_INSTALL=1` |
| Build variable | `PYTHON_VERSION=3.13` |

Guarda los ajustes y lanza un build del **último commit de main**, no una repetición del checkout antiguo. La opción exacta del panel puede variar. Si el panel ya conserva un build command Next.js/OpenNext, bórralo: se ejecutaría antes del wrapper. No cambies tokens ni crees un servicio ficticio llamado `frontend`.

`cloudflare.py` resuelve sus rutas desde el propio archivo, compila, valida y solo entonces llama a **Wrangler 4.132.0** con `--config` explícito. Su modo `preview` utiliza `versions upload`: sube una versión de prueba, no promueve producción. `deploy` sí cambia producción. Una carga correcta de versión y un despliegue activo no son lo mismo.

Esta preparación del repositorio **no modifica automáticamente los ajustes del panel**. Workers Builds documenta que no toma su fase de build de la sección Custom Builds del archivo Wrangler; por eso la preparación se incluye en el propio comando de despliegue. La instalación automática se omite para no instalar la aplicación de referencia.

### Prueba local sin publicar

```sh
python3 campus/cloudflare.py plan
python3 campus/cloudflare.py build
python3 campus/cloudflare.py dry-run
```

Los dos primeros comandos no necesitan red ni credenciales. `dry-run` puede descargar Wrangler mediante npm, pero no sube activos ni versiones. Se utiliza una versión fijada, no `latest`. Node.js/npm solo se requieren para Wrangler; no son dependencias del campus publicado. La instalación de la CLI no se confunde con instalar el package.json Next.js de la raíz.

Para inspeccionar respuestas del runtime local:

```sh
npx --yes wrangler@4.132.0 dev --config wrangler.jsonc --local --ip 127.0.0.1 --port 8789
```

No se configura una ruta pública, un dominio ni un binding remoto durante esta prueba. No uses `--remote`. El servidor Python `python3 campus/serve.py --port 8788` sigue disponible para la vista previa ordinaria.

## B. Cloudflare Pages conectado a GitHub

Crea un proyecto de tipo **Pages** con integración Git. No reutilices los campos de comandos de versiones de Workers.

| Campo | Valor |
|---|---|
| Repositorio / rama | `WiktorNykiel/fundamentos-ciberseguridad` / `main` |
| Directorio raíz | `campus` |
| Framework preset | Ninguno |
| Build command | `python3 build.py && python3 check_release.py` |
| Build output directory | `dist` |
| Variable | `SKIP_DEPENDENCY_INSTALL=1` |
| Variable | `PYTHON_VERSION=3.13` |

Pages no usa el wrapper `deploy` ni `versions upload`. La raíz Wrangler del repositorio es para **Workers**; el proyecto Pages se configura con su raíz propia `campus` y no debe apuntar a la raíz Next.js. El campus no necesita un archivo Wrangler de Pages para esta integración.

## C. Pages mediante Direct Upload

Para una prueba manual sin conectar Git, compila y valida, o descarga el artefacto `cloudflare-pages-ready` de una ejecución correcta de Actions. Extrae el contenedor del artefacto GitHub y sube **el ZIP interior `pages-ready.zip`**, que contiene `index.html` en su raíz. No subas un ZIP de fuentes ni un ZIP que solo contiene otro ZIP.

El panel de Pages admite ZIP. La CLI de Pages recibe una carpeta. La elección inicial importa: un proyecto Direct Upload no se convierte después en integración Git; crea uno Git desde el principio si necesitas actualizaciones automáticas.

## Aceptación después de publicar

Usa exclusivamente la URL que devuelva Cloudflare. Comprueba `/build-info.json`: el commit debe coincidir con el checkout desplegado; los recuentos esperados son **32 módulos, 96 fichas, 21 recursos y 480 horas**. Abre `#/temario`, filtra Linux y confirma ocho módulos; filtra macOS y confirma cuatro. Prueba una búsqueda, M05, L05A, autoevaluación, presentación y recarga con progreso.

Comprueba `course.json` como JSON, los scripts con su tipo correcto y una ruta inexistente con HTTP 404. Las rutas del curso son fragmentos `#/...`: no necesitan redirigir todos los archivos inexistentes a HTML. Revisa CSP, `nosniff` y ausencia de claves o llamadas a modelos. El asistente sigue siendo manual.

Exporta el progreso antes de cambiar de origen. Las marcas son locales, autodeclaradas y no cifradas. Una pantalla de compilación verde no acredita el funcionamiento de la URL final.

## Recuperación y diagnóstico

Si aparece `Next.js`, `.next`, `.open-next`, `opennextjs-cloudflare` o `WORKER_SELF_REFERENCE`, revisa la raíz y los comandos: no corresponde al campus. Si faltan activos, comprueba que no se omitió la compilación o que no se reintentó un commit anterior. Si faltan Python o npx, comprueba la versión de la imagen de build antes de instalar nada con privilegios.

No borres recursos creados por intentos anteriores sin inventario: el primer log muestra actividad sobre un bucket de caché, pero no demuestra su estado actual ni autoriza una limpieza ciega. Para volver atrás utiliza una versión previamente aceptada del producto elegido; luego verifica la URL y el contenido. Guarda logs minimizados fuera del repositorio público.

## Fuentes oficiales consultadas

- [Workers Builds: configuración, comandos y autodetección](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/).
- [Workers: imagen de build y SKIP_DEPENDENCY_INSTALL](https://developers.cloudflare.com/workers/ci-cd/builds/build-image/).
- [Workers Static Assets: configuración sin backend](https://developers.cloudflare.com/workers/static-assets/binding/).
- [Cabeceras de activos](https://developers.cloudflare.com/workers/static-assets/headers/).
- [Pages: configuración de build](https://developers.cloudflare.com/pages/configuration/build-configuration/).
- [Pages: Direct Upload](https://developers.cloudflare.com/pages/get-started/direct-upload/).

La revisión de documentación y las pruebas locales/CI se registran por separado de un despliegue real. Esta guía no inventa una URL ni una confirmación del proveedor.
