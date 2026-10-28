---
name: tablero
description: Regenera estrategia/user-story-mapping.html (el tablero visual del User Story Mapping) a partir de estrategia/user-story-mapping.md y estrategia/capturas/frames.json. Usar cuando el usuario diga "tablero", "/tablero", "regenera el tablero", "actualiza el html del mapa", o tras cualquier cambio en user-story-mapping.md.
---

# Tablero

**Comando: `/tablero [--publicar]`**

El markdown `estrategia/user-story-mapping.md` es lo que se edita; el HTML `estrategia/user-story-mapping.html` es lo que se lee. Esta skill reconstruye el HTML para que nunca se quede atrás. `/guardar` la ejecuta sola antes de cada commit.

## Flujo

1. Ejecutar desde la raíz del repo:
   ```
   python3 herramientas/generar-tablero.py
   ```
2. Si el generador falla, el markdown no tiene la estructura esperada (ver «Estructura» abajo). Corregir el markdown, no el HTML.
3. Si avisa de un id de Figma sin captura, tomar la captura (ver «Capturas») o quitar el id de la columna Figma.
4. Comprobar que `estrategia/user-story-mapping.html` cambió (`git diff --stat estrategia/user-story-mapping.html`) y decir cuántas historias y frames tiene.
5. Solo con `--publicar` o si el usuario lo pide: republicar el artefacto de claude.ai con la herramienta Artifact, pasando el mismo fichero y las capturas que hayan cambiado. El enlace es el de `contexto.md`. El artefacto es un enlace para enseñar fuera del equipo; la copia de trabajo es el repo.

## Estructura que espera el generador

- `## Cortes (entregables)`: tabla `Corte | Nombre | Qué demuestra | Criterio de hecho`. Un corte validado lleva en el nombre `· **validado el AAAA-MM-DD**`.
- `## Mapa · Panel (administrador)` y `## Mapa · App (visitante)`: una sección `### P<n> · Nombre` o `### V<n> · Nombre` por actividad, con una tabla `Historia | Corte | Pantallas | Caso | Figma | REVISAR`. Corte: número o «—». Caso: slug entre acentos graves o «—». Figma: ids de frame separados por coma (`165-2229, 184-2201`) o «—».
- `## Walking skeleton · recorrido exacto`: párrafo de validación, lista numerada y párrafo «Lo que queda fuera…».
- `## Decisiones pendientes para cerrar el mapa`: tabla `Decisión | Quién | Afecta a`.
- `## Fuera de alcance (fase 2)`: un párrafo.

Los ids de historia (`P3-2`) se calculan por orden dentro de cada actividad: cambian al insertar o mover filas. No usarlos como referencia estable en otros documentos; usar el texto de la historia o el caso.

## Capturas

`estrategia/capturas/frames.json` es el catálogo de frames (id, nombre, producto, captura) y `estrategia/capturas/<id>.jpg` la imagen de cada uno. Para añadir un frame nuevo: añadirlo al catálogo y capturarlo desde el prototipo de Figma en el navegador con la interfaz oculta (`&hide-ui=1`), recortando el borde negro con `magick <fichero> -fuzz 5% -trim +repage <fichero>`. Los frames altos del panel se capturan por trozos con desplazamiento y se unen con `magick a.jpg b.jpg -append salida.jpg`.
