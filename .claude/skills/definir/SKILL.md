---
name: definir
description: Completa un caso de casos/<slug>.md sección a sección mirando el Figma, preguntando solo lo que el diseño no dice (comportamiento, datos, errores, límites). Usar cuando el usuario diga "define este caso", "/definir", "completa el caso", "pasa el caso a definido".
---

# Definir

**Comando: `/definir [slug]`**

Paso 2 del flujo. El problema ya está resuelto por el diseño: aquí no hay problema, evidencia ni research. Se trata de convertir el diseño en un caso sin ambigüedades.

## Carga (silenciosa)

1. Si no dan slug, listar los casos `por-definir` en `casos/` y preguntar cuál.
2. Leer el caso, `contexto.md` (alcance, decisiones, fase 2) y su parte en `diseno/mapa-de-pantallas.md`.
3. Mirar los frames de Figma del caso (conector de Figma si está; si no, pedir capturas).
4. Presentar el arranque: título, producto, pantallas, secciones vacías.

## Cómo

Trabaja **sección a sección** de la plantilla: Qué hace el usuario · Pantallas · Comportamiento · Datos · Criterios de aceptación · Fuera de alcance · Dudas.

- Lo que el diseño ya muestra se escribe sin preguntar.
- Pregunta **solo lo que el diseño no dice**: reglas, estados vacíos y de error, validaciones, límites, permisos, qué se guarda y qué viene del backend.
- Propón una **respuesta por defecto** cuando sea razonable y pide confirmación. Una pregunta cada vez.
- Lo que no esté en el diseño ni decidido (`contexto.md`, notas del kick off o del aterrizaje) no se inventa: `REVISAR` con la fuente, y a Dudas con a quién preguntar (Olaia, diseño; Marta, técnico; Iker Ibero, cliente).
- Criterios de aceptación comprobables, en Given/When/Then en castellano o lista simple. Incluye errores y estados vacíos.
- Fuera de alcance: lo que se ve en Figma y es fase 2, con referencia a `contexto.md`. Fase 2 no se define.
- No escribas en el fichero sin confirmación de cada sección.

## Al terminar

1. Pon `estado: definido` en el frontmatter.
2. Resume qué quedó `REVISAR` y cuántas dudas abiertas hay.
3. Si hay muchas dudas o decisiones de comportamiento delicadas, sugiere `/grill-me`. Si no, sugiere `/dividir`.

## Reglas

- No inventar. Ortografía correcta (tildes, ñ, ¿¡).
- No tocar otros casos ni `contexto.md` (si algo decidido falta allí, proponlo al usuario).
