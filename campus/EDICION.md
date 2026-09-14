# Edición y evolución del campus

## Dónde cambiar cada contenido

| Elemento | Fuente |
|---|---|
| Títulos, orden y prerrequisitos | `formacion/sistemas-operativos/planificacion/curriculo.json` |
| Unidades, herramientas y fichas de práctica | `formacion/sistemas-operativos/modulos/*.md` y `CAPSTONE.md` |
| Apuntes explicativos y autoevaluación | `campus/content.py` |
| Guías detalladas existentes | `formacion/sistemas-operativos/practicas/R*.md` |
| Biblioteca | Lista `PUBLIC_DOCS` de `build.py` y lecciones numeradas |
| Vista, presentación y asistente | `campus/assets/app.js` |
| Progreso y validación de importaciones | `campus/assets/state.js` |
| Diseño claro, responsive e impresión | `campus/assets/styles.css` |

Editar fuentes, no `dist/course.json` ni el HTML generado. El build valida la estructura y reconstruye lectura, diapositivas, búsqueda y fichas. La aplicación Next.js de la raíz no es una dependencia del campus.

## Patrón docente

Cada módulo necesita una pregunta de entrada, un modelo mental, una tarea, un resultado verificable, un caso negativo y una explicación de límites. Usar la GUI para localizar el objeto y la CLI para reproducir o contrastar la acción. No introducir comandos sin contexto de plataforma, versión, privilegio y efecto.

Una práctica debe identificar entorno, tareas, evidencia, criterio de éxito y recuperación. Mantener IDs estables: `M01` a `M32` y `L01A` a `L32C`. El cambio de una ficha no añade horas automáticamente. Si cambia el número de módulos o las reglas de dominio, hay que actualizar catálogo, compilador, interfaz, tests y esquema de progreso de forma coordinada.

Las guías ampliadas son profundizaciones de fichas existentes. No decir que las 96 prácticas están ejecutadas porque existan 96 asistentes. Diferenciar diseño, explicación, prueba del código y validación nativa de un sistema.

## Revisar una contribución

Revisar diff, procedencia de referencias, datos sensibles, navegación y consecuencias de las acciones propuestas. Ejecutar unitarias, build real y pruebas de navegador. Comprobar portada, un módulo de cada plataforma, presentación, asistente, teclado y móvil. Los logs de CI deben corresponder al commit revisado.

Las autoevaluaciones son ejercicios formativos abiertos. Mantener fuera del repositorio público exámenes reservados, expedientes, respuestas individuales y cualquier información de alumnos. La exclusión de un documento del build no borra versiones públicas anteriores de Git.

## Ampliaciones previstas, no implementadas

Sincronización autenticada entre dispositivos; panel docente; evaluación supervisada; backend de IA; ejecución de laboratorios en entornos aislados; telemetría autorizada de resultados; y evaluación nativa de scripts Windows/macOS. Cada ampliación necesita diseño de acceso, retención, límites, coste y pruebas; no es una función disponible por aparecer en esta lista.

## Criterio de release

Un release del campus incluye commit de origen, informe de build, pruebas de aceptación, capturas revisadas y manifiesto SHA-256 del sitio. El despliegue real exige además URL de proveedor y verificación de esa URL. Una versión del campus no es una certificación de la formación ni una prueba de haber impartido sus horas.
