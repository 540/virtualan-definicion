---
name: compartir
description: Sincronizar la rama actual del repo Virtualan-definicion con el remoto (guardar, actualizar y push). Usar cuando el usuario diga "compartir", "/compartir", "sube los cambios", "haz push".
---

# Compartir

**Comando: `/compartir`**

Es la única vía de push de este repo (salvo petición expresa). Si hay cambios sin commitear, ejecuta antes el flujo de `/guardar` sin preguntar.

## Flujo

1. `git status`. Si hay cambios sin commitear, ejecutar el flujo de `/guardar`.
2. Si no hay remoto configurado, informar y terminar.
3. Flujo de `/actualizar`: `git pull --rebase`. Si hay conflictos, mostrarlos y ayudar a resolverlos (requiere al usuario).
4. `git push` (si la rama no tiene upstream, `git push -u origin <rama-actual>`).
5. Mostrar resumen:
   ```
   Compartido:
     [rama] → [remoto/rama]
     [N] commits subidos

   Estado:
     Sincronizado con el remoto
   ```

## Reglas

- No preguntar confirmación.
- Siempre pull antes de push.
- Nunca force push.
- Solo parar si hay conflictos de merge.
- Pushea la rama actual; el PR, si procede, se abre a mano.
