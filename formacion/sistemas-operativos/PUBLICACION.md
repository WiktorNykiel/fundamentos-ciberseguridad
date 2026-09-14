# Publicación y distribución

**Wiktor Nykiel · 14 de septiembre de 2026.**

El repositorio se denomina **WiktorNykiel/fundamentos-ciberseguridad** y se ha comprobado como **público**. Sustituye al nombre anterior del proyecto. La antigua indicación de visibilidad pendiente ya no describe este repositorio.

## Código público y web desplegada son estados diferentes

El curso fuente está en [este índice](README.md). El [campus 2.0](../../campus/README.md) compila lectura, presentación y prácticas guiadas desde ese contenido. El build genera `campus/dist/` y `campus/pages-ready.zip`; las [instrucciones de Pages](../../campus/DEPLOY-CLOUDFLARE.md) permiten publicarlo mediante Git o Direct Upload.

No se registra aquí un dominio inventado ni se afirma un despliegue en Cloudflare por haber escrito código. Una publicación real se confirma con la URL devuelta por el proveedor y pruebas sobre esa URL. Los artefactos temporales de Actions no son un alojamiento web permanente.

## Material anterior de alumnos

El paquete `sistemas-operativos-alumnos-v1.1.zip` y la planificación para alumnos se guardaron separadamente en Drive. Estos enlaces conservan los permisos que tenga la cuenta; **no se presentan como acceso anónimo confirmado**:

- [Paquete de ampliación para alumnos](https://drive.google.com/file/d/13lZEJoPx4jpL5eNg_EtX05-jb5xJWfKp/view?usp=drivesdk).
- [Planificación XLSX para alumnos](https://docs.google.com/spreadsheets/d/1_rHZ5Qncr9iFOo1a0wQTBSYIgPFAsjRv/edit).

La ampliación usa `labkit.py`; el kit del repositorio y del campus usa `oslab.py`. Son conjuntos diferentes. No intercambiar respuestas, datos o informes de pruebas. El campus actual integra las guías del repositorio, no presenta la ampliación externa como si se hubiera incorporado automáticamente.

## Material reservado

El original docente con soluciones, los expedientes, los resultados individuales y las comunicaciones privadas deben permanecer fuera del repositorio y del sitio públicos. El build selecciona expresamente las fuentes del alumno y excluye el banco docente de la biblioteca. Una carpeta, una rama o no enlazar un archivo no constituyen control de acceso sobre material público de Git.

No se incluyen credenciales ni claves de API en la web. El progreso es local y autodeclarado; sus copias contienen notas sin cifrar y deben revisarse antes de compartirlas.

## Integridad, pruebas y mantenimiento

`build-info.json` registra la estructura compilada y el hash del catálogo; `SHA256SUMS.txt` identifica los activos del sitio. Consultar los logs y capturas del workflow correspondiente al commit que se va a desplegar.

Las pruebas de interfaz no acreditan ejecución nativa de los laboratorios ni certificación profesional. Antes de cada cohorte se fijan versiones y se prueban las actividades correspondientes. La visibilidad pública no concede automáticamente una nueva licencia libre.
