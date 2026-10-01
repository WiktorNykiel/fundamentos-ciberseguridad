# Awesome DPD · SmartKEA

**Privacidad que se puede explicar, operar y demostrar.**

Colección editorial de fuentes primarias, itinerarios y herramientas de aprendizaje para delegados de protección de datos, juristas, perfiles de negocio, ingeniería y ciberseguridad. Foco inicial: **España y Unión Europea**. Revisión documental: **18 de septiembre de 2026**.

[Fuentes por tema](FUENTES.md) · [Certificaciones](CERTIFICACIONES.md) · [Plan DPD](ITINERARIO.md) · [Casos y respuestas](CASOS.md) · [Primeros 90 días](90-DIAS.md) · [Plantillas](plantillas/README.md) · [Contribuir](CONTRIBUTING.md) · [Publicación](PUBLICACION.md)

## Qué hay y qué no hay

32 referencias anotadas, 13 opciones de credencial por objetivo, una ruta DPD de seis etapas, ocho casos originales con criterios de respuesta y ocho plantillas de trabajo ficticio. Las horas y recomendaciones son propuestas editoriales. **No es asesoramiento para un caso concreto, un curso reconocido, certificación AEPD-DPD ni un aval de AEPD, ENISA, IAPP o ISACA.**

`awesome-dpd` está preparado como proyecto independiente dentro de este repositorio. Su repositorio propio en `smartkea-cyberinnovation` está pendiente de creación administrativa; no se anuncia aquí una URL de destino como ya disponible.

## Orden para empezar

Lee primero posición y funciones del DPD, después inventario y legitimación, luego riesgo/EIPD, derechos y brechas, contratación y transferencias, y finalmente supervisión y especialidades. Usa la tabla de fuentes para localizar el material oficial, no una copia de una guía ni un resumen sin fecha.

El DPD asesora y supervisa. El responsable conserva sus obligaciones y decisiones; no se atribuye al DPD el poder de aprobar todo tratamiento, aceptar cualquier riesgo o decidir autónomamente notificaciones. La compatibilidad con otras funciones exige analizar conflictos concretos, especialmente quién determina fines y medios. [Fuente CEPD](https://www.edpb.europa.eu/documents/guideline/data-protection-officer_en) y [LOPDGDD](https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673).

## Seguridad y licencias

Solo datos sintéticos. No incluyas expedientes, identidades, secretos, documentación laboral o material de examen reservado en issues, PR o demos. No se descargan documentos externos automáticamente. Las guías oficiales, las marcas y las normas de terceros conservan sus derechos. **Publicación pública no implica licencia abierta**: la licencia de reutilización de los textos y del código debe decidirla el titular antes de anunciar el proyecto como open source. Véase [aviso de licencia](AVISO-LICENCIA.md).

## Validación local

```sh
python3 tools/validate.py
python3 -m unittest discover -s tests -v
python3 tools/render.py
python3 -m http.server 8789 --bind 127.0.0.1 --directory site
```

Python 3.11+; sin paquetes externos, cuentas, claves, telemetría ni backend. El sitio generado funciona con enlaces y lectura sin JavaScript; el filtro y la impresión son mejoras opcionales. El progreso del campus no se mezcla con expedientes profesionales.

## Mantenimiento

Cada fuente registra ámbito, idioma, finalidad y estado de revisión. Una URL correcta no garantiza que su documento siga vigente. Las certificaciones y el calendario normativo se vuelven a contrastar antes de tomar una decisión. El plan de revisión recomendado está en CONTRIBUTING; no se ha activado monitorización automática ni envío de alertas.
