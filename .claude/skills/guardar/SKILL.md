---
name: guardar
description: Commit directo de los cambios del repo Virtualan-definicion, sin push. Usar cuando el usuario diga "guardar", "/guardar", "haz commit", "guarda los cambios".
---

# Guardar

**Comando: `/guardar`**

Ejecuta todo de forma directa, sin pedir confirmación. El usuario ya sabe lo que quiere guardar.

> Este repo es de definición de producto (sin código). `/guardar` solo commitea el contenido del repo.

## Flujo

1. `git status`. Si no hay cambios, informar y terminar.
2. `git add` de todos los archivos modificados o nuevos (excepto `.env` o credenciales).
3. Generar el mensaje de commit en español, descriptivo, con este formato:
   ```
   YYYY-MM-DD HH:MM - [Descripción de qué se hizo]
   ```
   - Fecha con `date +"%Y-%m-%d %H:%M"`.
   - Cuerpo opcional de 2-3 líneas si hace falta. Sin emojis.
   - Usar HEREDOC.
4. `git commit`.
5. Mostrar resumen:
   ```
   Commit realizado:
     [hash] [mensaje]

   Archivos:
     [lista]
   ```

## Reglas

- No preguntar confirmación ni validar el mensaje.
- No hacer push (eso es `/compartir`).
- Commitear en la rama actual, sea cual sea.
- Si hay archivos sensibles (`.env`, credenciales), excluirlos sin avisar.
