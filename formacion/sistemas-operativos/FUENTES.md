# Fuentes primarias y control de vigencia

Fecha de revisión documental: **2026-09-14**. Las fuentes se usan como referencia para diseñar actividades; no certifican el curso ni demuestran que sus laboratorios se hayan ejecutado. Las URLs pueden actualizarse. La versión efectiva se fija en la ficha de cada imagen, no se deduce de la versión que muestre una web.

| ID | Fuente oficial consultada | Uso didáctico |
|---|---|---|
| S01 | GNU, [Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html) | Sintaxis, expansión, quoting, redirecciones y programación shell |
| S02 | Proyecto systemd, [documentación](https://systemd.io/) | Unidades, servicios, aislamiento, operación y referencias de journal |
| S03 | Microsoft, [Windows Commands](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands) | CMD, BAT y utilidades nativas; comprobar aplicabilidad por edición |
| S04 | Microsoft, [PowerShell 101](https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/01-getting-started) | Objetos, herramientas, PowerShell 7 frente a Windows PowerShell 5.1 |
| S05 | Microsoft, [about_Remote_Requirements](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_remote_requirements) | Requisitos de remoting y diferencias de transporte |
| S06 | Microsoft Sysinternals, [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) | Telemetría, configuración y semántica de eventos |
| S07 | Apple, [Platform Security](https://support.apple.com/guide/security/welcome/web) | Seguridad de plataforma, integridad, cifrado y controles nativos |
| S08 | OpenBSD/OpenSSH, [ssh(1)](https://man.openbsd.org/ssh) | Administración remota autenticada, claves y verificación de host |
| S09 | Docker, [Swarm mode](https://docs.docker.com/engine/swarm/) | Conceptos y operación básica de servicios distribuidos |
| S10 | NIST, [NICE Framework latest updates](https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center/about/nice-framework-latest-updates) | Referencia de tareas, conocimientos y habilidades profesionales |
| S11 | NIST, [SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | Respuesta a incidentes ligada a la gestión del riesgo |
| S12 | MITRE, [ATT&CK](https://attack.mitre.org/) | Lenguaje para comportamientos, detecciones y cobertura; no puntuación automática |
| S13 | CIS, [Benchmarks](https://www.cisecurity.org/cis-benchmarks) | Selección de baseline por producto y versión; revisar licencia de cada recurso |
| S14 | Ollama, [CLI reference](https://docs.ollama.com/cli) | Ejemplo opcional de inferencia y gestión de modelos desde terminal |

## Puntos de actualización que afectan al curso

El manual de Bash consultado describe Bash 5.3; no asumir esa versión en Linux o en el Bash incluido en macOS. Las características se comprueban con la versión local. El temario trata Bash y zsh como lenguajes relacionados, no idénticos. [S01]

La documentación de PowerShell consultada permite diferenciar Windows PowerShell 5.1 y PowerShell 7; recomienda evitar privilegios innecesarios. La execution policy no es una frontera de seguridad. El curso no enseña a desactivar controles para que un script funcione. [S04]

La documentación de remoting distingue WinRM de SSH. Tener PowerShell en Linux no incorpora las APIs administrativas de Windows. No se prescribe TrustedHosts global ni listeners expuestos a Internet. [S05]

La portada de Apple Platform Security consultada corresponde a la edición de agosto de 2026. No se extrapola un control de Apple Silicon a todo Mac Intel ni se presupone una versión de macOS común a los alumnos. [S07]

NICE publica componentes v2.2.0 en 2026. La matriz del curso es una interpretación pedagógica por perfiles, no un mapeo exhaustivo de identificadores oficiales. NIST SP 800-61 Rev. 3 es la referencia de respuesta utilizada; no se presenta la revisión anterior como la vigente. [S10, S11]

## Consulta primaria local obligatoria

Linux: `man`, `info`, ayuda de la distribución y documentación del paquete instalado. Windows: `Get-Help`, `Get-Command`, ayuda de cada ejecutable y Microsoft Learn con el selector de producto. macOS: `man`, ayuda de Terminal, documentación Apple de la versión y ayuda de las utilidades instaladas. Las guías rápidas no sustituyen esta consulta.

Se amplía la lectura, antes de impartir la unidad concreta, con los manuales oficiales de GNU Coreutils, GNU grep/sed/gawk/findutils, zsh, el hipervisor elegido, Nginx/Apache/IIS, Kubernetes, el gestor de copias y el colector de logs. Estos recursos complementarios no se presentan como versiones verificadas en esta edición.

## Registro de revisión

Por cada dependencia: producto, versión, arquitectura, URL oficial, fecha consultada, estado de soporte, licencia, comandos de verificación, cambio detectado y módulos afectados. Revisar antes de cada cohorte; después de cambios relevantes en SO, shell, formatos o políticas; y al actualizar imágenes. Los enlaces rotos o cambios funcionales generan una corrección editorial antes de reutilizar el laboratorio.

No se incorporan correos privados, nombres de terceros, enlaces internos de trabajo ni materiales con identidad institucional. Las referencias externas se enlazan; no se copian sus manuales íntegros.
