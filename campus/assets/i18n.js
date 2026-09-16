/** Explicit UI translations; never translates commands, notes or identifiers. */
export const LANG_KEY = 'fundamentos-ciberseguridad:language:v1';
let lang = 'es';
export const language = () => lang;
export function setLanguage(value) { if (!['es','en'].includes(value)) throw new Error('Unsupported language'); lang=value; }
const EN = Object.fromEntries(String.raw`
Saltar al contenido|Skip to content
Fundamentos|Foundations
DE CIBERSEGURIDAD|OF CYBERSECURITY
Fundamentos de ciberseguridad, inicio|Cybersecurity foundations, home
Fundamentos de ciberseguridad|Cybersecurity foundations
Buscar en el curso|Search the course
Buscar teoría, prácticas o referencias…|Search theory, labs or references…
Mi progreso|My progress
Menú|Menu
Navegación del curso|Course navigation
Índice del curso|Course index
Cargando índice…|Loading index…
Formación independiente · Español|Independent learning · English
Formación independiente · ES / EN|Independent learning · ES / EN
Tu avance se guarda en este navegador.|Your progress is saved in this browser.
Publicar y verificar el campus →|Publish and verify the campus →
Preparando el curso|Preparing the course
Los contenidos se cargan desde este mismo sitio.|Content is loaded from this site only.
Pantalla completa|Full screen
Cerrar presentación|Close presentation
← Anterior|← Previous
Siguiente →|Next →
Flechas para avanzar · Esc para cerrar|Arrow keys to navigate · Esc to close
¿Borrar el progreso de este navegador?|Clear progress in this browser?
Se eliminarán las marcas, notas y favoritos del curso. Exporta una copia antes de continuar. No afecta a otros navegadores.|Course checkmarks, notes and bookmarks will be deleted. Export a backup first. Other browsers are not affected.
Conservar progreso|Keep progress
Borrar mi progreso|Clear my progress
Lectura sin JavaScript|Reading without JavaScript
El seguimiento y el asistente necesitan JavaScript.|Progress tracking and the guided assistant need JavaScript.
Abrir la guía de lectura completa, con índice e impresión.|Open the complete reading guide, including its index and print view.
Empieza por aquí|Start here
Índice completo|Full index
Explorar el curso|Explore the course
Mi recorrido|My learning path
Prácticas guiadas|Guided labs
Biblioteca y referencias|Library and references
Índice de aprendizaje|Learning index
Curso|Course
168 de teoría · 312 de práctica|168 theory · 312 practice
Módulos, de base a integración|Modules, from foundations to integration
Prácticas con evidencias|Labs with evidence
Tu avance autodeclarado|Your self-reported progress
Avance del curso|Course progress
Sistemas operativos · Terminal · Ciberseguridad|Operating systems · Terminal · Cybersecurity
Entiende el sistema.|Understand the system.
Domina la terminal.|Master the terminal.
Un recorrido práctico por Linux, Windows y macOS. Aprende el porqué, prueba en tu laboratorio y demuestra cada resultado.|A practical learning path through Linux, Windows and macOS. Understand why, practise in your lab and demonstrate every result.
Continuar mi recorrido →|Continue my learning path →
Comenzar el curso →|Start the course →
Ver temario completo|View the full curriculum
Cómo estudiar|How to study
laboratorio / terminal|lab / terminal
$ comprender el entorno|$ understand the environment
$ practicar con criterio|$ practise with purpose
$ comprobar el resultado|$ verify the result
$ documentar y recuperar|$ document and recover
Esquema de trabajo · no es una terminal|Workflow illustration · not a terminal
TU MAPA DE APRENDIZAJE|YOUR LEARNING MAP
Siete bloques. Una base sólida.|Seven blocks. One solid foundation.
Empieza desde cero o entra en el módulo que necesitas.|Start from scratch or open the module you need.
Lectura continua e impresión ↗|Continuous reading and printing ↗
Entrar en el bloque →|Open this block →
Aprendizaje acompañado, no ejecución remota.|Guided learning, not remote execution.
La web presenta teoría, guía tareas y guarda tus marcas. Los comandos se ejecutan manualmente en tu propio laboratorio. Sin cuenta, telemetría propia ni claves de API.|This site presents theory, guides tasks and saves your checkmarks. Run commands manually in your own lab. No account, application analytics or API keys.
Progreso local y autodeclarado. Completar una pantalla no acredita una competencia profesional.|Local, self-reported progress. Completing a screen does not certify professional competence.
Antes de empezar:|Before you start:
No necesitas experiencia previa.|No previous experience required.
Modo presentación ▷|Presentation mode ▷
En mis favoritos|Bookmarked
Guardar módulo|Bookmark module
Texto normal|Normal text
Texto más grande|Larger text
Secciones del módulo|Module sections
Teoría|Theory
Prácticas|Labs
Autoevaluación|Self-assessment
Los prerrequisitos todavía no están marcados en tu progreso. Puedes consultar este módulo sin bloqueo.|Your progress does not yet show the prerequisites as complete. You can still read this module.
En este módulo|In this module
Consultar el original en GitHub ↗|View the Spanish source on GitHub ↗
Mi cuaderno|My notebook
Qué has aprendido, qué falta por comprobar…|What you learned and what you still need to verify…
Guardado local. No incluyas secretos ni datos personales. Máximo 3.000 caracteres.|Saved locally. Do not include secrets or personal data. Maximum 3,000 characters.
Ayuda si te atascas|Help when you get stuck
Tipo de dificultad|Type of difficulty
Ruta|Path
Permisos|Permissions
Comando|Command
Resultado|Result
Evidencia|Evidence
Ayuda editorial local; no es un modelo de IA.|Local editorial guidance; not an AI model.
← Módulo anterior|← Previous module
Volver al curso|Back to the course
Siguiente módulo →|Next module →
Revisar mi recorrido →|Review my progress →
Del concepto a la evidencia.|From concept to evidence.
Cada práctica tiene cinco fases: preparar, ejecutar, verificar, documentar y recuperar. Las marcas las confirma el alumno, no el navegador.|Each lab has five stages: prepare, execute, verify, document and recover. The learner confirms completion, not the browser.
Comprobar antes de avanzar|Check before moving on
Autoevaluación formativa. Puedes revisar la teoría y repetirla; no es un examen supervisado.|Formative self-assessment. Review the theory and try again; this is not a supervised exam.
Comprobar respuesta|Check answer
Ya has respondido correctamente a esta comprobación.|You have already answered this question correctly.
Defensa práctica|Practical explanation
Explica qué cambiaste, cómo comprobaste el resultado y qué no puedes concluir. Después, contrasta tus evidencias con las tres prácticas del módulo.|Explain what you changed, how you verified the result and what you cannot conclude. Then compare your evidence with the module's three labs.
Revisar mis prácticas|Review my labs
He leído y puedo explicar las ideas del módulo|I have read the module and can explain its main ideas
Llevarlo a la práctica →|Put it into practice →
Respuesta correcta.|Correct answer.
Revisa la explicación y vuelve a intentarlo.|Review the explanation and try again.
Completada por ti|Marked complete by you
Pendiente|Pending
Guía ampliada|Extended guide
Revisar práctica →|Review lab →
Abrir asistente →|Open guided lab →
Leer ficha completa|Read the full lab brief
Laboratorio acompañado|Guided laboratory
Aprender haciendo.|Learn by doing.
96 diseños de práctica vinculados al programa. Las guías ampliadas concretan parte de ellos; no añaden horas a las 480 planificadas.|96 lab designs linked to the curriculum. Extended guides develop some of these labs; they do not add hours to the planned 480.
Bloque|Block
Todos los bloques|All blocks
Descargar kit del laboratorio|Download the lab kit
Preparar el entorno|Prepare the environment
Ejecutar con criterio|Execute with care
Comprobar el resultado|Verify the result
Guardar la evidencia|Save the evidence
Revertir y cerrar|Roll back and close
1. Identifica el entorno|1. Identify the environment
Plataforma seleccionada:|Selected platform:
. Cambiar esta selección no convierte una práctica Linux en una práctica Windows o macOS.|. Changing this selection does not turn a Linux lab into a Windows or macOS lab.
Estas consultas identifican tu sesión; no instalan ni modifican el sistema. Revísalas y ejecútalas manualmente en el equipo asignado.|These queries identify your session; they do not install or modify the system. Review them and run them manually on the assigned machine.
Confirma alcance, identidad, directorio, versión y punto de recuperación. Si no puedes identificar el equipo o los efectos, detén la práctica.|Confirm scope, identity, directory, version and recovery point. Stop the lab if you cannot identify the machine or the effects.
2. Ejecuta en tu laboratorio|2. Execute in your lab
Ver instrucciones originales|View the original instructions
No hay terminal remota en esta web. Copiar un comando no lo ejecuta ni demuestra que haya funcionado. No pegues órdenes en sistemas fuera del laboratorio.|This site has no remote terminal. Copying a command neither runs it nor proves it worked. Do not paste commands into systems outside your lab.
3. Contrasta el resultado|3. Cross-check the result
Realiza una prueba positiva y otra negativa. Diferencia «sin coincidencias», «acceso denegado» y «error». No conviertas una ausencia de logs en prueba de ausencia de actividad.|Run a positive and a negative test. Distinguish no matches, access denied and errors. Missing logs do not prove that no activity occurred.
Comprobación del kit oslab.py de R01|R01 oslab.py kit check
Solo para ese dataset, no para el paquete labkit.py.|Only for that dataset, not for the labkit.py package.
Archivos de datos|Data files
Bytes totales|Total bytes
Contrastar cantidades|Compare counts
La comprobación contrasta lo que escribes; no consulta tu equipo ni certifica una ejecución.|This check compares what you enter; it does not query your device or certify execution.
4. Deja una evidencia reproducible|4. Create reproducible evidence
Nota local del módulo|Local module note
Resultado observado, error, comprobación y limitaciones…|Observed result, error, verification and limitations…
No guardes contraseñas, claves, datos personales ni logs reales. Las notas no están cifradas.|Do not save passwords, keys, personal data or real logs. Notes are not encrypted.
Descargar plantilla de evidencia|Download the evidence template
5. Recupera y cierra|5. Recover and close
Volver a las prácticas|Back to labs
Fases de la práctica|Lab stages
Marcado por ti|Marked by you
Pendiente de confirmar|Awaiting confirmation
Marcar este paso y avanzar →|Mark this step and continue →
Marcar cierre|Mark closure
Reabrir práctica|Reopen lab
Completar práctica|Complete lab
Tu cuaderno de aprendizaje|Your learning notebook
Avanza con evidencia.|Make progress with evidence.
Exportar progreso|Export progress
Importar una copia|Import a backup
Reiniciar|Reset
Exporta antes de cambiar de navegador o dominio. La copia incluye tus notas y no está cifrada.|Export before switching browser or domain. The backup includes your notes and is not encrypted.
Tu recorrido, módulo a módulo|Your progress, module by module
Completado|Complete
· Favorito|· Bookmarked
Biblioteca|Library
Consultar, conectar y profundizar|Consult, connect and explore
Tu biblioteca de trabajo.|Your working library.
Lecciones ampliadas, equivalencias de comandos, bastionado, evidencias y referencias primarias. Sin salir del campus.|Extended lessons, command comparisons, hardening, evidence and primary references. All within the campus.
Lectura continua / imprimir|Continuous reading / print
Descargar kit CLI|Download the CLI kit
Referencias y lecciones|References and lessons
Abrir documento →|Open document →
← Volver a la biblioteca|← Back to the library
Fuente original en GitHub ↗|Spanish source on GitHub ↗
Referencia|Reference
Lección ampliada|Extended lesson
Copiar código · no ejecutar|Copy code · do not execute
Copiado. Revisa el comando antes de ejecutarlo en tu laboratorio.|Copied. Review the command before running it in your lab.
El navegador no permite copiar. Selecciona el código y cópialo manualmente.|Your browser cannot copy automatically. Select the code and copy it manually.
No se encontró esa sección|Section not found
El enlace no corresponde a un módulo o recurso del curso.|The link does not match a course module or resource.
No se pudo guardar en este navegador. Exporta el progreso para conservarlo.|Could not save in this browser. Export your progress to keep it.
Práctica marcada como completada por ti.|Lab marked complete by you.
Práctica reabierta.|Lab reopened.
La copia supera 1 MiB en UTF-8.|The backup exceeds 1 MiB in UTF-8.
Esta copia reemplazará las marcas y notas actuales. ¿Continuar?|This backup will replace your current checkmarks and notes. Continue?
Progreso importado y validado.|Progress imported and validated.
Se ha reiniciado únicamente el progreso de este curso.|Only this course's progress has been reset.
Pantalla completa no disponible; continúa en modo presentación.|Full screen is unavailable; continue in presentation mode.
El navegador ha bloqueado la pantalla completa.|The browser blocked full screen.
Una actualización de otra pestaña no era válida.|An update from another tab was invalid.
No se pudo cargar el catálogo.|Could not load the catalogue.
Catálogo incompatible.|Incompatible catalogue.
No se pudo recuperar el progreso local. Puedes importar una copia válida.|Could not recover local progress. You can import a valid backup.
No se ha podido abrir el curso|Could not open the course
Sirve el directorio compilado mediante HTTP(S), no abriendo index.html como archivo local.|Serve the built directory over HTTP(S), rather than opening index.html as a local file.
Abrir lectura continua|Open continuous reading
Tu punto de partida|Your starting point
Empieza por aquí.|Start here.
Un mismo recorrido para leer, presentar, practicar y demostrar lo aprendido. No necesitas instalar el campus en cada máquina del laboratorio.|One learning path to read, present, practise and demonstrate what you have learned. You do not need to install the campus on each lab machine.
1 · Orientarse|1 · Get oriented
Elige tu entrada|Choose your starting point
Sin experiencia previa: empieza en M01. Con experiencia: consulta los prerrequisitos y localiza la competencia que quieres reforzar.|No previous experience: start with M01. Already experienced: check the prerequisites and find the skill you want to strengthen.
Ver el índice completo →|View the full index →
2 · Preparar|2 · Prepare
Separa web y laboratorio|Separate the website from the lab
La web guarda tus marcas; Linux, Windows y macOS se practican en máquinas propias y autorizadas. No pegues credenciales ni registros reales en las notas.|The website saves your checkmarks; practise Linux, Windows and macOS on your own authorized machines. Do not paste credentials or real logs into notes.
Preparar el entorno →|Prepare the environment →
3 · Aprender|3 · Learn
Comprende y comprueba|Understand and verify
Lee la teoría, resuelve la autoevaluación y completa las tres prácticas. En cada una: preparación, ejecución manual, contraste, evidencia y recuperación.|Read the theory, answer the self-assessment and complete the three labs. Each lab covers preparation, manual execution, verification, evidence and recovery.
Abrir las prácticas →|Open the labs →
4 · Conservar|4 · Keep your progress
Continúa otro día|Continue another day
Usa favoritos y notas. Exporta tu progreso antes de cambiar de navegador o dominio. Las marcas no equivalen a horas cursadas ni a una certificación.|Use bookmarks and notes. Export your progress before switching browser or domain. Checkmarks do not represent attended hours or certification.
Mi recorrido y copia de progreso →|My learning path and progress backup →
Tres formas de seguir la misma lección.|Three ways to follow the same lesson.
Teoría para estudiar; presentación con flechas y Escape para exponer; asistente por fases para practicar. La presentación no sustituye las evidencias.|Theory for study; presentation with arrow keys and Escape for teaching; a step-by-step guide for practice. Presentations do not replace evidence.
Comenzar M01 →|Start M01 →
Guía de estudio completa|Complete study guide
Leer sin JavaScript|Read without JavaScript
Mapa curricular · fuente única|Curriculum map · single source
Índice completo del curso.|Complete course index.
32 módulos, 96 diseños de práctica y 480 horas planificadas. Acceso directo a teoría, prácticas y autoevaluación; los prerrequisitos orientan, no bloquean.|32 modules, 96 lab designs and 480 planned hours. Direct access to theory, labs and self-assessment; prerequisites guide you without blocking access.
Buscar en el índice|Search the index
Avance|Progress
Todos los estados|All statuses
Sin empezar|Not started
En curso|In progress
Completados por ti|Marked complete by you
Limpiar filtros|Clear filters
No hay módulos con estos filtros. Limpia los filtros para recuperar el índice completo.|No modules match these filters. Clear the filters to restore the full index.
Saltar a un bloque|Jump to a block
Módulo|Module
Teoría / práctica|Theory / practice
Antes|Prerequisites
Accesos|Open
Sin requisitos|No prerequisites
Completado por ti|Marked complete by you
Las horas son planificación docente, no tiempo medido. Las fichas diseñadas y los ejercicios ejecutados se distinguen en sus evidencias de validación.|Hours represent teaching plans, not measured time. Lab designs and executed exercises are distinguished by their validation evidence.
Conceptos, comandos y documentos|Concepts, commands and documents
Resultados de búsqueda.|Search results.
Escribe un concepto, un comando o varias palabras.|Enter a concept, a command or several words.
No hay coincidencias|No matches
Prueba con «permisos», «PowerShell», «logs» o un código de módulo.|Try permissions, PowerShell, logs or a module code.
La copia no corresponde a este curso o versión de progreso.|The backup does not match this course or progress version.
Estructura de progreso inválida.|Invalid progress structure.
La copia contiene módulos o prácticas desconocidos.|The backup contains unknown modules or labs.
Datos del módulo no válidos.|Invalid module data.
Estado de práctica incoherente.|Inconsistent lab state.
Preferencias inválidas.|Invalid preferences.
Archivo demasiado grande (máximo 1 MiB en UTF-8).|File too large (maximum 1 MiB in UTF-8).
Comprueba el directorio actual, las comillas y la existencia de la ruta. Una ruta incorrecta no se arregla elevando privilegios. Trabaja solo dentro del laboratorio.|Check the current directory, quotation marks and whether the path exists. Elevating privileges does not fix an incorrect path. Work only within the lab.
Identifica la cuenta, el propietario y el permiso efectivo. Revisa directorios padres y controles de plataforma. No cambies permisos de forma global ni desactives protecciones.|Identify the account, owner and effective permissions. Check parent directories and platform controls. Do not change permissions globally or disable protections.
Confirma el sistema, el intérprete, la versión y la ayuda local. Una opción GNU puede no existir en macOS; un cmdlet Windows puede no estar disponible en PowerShell sobre Linux.|Confirm the system, interpreter, version and local help. A GNU option may not exist on macOS; a Windows cmdlet may not be available in PowerShell on Linux.
Separa ausencia de resultados, error y falta de visibilidad. Contrasta con una segunda herramienta y registra el contexto. No marques éxito únicamente porque no se imprimió un error.|Distinguish no results, errors and lack of visibility. Cross-check with another tool and record the context. Do not mark success simply because no error was printed.
Conserva originales y trabaja sobre copias. Registra fecha, origen, herramienta, alcance y limitaciones. No pegues secretos, datos personales ni logs reales en tus notas.|Preserve originals and work on copies. Record date, origin, tool, scope and limitations. Do not paste secrets, personal data or real logs into your notes.
Esta práctica requiere administración nativa de otra plataforma. Utiliza su máquina virtual o equipo correspondiente; las consultas de orientación no sustituyen ese entorno.|This lab requires native administration of another platform. Use the corresponding virtual machine or device; orientation queries do not replace that environment.
Coincide con R01: 8 archivos y 62 bytes. Explica ahora el alcance y los metadatos.|Matches R01: 8 files and 62 bytes. Now explain scope and metadata.
No coincide con R01. Revisa la carpeta datos, los ocultos y la diferencia entre bytes y bloques de disco.|Does not match R01. Check the datos folder, hidden files, and the difference between bytes and disk blocks.
`.trim().split('\n').map(line=>line.split('|')));
const rules = [
 [/^Mi progreso · (\d+) %$/, (_,n)=>`My progress · ${n} %`],
 [/^(\d+) horas$/, (_,n)=>`${n} hours`],
 [/^(\d+) de (\d+) módulos visibles\.$/, (_,a,b)=>`${a} of ${b} modules visible.`],
 [/^(\d+)\/(\d+) completados$/,(_,a,b)=>`${a}/${b} complete`],
 [/^Prácticas \((\d+)\)$/,(_,n)=>`Labs (${n})`],
 [/^· (\d+) h teoría \/ (\d+) h práctica$/,(_,a,b)=>`· ${a} h theory / ${b} h practice`],
 [/^DIAPOSITIVA (\d+) \/ (\d+)$/,(_,a,b)=>`SLIDE ${a} / ${b}`],
 [/^(\d+) % del recorrido marcado$/,(_,n)=>`${n} % of the learning path marked`],
 [/^(\d+) resultados para «(.*)»\.$/,(_,n,q)=>`${n} results for “${q}”.`],
 [/^Módulos de (.+)$/,(_,name)=>`Modules in ${name}`],
 [/^Avance (M\d+)$/,(_,id)=>`Progress ${id}`],
 [/^Recorrido detallado: (.+)$/,(_,name)=>`Detailed guide: ${name}`],
 [/^(\d+) de 32 módulos completos; (\d+) lecturas y (\d+) prácticas marcadas\. Un módulo se completa al confirmar lectura, tres prácticas y autoevaluación\.$/,(_,a,b,c)=>`${a} of 32 modules complete; ${b} readings and ${c} labs marked. A module is complete when reading, three labs and self-assessment are confirmed.`],
 [/^(\d+)\/(\d+) hitos\. No mide horas reales ni certifica competencia\. Almacenamiento local, sin sincronización entre dispositivos\.$/,(_,a,b)=>`${a}/${b} milestones. This does not measure actual hours or certify competence. Local storage; no automatic cross-device synchronization.`],
 [/^(\d+)\/5 fases confirmadas\. Puedes revisarlas en cualquier orden; no se ejecutan acciones automáticamente\.$/,(_,n)=>`${n}/5 stages confirmed. Review them in any order; no actions run automatically.`],
 [/^(?:✓|[1-5]) · (.+)$/, (all,name)=>all.slice(0,4)+t(name)],
 [/^Lectura (.+) · (\d+)\/3 prácticas$/,(_,mark,n)=>`Reading ${mark} · ${n}/3 labs`],
 [/^(M\d+.*) · (\d+) módulos? · (\d+) prácticas$/,(_,ids,n,k)=>`${ids} · ${n} ${n==='1'?'module':'modules'} · ${k} labs`],
 [/^No se importó: (.+)$/,(_,reason)=>'Import failed: '+t(reason)],
];
export function t(value) {
 if(lang!=='en' || typeof value!=='string')return value;
 const s=value.trim();let answer=Object.hasOwn(EN,s)?EN[s]:undefined;
 if(answer===undefined){for(const [re,convert] of rules){if(re.test(s)){answer=s.replace(re,convert);break;}}}
 return answer===undefined?value:value.slice(0,value.length-value.trimStart().length)+answer+value.slice(value.trimEnd().length);
}
const previous = new WeakMap();
export function localiseUI(root = document) {
 const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);
 let node;
 while((node=walker.nextNode())){
   if(node.parentElement?.closest('pre, code, textarea, script, style, [data-no-translate]'))continue;
   const record=previous.get(node);const source=record&&record.output===node.nodeValue?record.source:node.nodeValue;
   const output=t(source);node.nodeValue=output;previous.set(node,{source,output});
 }
 for(const element of root.querySelectorAll('[aria-label], [placeholder], [title]')){
   for(const name of ['aria-label','placeholder','title'])if(element.hasAttribute(name)){
     const key='data-original-'+name;const source=element.getAttribute(key)||element.getAttribute(name);
     element.setAttribute(key,source);element.setAttribute(name,t(source));
   }
 }
 for(const a of root.querySelectorAll('a[href="lectura.html"],a[href="reading.html"]')) a.setAttribute('href',lang==='en'?'reading.html':'lectura.html');
}
