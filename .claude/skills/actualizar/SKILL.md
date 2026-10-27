---
name: actualizar
description: Traer los cambios del remoto (pull con rebase) al repo Virtualan-definicion. Usar cuando el usuario diga "actualizar", "/actualizar", "trae los cambios", "haz pull".
---

# Actualizar

**Comando: `/actualizar`**

Trae los últimos cambios del repositorio remoto a la rama actual.

## Flujo

### Paso 1: verificar estado local

1. `git status`.
2. Si hay cambios sin commitear: avisar "Hay cambios sin guardar. ¿Quieres ejecutar `/guardar` primero o continuar?". Si continúa, `git stash` antes del pull y `git stash pop` después.

### Paso 2: traer cambios

1. Si no hay remoto configurado, informar y terminar (sin fallar en silencio).
2. `git pull --rebase`.
3. Si hay conflictos: mostrar los archivos y ayudar a resolverlos. No resolver automáticamente.

### Paso 3: confirmar

```
Actualizado:
  [remoto/rama] → [rama local]
  [N] commits nuevos

Cambios recibidos:
  [lista de archivos modificados]
```

Si no había cambios: "Ya estás al día con el remoto."

## Reglas

- Nunca resolver conflictos sin el usuario.
- Avisar antes de continuar si hay cambios locales sin commitear.
- Trabajar sobre la rama actual.
