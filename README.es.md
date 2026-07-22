<div align="center">

# ⚡ HappyCoding Everyday

### Un flujo de trabajo de Codex que ajusta automáticamente el rigor al riesgo.

Describe el resultado una vez. HappyCoding elige la ruta segura más ligera entre una corrección puntual, una colaboración acotada y una entrega de alto riesgo.

**🌐 Language / 语言 / 言語 / 언어 / Idioma**

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md)

[![Status: Alpha](https://img.shields.io/badge/status-alpha-f59e0b)](#estado-del-proyecto)
[![CI](https://github.com/caredhieacid/jensenmo-happy_coding_everyday/actions/workflows/validate.yml/badge.svg)](https://github.com/caredhieacid/jensenmo-happy_coding_everyday/actions/workflows/validate.yml)
[![Codex Skill](https://img.shields.io/badge/Codex-agent%20skill-111827)](skills/jensenmo-happy-coding-everyday/SKILL.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-22c55e.svg)](LICENSE)

[Inicio rápido](#inicio-rápido) · [Carriles](#tres-carriles-de-ejecución) · [Principios](#principios-de-diseño) · [Documentación](docs/README.md)

</div>

> El [README.md](README.md) en inglés es la fuente canónica. Esta versión es un borrador pendiente de revisión por una persona nativa; si difiere, prevalece la versión inglesa.

## ¿Qué es HappyCoding?

HappyCoding Everyday es una única entrada automática para el flujo de programación de Codex. Convierte una solicitud normal en un contrato pequeño, selecciona el carril de ejecución menos costoso que siga siendo seguro, realiza el trabajo y termina con evidencia nueva posterior al último cambio. No necesitas elegir un modo ni administrar pruebas o agentes en cada tarea.

## Inicio rápido

```bash
codex plugin marketplace add caredhieacid/jensenmo-happy_coding_everyday
```

Abre **Plugins** en Codex, elige **JensenMo HappyCoding** e instala **HappyCoding Everyday**. En una tarea nueva, pide el trabajo con lenguaje normal:

```text
Corrige la regresión de inicio de sesión, conserva mis cambios no relacionados y muestra la verificación nueva.
```

También puedes invocarlo de forma explícita:

```text
$jensenmo-happy-coding-everyday audita este contrato de API antes de modificar código.
```

## Tres carriles de ejecución

| Carril | Cuándo se usa | Comportamiento predeterminado |
| --- | --- | --- |
| **Everyday** | Un resultado acotado, bajo acoplamiento y una ruta de aceptación | Inspeccionar, hacer el cambio mínimo y ejecutar una prueba enfocada |
| **Collaboration** | Trabajo que puede separarse de forma independiente o una superficie de lectura amplia | Paralelizar la lectura y mantener las escrituras compartidas bajo un único responsable |
| **Delivery** | Seguridad, migraciones, producción, coordinación duradera o aceptación real por etapas | Contrato persistente, puertas por etapa, revisión independiente y reversión |

Un pull request, varios archivos o la presencia de frontend y backend no obligan por sí solos a usar Delivery. La decisión depende del riesgo, la independencia, la propiedad y el coste de aceptación.

## Principios de diseño

- **Una sola expresión de la intención**: el usuario no tiene que elegir el flujo.
- **Rigor mínimo suficiente**: se empieza en Everyday y solo se asciende con evidencia.
- **Evidencia por encima de ceremonia**: se demuestra el comportamiento solicitado, no solo la ejecución de un comando.
- **Lectura paralela, escritura controlada**: se protege el contexto sin crear conflictos.
- **Verificación nueva**: la prueba relevante se vuelve a ejecutar después del cambio final.
- **Respeto por el modo de solo lectura**: una auditoría, explicación o diagnosis no autoriza modificaciones.

Consulta la [filosofía de diseño](docs/design-philosophy.md) y la [arquitectura](docs/architecture.md).

## Instalación directa del skill

```bash
git clone https://github.com/caredhieacid/jensenmo-happy_coding_everyday.git
cd jensenmo-happy_coding_everyday
mkdir -p "$HOME/.agents/skills"
ln -s "$(pwd)/skills/jensenmo-happy-coding-everyday" \
  "$HOME/.agents/skills/jensenmo-happy-coding-everyday"
```

Si el destino ya existe, inspecciónalo antes de sustituir o eliminar nada. `$HOME/.agents/skills` es la ubicación actual de skills de usuario documentada por Codex.

## Validación y publicación

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/validate_repository.py
```

Cada PR crea un paquete de vista previa determinista. Una etiqueta `v*` que coincida con la versión del plugin crea automáticamente un GitHub Release con el ZIP y su suma SHA-256. La existencia de un escenario no demuestra su comportamiento: debe evaluarse en un contexto de agente nuevo y comprobar sus invariantes observables.

## Estado del proyecto

El proyecto está en **Alpha**. El enrutamiento principal, el paquete del plugin, las validaciones estructurales y los primeros escenarios de presión están disponibles, pero los umbrales se siguen calibrando mediante tareas reales.

[Documentación](docs/README.md) · [Contribuir](CONTRIBUTING.md) · [Seguridad](SECURITY.md) · [Soporte](SUPPORT.md) · [Código de conducta](CODE_OF_CONDUCT.md)

## Licencia

[MIT](LICENSE) © 2026 Jensen Mo
