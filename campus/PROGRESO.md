# Progreso local y reanudación por pestaña

Las marcas, notas y favoritos se conservan en localStorage del origen. El punto de continuación de cada pestaña se conserva además en sessionStorage, para que la recarga de la portada no adopte el módulo visitado en otra pestaña. La ruta se valida contra los módulos y prácticas del catálogo antes de restaurarla.

Cerrar una pestaña finaliza esa sesión. Una pestaña nueva puede comenzar con la última ruta de la copia compartida; después mantiene su propio recorrido. Si el navegador bloquea sessionStorage, el campus sigue funcionando con la copia compartida como alternativa, sin garantizar reanudación independiente por pestaña.

La exportación JSON conserva la ruta del recorrido que se exporta. La importación reemplaza la copia actual con confirmación. Las notas no están cifradas; no deben contener datos personales ni secretos. No editar simultáneamente las mismas notas en varias pestañas: esto no es un editor colaborativo.

Las pruebas de navegador incluyen la secuencia de regresión: pestaña A en M05, vuelta a portada, pestaña B en M06, recarga de A y continuación en M05. Esto comprueba el punto de continuación, no una sincronización entre dispositivos.
