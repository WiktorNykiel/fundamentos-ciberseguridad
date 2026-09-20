# Workers: compilación antes de subir / Build before upload

Revisión: 2026-09-20. Este documento trata Workers Builds, no Pages.

## Diagnóstico basado en el log recibido

El 20-09-2026 a las 09:47 UTC, `npx wrangler versions upload` con Wrangler 4.135.0 falló porque `assets.directory` apuntaba a `campus/dist`, que no existía. En el log no aparece la compilación del campus antes de la subida. npm instaló paquetes; eso no genera los activos de este campus Python. El aviso de scripts de instalación no es el error que detuvo este intento.

No es el error de binding `frontend` del 16 de septiembre. Tampoco demuestra un problema de permisos de la cuenta. No se guardan aquí el log privado, identificadores de cuenta o credenciales.

## Corrección en el repositorio

`wrangler.jsonc` ejecuta ahora `python3 campus/cloudflare.py build` como custom build antes de procesar los activos. El comando compila y valida, pero nunca invoca Wrangler. Por eso una llamada directa a `wrangler versions upload` ya no depende de una carpeta dist generada en una sesión anterior. No añadir dist al control de versiones ni crear un directorio vacío para silenciar el error.

La configuración rechaza hooks diferentes, otras rutas de activos y bindings ajenos. Se conservan la aplicación de referencia, el nombre del Worker y la fecha de compatibilidad. Las pruebas CI reproducen el checkout sin dist con las versiones 4.132.0 y 4.135.0; su resultado se consulta en Actions, no se deduce de la existencia de este documento.

## Configuración del panel tras integrar esta revisión

| Campo en Workers > Settings > Builds | Valor |
|---|---|
| Root directory | Raíz del repositorio, no `campus` |
| Build command | Vacío: el custom build de Wrangler compila y valida |
| Production branch | `main` |
| Deploy command | `npx --yes wrangler@4.135.0 deploy --config wrangler.jsonc` |
| Non-production branch deploy command | `npx --yes wrangler@4.135.0 versions upload --config wrangler.jsonc` |
| Build variable | `SKIP_DEPENDENCY_INSTALL=1` |
| Build variable | `PYTHON_VERSION=3.13` |

Un `versions upload` correcto crea una versión: **no la promueve automáticamente a producción**. Para publicar producción se utiliza `deploy`, o se promociona una versión revisada. Estos comandos tienen efectos externos; los tests solo usan `--dry-run` y no necesitan secretos Cloudflare.

Las variables del panel y los comandos de Builds no cambian por hacer merge de un archivo. Hay que comprobarlos en el Worker existente. Mantener tokens fuera de Git. La omisión de instalación afecta solo al campus estático, no es una recomendación para la aplicación Next.js.

## Pruebas sin publicación

Desde la raíz de una copia del repo con estos cambios:

```sh
python3 campus/cloudflare.py plan
npx --yes wrangler@4.135.0 versions upload --dry-run --config wrangler.jsonc
python3 campus/check_release.py
```

El log debe mostrar custom build, generación del campus, validación de release y finalización del dry-run. Después de publicar, comprobar idioma, índice, scripts, 404 y `build-info.json` en la URL real. Una subida correcta no demuestra que el navegador reciba la versión esperada.

## English operational summary

The attached September 20 log fails because `campus/dist` does not exist before `wrangler versions upload`. Installing the root npm dependencies does not build this Python-generated static campus. The repository now owns the build step through Wrangler's `build.command`; it calls the build-only wrapper and cannot recurse into Wrangler. Keep the repository root as the Workers Builds root, leave the dashboard build command empty, use `deploy` for production and `versions upload` for previews, and set the build variables shown above. A preview upload is not a production promotion. The GitHub workflow checks both raw commands from a missing-assets checkout using dry-run only; it never deploys or changes account permissions.

## Fuentes primarias / Primary sources

- [Custom builds](https://developers.cloudflare.com/workers/wrangler/custom-builds/): comando previo y `WRANGLER_COMMAND` para versions upload.
- [Workers Builds configuration](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/): build, deploy y preview son pasos distintos.
- [Build image](https://developers.cloudflare.com/workers/ci-cd/builds/build-image/): Python y SKIP_DEPENDENCY_INSTALL.
- [Versions and deployments](https://developers.cloudflare.com/workers/versions-and-deployments/): crear versión no equivale a dirigir tráfico.
