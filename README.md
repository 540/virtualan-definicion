# Virtualan · Definición de producto

Repo de definición del rediseño de CulturApp (panel y app) para Virtualan. Aquí se traduce el diseño de Figma en casos de uso con comportamiento y criterios de aceptación, y se dividen en tareas para desarrollo. No contiene código.

- `CLAUDE.md`: instrucciones para la IA y flujo de trabajo.
- `contexto.md`: qué es el proyecto, alcance, decisiones, preguntas abiertas, interlocutores y enlaces.
- `diseno/mapa-de-pantallas.md`: pantallas y flujos del diseño, con enlace a Figma.
- `estrategia/user-story-mapping.md`: estrategia de desarrollo (usuarios, actividades, historias, cortes). Es lo que se edita.
- `estrategia/user-story-mapping.html`: el mismo mapa como tablero visual con capturas de Figma. Es lo que se lee. Se genera con `/tablero` (o `python3 herramientas/generar-tablero.py`); no se edita a mano.
- `estrategia/capturas/`: capturas de los frames de Figma y su catálogo `frames.json`.
- `herramientas/`: el generador del tablero, su plantilla y `plantilla-caso.md`.
- `casos/`: un fichero por caso de uso. Se crea con el primer caso.
- `estado.md`: tabla de casos y estado. La genera `/estado` cuando hay casos.
- `.claude/skills/`: `/extraer-diseno`, `/tablero`, `/definir`, `/grill-me`, `/dividir`, `/estado`, `/guardar`, `/actualizar`, `/compartir`.

Para empezar: lee `contexto.md`, abre `estrategia/user-story-mapping.html` en el navegador.
