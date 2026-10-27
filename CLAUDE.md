# CLAUDE.md · Virtualan-definicion

Repo de definición de producto de Virtualan (equipo de discovery de 540). No contiene código. El repo de desarrollo es `../virtualan` (`/Users/lewricka/Development/Virtualan/virtualan`): se consulta con `--add-dir` cuando exista y es de solo lectura desde aquí.

## Contexto

Virtualan es el cliente; CulturApp (culturapp.es) es una app móvil sin descarga para visitar patrimonio cultural (ayuntamientos, museos, yacimientos, castillos). Cada entidad publica lugares, puntos de interés y contenidos multiidioma, y coloca QR físicos. Se rediseñan el panel de administración y la app del visitante: la funcionalidad actual con mejoras visuales y de UX, más la gestión de QR dentro del panel.

No hay estudio de estrategia ni research: es ejecución a partir del diseño. MVP del panel = Lugares y Administradores (con QR); app = Inicio, Explorar, Visita y Cuenta. Pago, escanear QR desde la app, ventas, papelera, usuarios, buscador del panel, 3D y RA son fase 2. Detalle, decisiones y preguntas abiertas en `contexto.md`.

## Cómo se trabaja

1. `/extraer-diseno`: lee el Figma, rellena `mapa-de-pantallas.md` y propone los casos.
2. `/definir`: completa un caso, sección a sección.
3. `/grill-me` (opcional): interroga el caso para encontrar huecos.
4. `/dividir`: parte el caso en tareas para desarrollo.
5. `/estado`: regenera `estado.md`.

Git: `/guardar` (commit sin push), `/actualizar` (pull con rebase), `/compartir` (guardar + actualizar + push).

## Reglas

- No inventar. Lo que no esté en el diseño ni decidido se marca `REVISAR` con su fuente.
- El diseño de Figma es la fuente de verdad de las pantallas; este repo lo es del comportamiento y los criterios de aceptación.
- Nombres de fichero y carpeta en minúsculas, sin acentos, con guiones. Contenido con ortografía correcta (tildes, ñ, ¿¡).
- Commits en español. Push solo con `/compartir` o si se pide.
- Un caso = un fichero: `casos/<slug>.md`, sin subcarpetas.
- La fase 2 no se define: solo se anota en «Fuera de alcance».

## Interlocutores

| Quién | Rol |
|---|---|
| Iker Ibero | Virtualan, decisor, aprueba prototipos |
| Olaia Merino | 540 UX/UI, lead de diseño (panel, app, design system) |
| Marta García | 540 desarrollo: backend, QR, estimación |
| Pablo | 540, socio: alcance, precio, plazos |
| Iker Mariñelarena | 540, facilita; usuario de este repo |

## Enlaces

- [Notion del proyecto](https://app.notion.com/p/540/Virtualan-Redise-o-de-CulturApp-panel-y-app-405c31909e598188a8b2dc6c2fb49a5a)
- [Figma · Design system](https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=0-1)
- [Prototipo del panel](https://www.figma.com/proto/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?page-id=165%3A2228&node-id=165-3514&starting-point-node-id=165%3A3514&scaling=scale-down-width)
- [Prototipo de la app](https://www.figma.com/proto/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?page-id=48%3A2&node-id=330-621&starting-point-node-id=330%3A621&scaling=scale-down-width)
- [Prototipo web del panel completo](https://claude.ai/artifact/PaBRhqaDqYbzCvk3myfnuV) (referencia, no al día)
- [Panel actual](https://dashboard.culturapp.es) · [Web](https://culturapp.es)
- [Notas del kick off](https://docs.google.com/document/d/1e4TgfvuTsCmoBWrBc7FVxwinhhj2yNG7RkEQXexO1cg) · [Notas del aterrizaje](https://docs.google.com/document/d/1CZbK-Ne6PNGCo82J47NWVi47PfvEfJMoun09vUqrV5A)
