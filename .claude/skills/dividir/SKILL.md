---
name: dividir
description: Parte un caso definido en tareas ejecutables por desarrollo, como rebanadas verticales probables solas, y las escribe en la sección Tareas del caso. Usar cuando el usuario diga "divide este caso", "/dividir", "parte en tareas", "prepara las tareas para desarrollo".
---

# Dividir

**Comando: `/dividir [slug]`**

Paso 4 del flujo. Basado en `create-tasks`, `story-splitting` y `hamburger-method`, adaptado a este repo.

## Carga

1. Leer `casos/<slug>.md` entero. Debe estar `definido` (o `dividido`, si se rehace). Si está `por-definir`, parar y sugerir `/definir`.
2. Leer `contexto.md` para el alcance y las decisiones.
3. Si hay dudas abiertas que bloquean, avisar y preguntar si seguir.
4. Si el repo de desarrollo `../virtualan` está disponible (solo lectura), mirar qué existe ya para no proponer lo hecho.

## Criterios

- **Rebanadas verticales:** cada tarea atraviesa lo necesario (pantalla, lógica, datos) y se puede probar sola. **Nada de tareas por capa técnica** («crear tablas», «hacer el endpoint», «maquetar»).
- **Primera tarea = camino feliz mínimo de extremo a extremo.** El flujo más corto que da valor, aunque sea tosco.
- Después, **variantes y errores**, una por tarea: roles, idiomas, validaciones, estados vacíos, errores.
- Si el caso se parte en más de unas cinco tareas, o hay una de la que cuelga casi todo, suele ser señal de que el caso era demasiado grande: propón partirlo en varios casos con `story-splitting` (pistas: «y», «o», «gestionar») antes de seguir.
- Si una tarea es difusa, usa `hamburger-method`: capas del flujo, 4-5 opciones por capa de simple a completa, y compón la rebanada mínima.
- Dependencias solo cuando la tarea necesita de verdad lo anterior para empezar; el resto, en paralelo.
- Cada tarea cubre criterios de aceptación concretos del caso; todos los criterios quedan cubiertos.
- No dividas lo de fase 2.

## Formato de cada tarea (sección Tareas)

```
### T1. <Título>
- Qué incluye: ...
- Cómo se comprueba: ... (criterios del caso que cubre)
- Dependencias: ninguna | T<n>
- Tamaño: S | M | L
- Hecha: [ ]
```

Un tamaño L es sospechoso: intenta partirlo.

## Flujo

1. Propón el despiece (lista corta con tamaños y dependencias) y pide confirmación.
2. Con el visto bueno, escribe las tareas en la sección Tareas y pon `estado: dividido`.
3. **Issues en GitHub:** solo si existe `../virtualan` con remoto en GitHub **y el usuario lo pide expresamente en ese momento**, ofrece crearlas con `gh` (una por tarea, con el caso enlazado) en ese repo. Si no lo pide, no las crees ni lo sugieras con insistencia. Guarda el número en `issue:` solo si se crean.

## Reglas

- No inventar: lo no decidido sigue `REVISAR`.
- No modificar el repo de desarrollo salvo por la creación de issues pedida expresamente.
- Ortografía correcta (tildes, ñ, ¿¡).
