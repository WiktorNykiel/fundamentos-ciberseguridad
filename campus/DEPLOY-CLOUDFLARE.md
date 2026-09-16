# Probar el campus en Cloudflare Pages

## Qué publicar

Publicar únicamente `campus/dist/` o su ZIP `campus/pages-ready.zip`. No subir el repositorio entero, `node_modules`, diagnósticos ni una carpeta docente privada. El sitio es estático: la web orienta las prácticas, no ejecuta comandos ni necesita credenciales de los alumnos.

## Opción A · Integración Git para actualizaciones continuas

En Cloudflare, abrir **Workers & Pages**, crear una aplicación **Pages** y conectar el repositorio `WiktorNykiel/fundamentos-ciberseguridad`. Los nombres del panel pueden variar; seleccionar Pages e integración Git, no un proyecto Workers ni el preset Next.js.

| Campo | Valor |
|---|---|
| Rama de producción | `main` |
| Directorio raíz | `campus` |
| Framework | Ninguno |
| Comando de build | `python3 build.py && python3 check_release.py` |
| Directorio de salida | `dist` |
| Variable de build | `SKIP_DEPENDENCY_INSTALL=1` |
| Python de build | `PYTHON_VERSION=3.13` o una versión compatible 3.11+ admitida por la imagen |

La variable evita instalar dependencias Node: el campus no las necesita. El compilador accede a `../formacion/sistemas-operativos/` dentro del mismo checkout. No añadir tokens al repositorio ni al código del navegador.

Guardar y desplegar. Utilizar la URL exacta que muestre Cloudflare. Abrir `build-info.json` en ese origen y contrastar `sourceCommit` con el commit desplegado. Un build fallido no equivale a una publicación actualizada.

## Opción B · Direct Upload para una prueba manual

1. Obtener el ZIP validado de la entrega o generarlo con los comandos siguientes.
2. En el panel crear un proyecto Pages de Direct Upload y subir **`pages-ready.zip`**.
3. Antes de publicar, comprobar que `index.html`, `_headers` y `course.json` están en la raíz del ZIP, no dentro de otra carpeta.
4. Abrir la URL devuelta por Cloudflare y completar la comprobación funcional de esta guía.

```sh
python3 campus/build.py
python3 campus/check_release.py
```

El panel admite ZIP. Con Wrangler se pasa una carpeta de activos, no ese ZIP. Direct Upload e integración Git son modos de proyecto diferentes; un proyecto Direct Upload no puede convertirse después a integración Git. Elegir A para trabajar habitualmente desde GitHub. El validador aplica un máximo conservador de 1000 activos y menos de 25 MiB por archivo para la subida mediante panel.

## Comprobación funcional después de publicar

| Acción | Resultado esperado |
|---|---|
| Abrir portada y «Empieza por aquí» | Se distinguen web, laboratorio y progreso local |
| Abrir `#/temario` | 32 módulos en siete bloques; accesos a teoría, prácticas y revisión |
| Buscar «permisos linux» | Coincidencias por ambas palabras; incluye biblioteca cuando procede |
| Abrir M05 y su pestaña Prácticas | Tres fichas; acceso al asistente L05A |
| Completar una fase y recargar | La marca se conserva en el mismo origen/navegador |
| Abrir presentación, usar flechas y Escape | Se avanza y vuelve a la lectura sin ocultar texto largo |
| Exportar e importar progreso | La copia válida se restaura; una copia incompatible se rechaza |
| Abrir móvil e índice | Tablas con desplazamiento local, sin desbordamiento global |
| Abrir `lectura.html` | Curso legible sin JavaScript |
| Revisar cabeceras de `index.html` | CSP, nosniff, protección de marcos y política de referencia |

Las marcas no verifican el sistema del alumno ni miden 480 horas de uso. El alojamiento puede conservar sus propios logs; la aplicación no añade analítica propia.

## Diagnóstico y reversión

**Se instala Next.js:** revisar raíz `campus`, framework ninguno y variable `SKIP_DEPENDENCY_INSTALL` en producción y previsualización. **Archivo curricular no encontrado:** debe utilizarse un checkout completo, no solo la carpeta campus. **Pantalla vacía:** comprobar `course.json`, consola y MIME; no abrir con `file://`. **El progreso parece perdido:** verificar origen exacto, navegador y modo privado; importar una copia exportada antes del cambio. **No aparece la última versión:** revisar commit y build-info, despliegue activo y caché; no borrar las notas para actualizar la web.

Para revertir, seleccionar un despliegue anterior conocido en Cloudflare o volver a publicar un ZIP validado conservado. Mantener las copias de progreso fuera del sitio antes de cambiar de dominio. No publicar una terminal abierta para ampliar este asistente.

## Referencias oficiales

- [Configuración de build](https://developers.cloudflare.com/pages/configuration/build-configuration/).
- [Imagen de build y variables](https://developers.cloudflare.com/pages/configuration/build-image/).
- [Integración Git](https://developers.cloudflare.com/pages/get-started/git-integration/).
- [Direct Upload y límites](https://developers.cloudflare.com/pages/get-started/direct-upload/).

Revisión documental: 2026-09-16. Este documento prepara la publicación; no acredita que se haya creado un proyecto, dominio o despliegue en una cuenta Cloudflare.
