---
name: grill-me
description: Interroga sin tregua un caso de casos/<slug>.md hasta llegar a un entendimiento compartido, buscando huecos en comportamiento, datos, criterios de aceptación y fuera de alcance. Usar cuando el usuario diga "grill me", "/grill-me", "interrógame sobre este caso", "busca huecos en el caso" o quiera endurecer un caso antes de dividirlo.
---

# Grill me

**Comando: `/grill-me [slug]`**

## Rol

Interrogar sin tregua la definición de un caso hasta llegar a un entendimiento compartido. Recorre el árbol de decisiones y resuelve las dependencias entre decisiones una a una.

## Sobre qué se hace

Sobre `casos/<slug>.md`. Si el usuario no da el slug, listar `casos/` y preguntar cuál. Lee el caso entero, `contexto.md` y las pantallas implicadas en `diseno/mapa-de-pantallas.md` (y en Figma si hay conector).

Buscar huecos en:
- **Comportamiento:** reglas, estados (vacío, cargando, error, éxito), validaciones, permisos (administrador global frente a subadministrador), idiomas.
- **Datos:** qué se guarda, qué viene del backend, qué está marcado `REVISAR`.
- **Criterios de aceptación:** ¿se pueden comprobar? ¿cubren errores y estados vacíos?
- **Fuera de alcance:** lo visible en Figma que es fase 2 y no está anotado.

## Cómo

- Una pregunta cada vez, esperando respuesta antes de la siguiente.
- En cada pregunta, da tu recomendación con su porqué.
- Empieza por la decisión que más sostiene el caso: si cae, cae el resto.
- Presiona donde el caso es débil: `REVISAR` sin fuente, criterios vagos, comportamiento que el diseño no cubre.
- Si una pregunta se responde mirando el diseño, el contexto o el repo de desarrollo (`../virtualan`, si está añadido con `--add-dir`, solo lectura), míralo en vez de preguntar.
- Retar no es bloquear: señala la debilidad y deja que el usuario decida.

## Al terminar

1. Actualiza `casos/<slug>.md` con lo aclarado (Comportamiento, Datos, Criterios, Fuera de alcance).
2. Lo que siga sin saberse no se inventa: queda en la sección Dudas como checkbox, con a quién preguntar (Olaia, diseño; Marta, técnico; Iker Ibero, cliente), y `REVISAR` con su fuente donde corresponda.
3. Resume en pocas líneas qué se cerró y qué dudas quedan. Si el caso estaba `definido`, mantén el estado salvo que las dudas lo invaliden.

## Reglas

- Una pregunta a la vez; nunca un cuestionario en bloque.
- Siempre con recomendación.
- No inventar: todo dato sin fuente se marca `REVISAR`.
- Ortografía correcta (tildes, ñ, ¿¡) en todo lo que se escriba.
