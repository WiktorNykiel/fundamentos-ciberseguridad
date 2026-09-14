# Desplegar en Cloudflare Pages

## Integración Git: mantener el curso actualizado

En Workers & Pages, crear una aplicación de Pages e importar el repositorio `WiktorNykiel/fundamentos-ciberseguridad`. Autorizar únicamente el repositorio necesario.

| Configuración | Valor |
|---|---|
| Rama de producción | `main` |
| Directorio raíz | `campus` |
| Framework | Ninguno |
| Comando de compilación | `python3 build.py` |
| Directorio de salida | `dist` |

El checkout también contiene `../formacion/sistemas-operativos/`, que es la fuente. No seleccionar el preset Next.js ni publicar la raíz completa. Utilizar Python 3.11 o posterior en el entorno de compilación; las comprobaciones del workflow utilizan Python 3.13.

Después del primer despliegue, abrir la URL que Cloudflare devuelva. No se presupone ningún subdominio. Comprobar inicio, búsqueda, enlace profundo, presentación, guardado/recarga, móvil, lectura continua y descarga del kit. Verificar que `_headers` se ha aplicado.

La integración puede reconstruir los cambios posteriores de las ramas configuradas. Un push no demuestra que la cuenta del titular ya tenga esa integración activada.

## ZIP precompilado: Direct Upload

`python3 campus/build.py` genera `campus/pages-ready.zip`, con `index.html` en su raíz. En un proyecto Direct Upload, subir ese ZIP desde el panel y publicar. Subir el ZIP del sitio, no un ZIP de todo el repositorio o de los informes de pruebas.

La documentación de Cloudflare distingue los formatos: el panel admite ZIP o carpeta; Wrangler recibe una carpeta de activos, no el ZIP. Un proyecto Direct Upload no se convierte después en uno con integración Git: elegir el método antes de crearlo. Si se necesita actualización continua desde este repositorio, utilizar integración Git desde el principio.

## Wrangler opcional

Con Wrangler instalado y autorizado en el equipo del titular, desde la raíz y tras el build:

```sh
wrangler pages deploy campus/dist --project-name fundamentos-ciberseguridad --branch main
```

El nombre es una propuesta de parámetro, no prueba de que el proyecto exista. No añadir tokens al código, frontend, argumentos guardados o material del alumno. Reutilizar la configuración existente de la cuenta cuando corresponda.

## Seguridad y datos

`_headers` restringe scripts y conexiones al propio origen; no contiene `unsafe-inline` ni `unsafe-eval`. Añade bloqueo de marcos, `nosniff`, política de referencia y restricciones de cámara, micrófono y geolocalización. Estas reglas de Pages se aplican a activos estáticos. No hay Functions; si se incorporan después, necesitan sus propias cabeceras.

La navegación con `#/...` no necesita una regla global que convierta cualquier error en HTML. No hay service worker ni caché offline persistente. El progreso es local y depende del origen: exportarlo antes de pasar de preview a producción, cambiar dominio o borrar datos.

Esta versión no necesita base de datos, backend, cuenta de alumno ni API de IA. Si se incorporan cuentas, inferencia o ejecución gestionada, diseñar servicios separados con permisos, privacidad y pruebas propias. No incrustar credenciales en el cliente ni exponer el servidor local de previsualización.

## Fuentes primarias

- [Pages: sitios HTML estáticos](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/).
- [Integración Git](https://developers.cloudflare.com/pages/get-started/git-integration/).
- [Direct Upload y formatos permitidos](https://developers.cloudflare.com/pages/get-started/direct-upload/).
- [Cabeceras de activos estáticos](https://developers.cloudflare.com/pages/configuration/headers/).

Consulta documental: 14 de septiembre de 2026. No equivale a despliegue en la cuenta Cloudflare del titular. El último build y sus evidencias se consultan en GitHub Actions.
