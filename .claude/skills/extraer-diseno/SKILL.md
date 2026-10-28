---
name: extraer-diseno
description: Lee el diseño de Figma de CulturApp, rellena diseno/mapa-de-pantallas.md (pantallas, flujos, enlace al frame) y propone la lista de casos de uso, creando un casos/<slug>.md por cada uno desde la plantilla. Usar cuando el usuario diga "extrae el diseño", "/extraer-diseno", "monta el mapa de pantallas", "propón los casos", o al empezar el repo o tras cambios en Figma.
---

# Extraer diseño

**Comando: `/extraer-diseno [enlace de Figma o página]`**

Paso 1 del flujo. Convierte el diseño en un mapa de pantallas y en una lista de casos de uso.

## Fuentes, por orden

1. Conector de Figma, si está disponible: leer el archivo «CulturApp · Design system» (enlaces en `contexto.md`), páginas «Prototipo · Panel MVP» y «Prototipo · App». Anotar el enlace a cada frame.
2. Si no hay conector: capturas o descripción que pegue el usuario. Decirlo y pedirlas.
3. `contexto.md` para saber qué es MVP y qué es fase 2.

No inventes pantallas ni flujos. Lo que no puedas ver, se marca `REVISAR` con la fuente que falta.

## Paso 1: rellenar `diseno/mapa-de-pantallas.md`

Respeta el esqueleto (Panel: Lugares con lista, ficha, puntos, punto y QR, y Administradores; App: Inicio, Explorar, Visita, Cuenta). Para cada pantalla:
- Nombre y qué muestra (acciones, estados visibles).
- Flujo: a qué pantallas lleva y desde cuáles se llega.
- Enlace al frame de Figma.

Lo que sea fase 2 va en su sección aparte, sin definir. Sustituye la nota «Pendiente de extraer del Figma» por lo extraído y pon la fecha de extracción.

## Paso 2: proponer los casos

Criterio de corte, inspirado en `create-use-cases`:
- **Un caso = un flujo que el usuario completa de principio a fin y que da valor por sí solo**, no una pantalla. Ejemplo: «Crear un lugar y publicarlo», «Generar y descargar el QR de un punto».
- Pasa cada candidato por la prueba de tamaño: si sus criterios se encadenan con «y» (crear y editar y borrar y reordenar), son varios casos con un solo nombre. Pistas: «gestionar», «administrar», «y», «o», «incluyendo». Parte en rebanadas verticales (crear / editar / borrar, por tipo de contenido, por rol).
- Una pantalla puede aparecer en varios casos; un caso puede cruzar varias pantallas.
- Fase 2 no genera casos.

Presenta la lista como tabla: slug, título, producto (panel | app), pantallas implicadas, y por qué es un caso independiente.

## Paso 3: confirmar y crear

**Pide confirmación de la lista antes de crear ficheros.** Con el visto bueno, crea la carpeta `casos/` si no existe y un `casos/<slug>.md` por caso desde `herramientas/plantilla-caso.md`:
- `estado: por-definir`, `producto`, `figma:` con los enlaces de los frames.
- «Pantallas de Figma implicadas» ya rellena. El resto, tal cual la plantilla.
- Slug en minúsculas, sin acentos, con guiones. Sin subcarpetas.

## Al terminar

Resume: pantallas extraídas, casos creados y qué quedó `REVISAR`. Sugiere `/definir` sobre el primer caso.
