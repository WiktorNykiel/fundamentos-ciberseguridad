# Verificación del campus 2.0

## Ejecución verificada

El [run 34900257743](https://github.com/WiktorNykiel/fundamentos-ciberseguridad/actions/runs/34900257743) del commit `434ed4deadd007de4c19d98db6fefe8d8ea60fae` terminó correctamente. Sus artefactos se descargaron, se comprobó el SHA-256 del archivo recibido y se revisaron los logs y capturas.

| Conjunto | Resultado observado |
|---|---|
| Compilador Python | 22 pruebas correctas |
| Estado y progreso JavaScript | 17 pruebas correctas, ninguna omitida |
| Navegador Chromium con el curso real | 20 pruebas correctas |
| Compilación real | 32 módulos, 96 prácticas, 18 recursos, 170 secciones de presentación y 8 guías ampliadas |
| Regresión del kit y de la planificación existentes | Ambos pasos de CI correctos |

Las 59 pruebas del campus son distintas de las del kit de administración. No se suman como una medida única de cobertura de la formación. Las horas siguen siendo 480 planificadas, no horas impartidas o medidas por el navegador.

## Qué cubre el navegador

Portada, navegación y recarga de lectura; notas tratadas como texto; autoevaluación; cinco fases y finalización de práctica; búsqueda; presentación con flechas y Escape; exportación, importación y reinicio; ruta inválida; enlace de salto accesible; cabeceras CSP; enlaces con texto; navegación interna a referencias; reanudación; lectura continua sin JavaScript; y contraste manual de cantidades de R01.

Se comprobaron escritorio y una ventana móvil de 390 × 844. La prueba móvil no detectó desbordamiento horizontal de la página. Las pruebas rechazaban solicitudes de red fuera del servidor local y errores JavaScript. Se inspeccionaron las capturas de inicio y presentación; los títulos duplicados de presentación se corrigieron antes de esta ejecución.

## Correcciones encontradas durante la aceptación

La primera ejecución de navegador encontró un selector de prueba ambiguo en la biblioteca, porque seleccionaba también el contenedor oculto de presentación. Se acotó al artículo de la vista principal. Se añadieron pruebas de referencias internas, reanudación, lectura continua y comprobación de R01. La segunda ejecución pasó las veinte pruebas.

## Trazabilidad de cambios posteriores

Este informe registra una ejecución concreta; no cambia retroactivamente su commit ni su hash. La corrección editorial de la antigua referencia a distribución privada se incorpora después de ese run y el workflow vuelve a compilar y verificar el curso. Para desplegar, comprobar el run del commit que se vaya a usar y su artefacto correspondiente en Actions.

## Límites

No se han ejecutado las 96 prácticas nativas, scripts Windows/macOS en sus plataformas, clústeres Docker/Compose/Swarm, modelos de IA ni una cohorte docente. El asistente no ejecuta comandos. El seguimiento es local y autodeclarado, no evaluación supervisada. Las pruebas web no son una auditoría exhaustiva de seguridad o accesibilidad ni acreditan un despliegue en Cloudflare.

El repositorio conserva la aplicación previa de la raíz. Estas pruebas validan el campus estático y sus fuentes, no esa aplicación. La carpeta del campus no requiere construirla.
