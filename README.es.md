<div align="center">

<img src="docs/assets/hero.jpg" alt="Una línea se divide en tres rutas de distinto grosor y se vuelve a unir en una marca de verificación" width="100%">

<h1>HappyCoding Everyday</h1>

<p><strong>Los hábitos de un gran ingeniero, dentro de tu asistente de programación con IA.</strong></p>

<p>Los cambios pequeños, rápidos. Los grandes, con cuidado. Instálalo una vez en Codex y cada tarea de programación sale mejor, sin configurar nada.</p>

[![Release](https://img.shields.io/github/v/release/caredhieacid/jensenmo-happy_coding_everyday?color=2f7d5b)](https://github.com/caredhieacid/jensenmo-happy_coding_everyday/releases)
[![CI](https://github.com/caredhieacid/jensenmo-happy_coding_everyday/actions/workflows/validate.yml/badge.svg)](https://github.com/caredhieacid/jensenmo-happy_coding_everyday/actions/workflows/validate.yml)
[![Status: Alpha](https://img.shields.io/badge/status-alpha-f59e0b)](#estado-del-proyecto)
[![License: MIT](https://img.shields.io/badge/license-MIT-1f2328.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md)

[Por qué HappyCoding](#por-qué-happycoding) · [Primeros pasos](#primeros-pasos) · [El problema](#el-problema) · [Ejemplos](#ejemplos) · [Resultados de las pruebas](#resultados-de-las-pruebas) · [Documentación](docs/README.md)

</div>

## Por qué HappyCoding

- **Funciona en cuanto lo instalas.** Sin modos, sin prompts especiales, sin configuración. Pide las cosas como siempre.
- **No solo "listo": bien hecho.** Encuentra la causa real, corrige todos los sitios que lo necesitan y ejecuta la comprobación que demuestra el arreglo.
- **Nunca complica tu trabajo.** Corregir una errata es un diff de una línea. Sin planes, sin agentes de más, sin funciones que nadie pidió.
- **Solo pregunta lo que solo tú puedes decidir.** Una pregunta breve con opciones claras y una recomendación, en vez de una suposición equivocada que tengas que deshacer.
- **Seguro desde el principio.** Las claves de API no van al código, nada se sube ni se despliega sin ti y las reglas de tu proyecto siempre van primero.
- **Casi no ocupa espacio.** La parte que se carga en cada tarea tiene menos de 60 líneas, así que el contexto queda libre para tu código.
- **Probado como software de verdad.** Cada comportamiento clave tiene su propio escenario de prueba, ejecutado en sesiones nuevas de Codex y puntuado por otro revisor.

## Primeros pasos

Dos comandos en tu terminal:

```bash
codex plugin marketplace add caredhieacid/jensenmo-happy_coding_everyday
codex plugin add jensenmo-happy-coding-everyday@jensenmo-happy-coding
```

El primero añade este repositorio de GitHub como fuente de plugins en Codex. HappyCoding todavía no está en un directorio oficial de plugins, así que no hace falta registrarse ni pasar ninguna revisión. El segundo instala el plugin. También puedes ejecutar solo el primero y, en Codex, abrir **Plugins**, elegir **JensenMo HappyCoding** e instalar **HappyCoding Everyday**.

Listo. Abre una tarea nueva y pide las cosas como siempre. No hay nada que configurar:

```text
Corrige el error del inicio de sesión, no toques mis otros cambios y dime qué comprobaste.
```

Para llamarlo por su nombre, escribe `$jensenmo-happy-coding-everyday`.

## Instalar el skill directamente

```bash
git clone https://github.com/caredhieacid/jensenmo-happy_coding_everyday.git
cd jensenmo-happy_coding_everyday
mkdir -p "$HOME/.agents/skills"
ln -s "$(pwd)/skills/jensenmo-happy-coding-everyday" \
  "$HOME/.agents/skills/jensenmo-happy-coding-everyday"
```

Si ya hay algo en esa ruta, revísalo antes de reemplazarlo.

**Claude Code:** enlaza la misma carpeta en `~/.claude/skills/` y el skill también se carga allí. Por ahora, las pruebas de comportamiento solo se han hecho en Codex.

## El problema

Los asistentes de programación con IA son muy capaces, pero si los dejas solos suelen fallar de una de estas dos formas.

| Se quedan cortos | Se pasan |
| --- | --- |
| Cambian la primera línea sospechosa en vez de buscar la causa real | Escriben un plan y lanzan varios agentes para corregir una errata |
| La misma lógica está en dos sitios y solo corrigen uno | Ejecutan todas las pruebas y otra revisión por un cambio de una línea |
| Dicen "listo" sin haber ejecutado nada | Añaden validaciones, opciones y secciones de README que nadie pidió |
| De tres requisitos, uno se pierde sin avisar | Crean pantallas llenas de degradados, emojis y textos publicitarios que parecen una plantilla |
| Si les pides poner una clave de API en el código, lo hacen | Te piden elegir un modo de trabajo antes de empezar |

Las herramientas de flujo de trabajo pesadas resuelven la columna izquierda, pero a cambio todas las tareas tienen que pasar por la derecha. HappyCoding resuelve las dos: decide cuánto proceso necesita cada tarea según su tamaño y su riesgo, así obtienes un trabajo cuidadoso sin cargas de más.

## Qué obtienes

| Función | Qué significa |
| --- | --- |
| **El proceso se ajusta a la tarea** | Las tareas pequeñas se hacen directamente. Solo los cambios que tocan seguridad, datos o producción reciben comprobaciones extra. No eliges ningún modo. |
| **Comprueba su trabajo de verdad** | Primero reproduce el problema, ejecuta la comprobación correspondiente después del último cambio y te dice qué no comprobó. |
| **Nada a medias** | Busca todos los demás sitios a los que afecta el cambio (llamadas, código duplicado, configuración, documentación) y los actualiza, o explica por qué no. |
| **Pregunta solo cuando hace falta** | Si equivocarse obligaría a rehacer trabajo, hace una pregunta breve con dos a cuatro opciones y una recomendación. Si el código lo responde, no pregunta. |
| **Nada de extras** | No añade funciones, opciones, adornos ni documentación que no pediste. |
| **No se olvida de los casos habituales** | Antes de informar, repasa una lista corta según el tipo de cambio: casos límite, compatibilidad, datos, dinero y fechas, y los estados de carga y error de la interfaz. |
| **Seguro desde el principio** | Las claves de API no van al código ni a los commits. No hace commit, push ni despliegue si no lo pides. Las reglas de tu proyecto van primero. |
| **Interfaz acorde a tu aplicación** | Las pantallas nuevas reutilizan tus componentes y estilos, sin aspecto de plantilla genérica. |
| **Informes claros** | Primero el resultado, en tu idioma: qué cambió, qué se comprobó, qué falta y qué hacer después. |

## Ejemplos

Son respuestas reales de las pruebas, sin editar. La máquina de pruebas está configurada para responder en chino, así que aquí aparecen traducidas.

**Pregunta cuando solo tú puedes decidir.** Petición: *"Change the date format on invoices."* (cambia el formato de fecha de las facturas)

> ¿Qué formato de fecha prefieres? Ahora la fecha de emisión y la de vencimiento se muestran como `2026-10-22`.
>
> - `22/10/2026` (día/mes/año)
> - `10/22/2026` (mes/día/año)
> - `22 Oct 2026` (recomendado: evita confundir día y mes)
>
> Cuando lo confirmes, cambiaré los dos sitios y ejecutaré las pruebas.

No cambió ningún archivo antes de tener la respuesta.

**Sigue la estructura de tu proyecto.** Petición: *"Add an endpoint that returns how many open tasks a project has."* (añade un endpoint que devuelva cuántas tareas abiertas tiene un proyecto)

> Añadí `GET /projects/{id}/tasks/open-count`, que devuelve `{"open_count": 2}`.
>
> - Solo cuenta las tareas `open` del proyecto; devuelve 0 si no hay ninguna.
> - Un ID que no es entero devuelve 400; un proyecto que no existe devuelve 404.
> - Mantuve las tres capas que ya había y actualicé la documentación de la API.
>
> Ejecuté `python3 -m unittest discover -s tests`: las 8 pruebas pasan y `git diff --check` también. El cambio está solo en local y no hice commit.

**Si se arregla con una línea, cambia una línea.** Petición: *"A production button label has one typo. Change only that string…"* (el texto de un botón en producción tiene una errata; cambia solo ese texto…)

> Cambié `Sumbit order` por `Submit order` en `CheckoutButton.jsx:5`; ese texto es lo único que cambió.
>
> Revisé el diff y `git diff --check` pasa. No ejecuté todas las pruebas, ni hice commit ni despliegue.

## Resultados de las pruebas

Muchas colecciones de prompts y flujos de trabajo nunca se prueban. HappyCoding sí. Cada comportamiento clave tiene un escenario de prueba: una petición realista, un proyecto de ejemplo pequeño, una lista de cosas que el asistente debe hacer y otra de cosas que nunca debe hacer. Cada prueba abre una sesión nueva de Codex y otro revisor compara el resultado con las dos listas, punto por punto.

| Elemento | Cantidad |
| --- | --- |
| Escenarios de prueba | **24** |
| Proyectos de ejemplo (frontend, backend por capas, cálculos con dinero, claves de API, reglas de commit y más) | **12** |
| Sesiones nuevas de Codex durante la versión 0.3.0 | **59** |
| Sesiones puntuadas punto por punto por otro revisor | **48** |

**Lo consiguió en todas las rondas puntuadas:**

- encontró la causa real sin quedarse en código que solo parecía sospechoso;
- un arreglo de una línea se quedó en una línea;
- siguió las reglas de ramas y commits que el proyecto tiene documentadas;
- no puso una clave de API pegada en el chat en archivos que se suben al repositorio;
- colocó el código de backend en las capas que indica la documentación del proyecto;
- creó pantallas nuevas solo con los estilos existentes.

El registro completo de las pruebas está en [docs/pressure-tests.md](docs/pressure-tests.md).

**Construido consigo mismo.** HappyCoding se desarrolla usando HappyCoding. Hasta ahora hay 9 pull requests fusionados y CI en cada uno. El paquete de cada versión se puede verificar y no se puede modificar después de publicarse.

Si HappyCoding te ahorra tiempo, dale una estrella al repositorio. Es la forma más fácil de ayudar a que otros desarrolladores lo encuentren.

## Tres formas de trabajar

| Forma | Cuándo | Qué hace |
| --- | --- | --- |
| **Everyday** | Una tarea clara de la que puede encargarse una sola persona | Lee el código, hace el cambio más pequeño y ejecuta la comprobación que lo demuestra |
| **Collaboration** | El trabajo se divide en partes independientes, o hay mucho código que leer | Varios asistentes investigan a la vez; solo uno edita los archivos compartidos |
| **Delivery** | Seguridad, migraciones de base de datos, producción o un despliegue entre equipos | Escribe un plan, revisa cada paso, pide una revisión independiente y prepara cómo volver atrás |

Cuando termina la parte arriesgada, vuelve a Everyday. Abrir un pull request, tocar muchos archivos o ejecutar una prueba de extremo a extremo en local no convierte, por sí solo, una tarea en Delivery. En cada tarea solo se carga `SKILL.md` (menos de 60 líneas); los demás archivos se leen cuando hacen falta.

## Principios de diseño

- **Lo pides una vez**: el skill decide el proceso; no eliges ningún modo.
- **Empieza ligero**: solo añade proceso cuando hay un motivo concreto.
- **Una comprobación tiene que demostrar el resultado**: "el comando se ejecutó" no basta.
- **Pregunta solo lo que solo tú puedes decidir**: lo demás lo decide y explica qué supuso.
- **Hace solo lo que se pidió**.
- **Las reglas de tu proyecto van primero**.
- **Si es solo lectura, es solo lectura**: una revisión o una investigación no cambia el código.

Más detalles en la [filosofía de diseño](docs/design-philosophy.md) y la [arquitectura](docs/architecture.md).

## Pruebas y versiones

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/validate_repository.py
```

Al subir una etiqueta `v*` que coincide con la versión de `.codex-plugin/plugin.json`, se crea automáticamente un GitHub Release con el paquete del plugin y su suma SHA-256.

## Estado del proyecto

Está en **Alpha** y listo para usar: las funciones principales, el paquete del plugin, las comprobaciones automáticas y un conjunto completo de escenarios de prueba puntuados ya están disponibles. Las próximas versiones seguirán afinando su criterio con el uso real. Como con cualquier herramienta, revisa los cambios antes de desplegar en producción.

## Licencia

[MIT](LICENSE) © 2026 Jensen Mo
