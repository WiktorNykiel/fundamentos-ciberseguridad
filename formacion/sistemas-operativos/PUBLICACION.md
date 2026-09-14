# Publicación y distribución del curso

**Responsable: Wiktor Nykiel · 14 de septiembre de 2026.**

El titular ha solicitado actualizar y hacer público el curso. Esta instrucción sustituye la preferencia inicial de mantenerlo privado, pero no convierte por sí sola un repositorio o un archivo de Drive en accesible sin autenticación.

## Estado operativo

La conexión utilizada permite escribir archivos y fusionar propuestas de cambio en GitHub. No ofrece una operación para crear un repositorio ni cambiar su visibilidad. La conexión de Drive permite guardar archivos; su acción de compartición disponible no permite conceder acceso anónimo a cualquiera.

Por tanto, **los enlaces siguientes no se presentan como públicos**. El estado de acceso debe comprobarse en los metadatos del proveedor y mediante una prueba sin sesión después de que se efectúe el cambio administrativo. Una fusión, un nombre de archivo o una etiqueta no acreditan publicación pública.

## Material preparado para alumnos

| Material | Ubicación | Alcance |
|---|---|---|
| Temario y kit del repositorio | [Índice del curso](README.md) | 32 módulos, 480 horas, desarrollo curricular y kit ejecutable existente. |
| Paquete de ampliación para alumnos | [Descargar desde Drive](https://drive.google.com/file/d/13lZEJoPx4jpL5eNg_EtX05-jb5xJWfKp/view?usp=drivesdk) | Mapa curricular, 16 guías ampliadas, scripts, datos sintéticos, web de laboratorio, pruebas y planificación. |
| Planificación XLSX para alumnos | [Abrir en Drive](https://docs.google.com/spreadsheets/d/1_rHZ5Qncr9iFOo1a0wQTBSYIgPFAsjRv/edit?usp=drivesdk&ouid=116648030670437270818&rtpof=true&sd=true) | Nueve hojas; 240 sesiones, 96 laboratorios y 64 preguntas sin respuestas docentes. |

El paquete ampliado conserva su motor `labkit.py` y sus propios ejemplos; el kit del repositorio utiliza `oslab.py`. Son conjuntos diferentes. No intercambiar sus datasets ni atribuir las pruebas de uno al otro. El paquete ampliado está almacenado en Drive; su contenido no se ha descomprimido como una segunda copia del código dentro de este repositorio.

### Integridad del ZIP para alumnos

Archivo: `sistemas-operativos-alumnos-v1.1.zip`.

SHA-256:

```text
16aa0ba1e4c7c207a79726e153f51d6eea785e6908e007bb40493135564dfb8d
```

Contiene 61 archivos, incluido un manifiesto de integridad de los contenidos. No es una copia de todo el repositorio ni de su historial. El original docente, con respuestas y casos resueltos, se conserva separadamente y no se enlaza desde esta página.

## Revisión aplicada al paquete para alumnos

Se ha retirado el directorio de soluciones docentes. Las 64 preguntas se mantienen sin `answer_criteria`; la columna de corrección del XLSX se ha vaciado y convertido en espacio de respuesta para el alumno. No se incorpora el parche original, porque contenía también material docente. Se han excluido cachés de Python y verificado las referencias institucionales y personales conocidas.

La suite del paquete para alumnos se ha vuelto a ejecutar en Linux: **75 pruebas correctas, cero fallos, cero errores y cero omitidas**. Verifica Python, integración Bash, HTTP exclusivamente en loopback y coherencia curricular. No demuestra administración nativa Windows/macOS, despliegue Docker/Compose/Swarm, ejecución de modelos de IA ni impartición de una cohorte.

## Carga de la formación

Los cuatro bloques de fundamentos, Linux, Windows y macOS suman **322 horas**. Los bloques transversales, IA y proyecto añaden **158**. Total: **480 horas**, de las cuales **168 son teoría y 312 práctica**. Las guías ampliadas no se suman como nuevos laboratorios a los 96 existentes.

## Paso administrativo pendiente

Para cambiar la visibilidad del repositorio existente, su titular debe utilizar `Settings → Danger Zone → Change repository visibility → Public` y confirmar los efectos. La documentación oficial explica que el código y los registros históricos de Actions pasan a ser visibles: [GitHub: visibilidad de repositorios](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility).

Antes de ese cambio, revisar **todo** el repositorio, ramas, historial, comentarios y artefactos: la revisión del paquete para alumnos no constituye una auditoría de ese conjunto. Si debe mantenerse privada la aplicación u otro historial, publicar una copia limpia del directorio del curso en un repositorio público independiente, sin historial ajeno al curso.

En Drive, el permiso requerido para difusión es lector para cualquiera con el enlace; no equivale al acceso limitado al dominio de la empresa. No conceder edición anónima ni hacer pública la carpeta docente.

## Licencia y mantenimiento

Visibilidad pública no implica automáticamente una licencia de software libre. No se asigna una licencia nueva sin decisión del titular. Las licencias de las fuentes y herramientas permanecen vigentes. Antes de una cohorte se deben fijar versiones, validar cada práctica nativa, comprobar los enlaces y revisar el estado de las pruebas.
