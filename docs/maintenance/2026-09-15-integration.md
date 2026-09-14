# Integración de dependencias y correcciones del campus · 2026-09-15

## Alcance de los PR

Se consolidan #1 (minimatch), #4 (flatted), #5 (picomatch), #6 (brace-expansion), #10 (js-yaml), #11 (@humanfs/node), #12 (nanoid), #13 (baseline-browser-mapping), #14 (browserslist), #15 (Next/sharp) y #16 (Next). La integración conserva sus commits como ancestros, no reemplaza el trabajo por una actualización sin procedencia.

Los cambios comunes se deduplican. El PR #15 incluye Next 16.3.5, que sustituye al 16.3.3 propuesto por #16; no se degrada la versión. Se alinea eslint-config-next con Next y se mantiene React/React DOM en la línea 19.2, parche 19.2.8. Los cambios de dependencias pertenecen a la aplicación de referencia de la raíz: el campus estático sigue sin dependencias npm de producción.

## Correcciones del campus

- Un evento `storage` recibido no vuelve a escribirse a `localStorage`: evita el intercambio repetitivo entre pestañas y que cambie la ruta recordada al renderizar una actualización ajena.
- Una práctica con todas las fases confirmadas se reabre en el cierre. Las incompletas se reanudan en su primera fase pendiente.
- La importación usa un límite de 1 MiB en bytes UTF-8, coherente con el archivo seleccionado, y permite recuperar las notas Unicode máximas admitidas por módulo.
- Se conserva el esquema y la clave de progreso v1. No se borran ni migran de forma destructiva las marcas existentes.

## Pruebas y operación

Las regresiones anteriores tienen pruebas de estado y de navegador. El workflow del campus también se ejecuta ante cambios del manifiesto o lockfile raíz. Un workflow separado valida la aplicación heredada mediante instalación reproducible sin scripts de ciclo de vida, lint, tipos, pruebas de dependencias, build y auditoría de dependencias de producción.

Se eliminan las descargas de fuentes de Google durante el build de la aplicación de referencia, usando tipografías de sistema y configuración visual clara. No se cambian permisos, reglas de ramas, requisitos de revisión ni despliegues Cloudflare.

La existencia de estas pruebas no acredita una ejecución: el resultado y SHA exactos se consultan en el PR de integración y en sus ejecuciones de Actions. La aceptación web no sustituye las pruebas de los 96 laboratorios nativos ni la ejecución Windows/macOS.
