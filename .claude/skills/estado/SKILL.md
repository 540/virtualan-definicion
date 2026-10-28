---
name: estado
description: Regenera estado.md leyendo el frontmatter de casos/*.md, con una tabla de casos y un resumen de tres líneas. Usar cuando el usuario diga "estado", "/estado", "cómo vamos", "actualiza el estado", "qué casos hay".
---

# Estado

**Comando: `/estado`**

Vista rápida del avance de la definición. Solo lee `casos/*.md` y reescribe `estado.md`. No toca `../virtualan` aunque exista.

## Flujo

1. Listar `casos/*.md`. Si la carpeta no existe o no hay casos, avisar y no crear `estado.md`.
2. De cada caso leer: título (primer `#`), `producto`, `estado`, tareas hechas/total (en la sección Tareas, tareas `### T<n>` y su casilla `Hecha: [x]`), dudas abiertas (casillas `- [ ]` en la sección Dudas).
3. Reescribir `estado.md`:

```markdown
# Estado de los casos

Actualizado: AAAA-MM-DD

<Resumen de tres líneas: cuántos casos hay y en qué estados; qué toca ahora; dónde están los bloqueos (dudas abiertas).>

| Caso | Producto | Estado | Tareas hechas/total | Dudas abiertas |
|---|---|---|---|---|
| [titulo](casos/slug.md) | panel | definido | 0/0 | 3 |
```

4. Mostrar la tabla y el resumen en la respuesta.

## Reglas

- Fecha real con `date +%F`.
- Orden: por producto (panel, app) y por estado (de por-definir a hecho).
- Usar guion «0/0» o «-» cuando no hay tareas.
- No commitear (eso es `/guardar`).
- Ortografía correcta (tildes, ñ, ¿¡).
