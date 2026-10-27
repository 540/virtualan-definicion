# Contexto · Virtualan · Rediseño de CulturApp

Última actualización: 2026-10-27

## Qué es

CulturApp (culturapp.es) es una app móvil sin descarga para visitar patrimonio cultural: ayuntamientos, museos, yacimientos, castillos. Cada entidad publica lugares, puntos de interés y los contenidos de cada punto (texto, audio, vídeo, imagen, antes y después, 360) en varios idiomas, y coloca QR físicos que llevan al visitante al contenido.

Se rediseñan dos productos: el **panel de administración** (dashboard.culturapp.es) y la **app del visitante**. El alcance es la funcionalidad actual con mejoras visuales y de UX, más la gestión de QR dentro del panel. No hay estudio de estrategia ni research: es un proyecto de ejecución a partir del diseño.

## Dolores de partida

- Los QR se generan fuera (QR Kit) porque los enlaces cambiaban al editar.
- Solo se registra el primer escaneo.
- Lo borrado no se recupera.
- El panel está en inglés.
- Saltos de línea forzados con puntos blancos.
- Stripe da fallos.
- Los subadministradores no tienen una gestión clara.

## Alcance del MVP

**Panel:** Lugares (ficha, puntos y punto) y Administradores, con el QR dentro de cada lugar y de cada punto. Un QR por destino. Configuración general separada de la de cada idioma.

**App:** Inicio, Explorar (con buscador), Visita y Cuenta (correo o Google). Estilo A. Imágenes y vídeos 360 priorizados.

**Técnico:** front desde cero en React Native (el panel en navegador con react-native-web). Backend por decidir.

## Fase 2 (fuera de alcance)

- Pago de visitas (Stripe) y acceso temporal de 24 h a audioguías.
- Escanear QR desde la app.
- Ventas, papelera, usuarios y buscador en el panel (también precio, fuera del MVP).
- 3D y realidad aumentada.

El panel completo queda en Figma como visión futura (página «Prototipo · Panel completo»).

## Decisiones con fecha

| Fecha | Decisión |
|---|---|
| 2026-09-28 | Kick off: funcionalidad actual con mejoras visuales y de UX. Se priorizan imágenes y vídeos 360; 3D y realidad aumentada se posponen. |
| 2026-10-05 | Aterrizaje (Olaia, Marta, Iker): MVP del panel = Lugares (ficha, puntos y punto) y Administradores, con el QR dentro de cada lugar y de cada punto. Fuera del MVP: ventas, papelera, usuarios, buscador y precio. Un QR por destino. Configuración general separada de la de cada idioma. Front desde cero en React Native; backend por decidir. |
| 2026-10-05 y 2026-10-14 | App: la visita se abre siempre en castellano y el idioma se cambia desde el menú. La cuenta entra en alcance; el pago pasa a fase 2. Explorar tiene buscador. Estilo A. |
| 2026-10-21 | Revisión: cambios de Iker aplicados. «Escanear QR» desde la app pasa a fase 2. |
| 2026-10-26 | Panel: columna Entidad en la lista de lugares; ningún idioma es obligatorio, hay un idioma predeterminado; «Añadir idioma» solo para el administrador global; idiomas con abreviatura (ES · EU · EN · FR · CA · GL); el editor de texto admite una imagen entre título y texto. App: contenidos por pestañas; «Siguiente punto» como botón; idioma elegido siempre a la vista; antes y después horizontal a pantalla completa; cuenta (correo o Google) entra, pago no. |

## Preguntas abiertas para Virtualan

- [ ] Visto bueno a los prototipos del 21 de octubre.
- [ ] Logo de la entidad: ¿campo en el panel o fuera? Hay un comentario de Iker Ibero del 22 de octubre en Figma, sin responder.
- [ ] Migración de los QR ya impresos con QR Kit.
- [ ] Registro de cada escaneo (hoy solo el primero).
- [ ] Número de punto en carteles y mínimos para publicar un lugar.
- [ ] Accesibilidad (sector público, EN 301 549).

## Interlocutores

| Quién | Rol |
|---|---|
| Iker Ibero | Virtualan, decisor, aprueba prototipos |
| Olaia Merino | 540 UX/UI, lead de diseño: panel, app y design system |
| Marta García | 540 desarrollo: coordinación con juniors, backend, QR y estimación |
| Pablo | 540, socio: alcance, precio, plazos |
| Iker Mariñelarena | 540, facilita; usuario de este repo |

## Enlaces

- [Notion del proyecto](https://app.notion.com/p/540/Virtualan-Redise-o-de-CulturApp-panel-y-app-405c31909e598188a8b2dc6c2fb49a5a)
- [Figma «CulturApp · Design system»](https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=0-1) (páginas: Fundamentos, una por componente, Organismos, Prototipo · Panel MVP, Prototipo · Panel completo, Prototipo · App)
- [Prototipo del panel](https://www.figma.com/proto/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?page-id=165%3A2228&node-id=165-3514&starting-point-node-id=165%3A3514&scaling=scale-down-width) (escritorio 1440, con diagrama de flujo y arquitectura al lado)
- [Prototipo de la app](https://www.figma.com/proto/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?page-id=48%3A2&node-id=330-621&starting-point-node-id=330%3A621&scaling=scale-down-width) (375×812; Inicio, Explorar, Visita, Cuenta; sección «Fase 2 · Pago»)
- [Prototipo web del panel completo](https://claude.ai/artifact/PaBRhqaDqYbzCvk3myfnuV) (referencia, no está al día)
- [Panel actual](https://dashboard.culturapp.es) · [Web](https://culturapp.es)
- [Notas del kick off](https://docs.google.com/document/d/1e4TgfvuTsCmoBWrBc7FVxwinhhj2yNG7RkEQXexO1cg) · [Notas del aterrizaje](https://docs.google.com/document/d/1CZbK-Ne6PNGCo82J47NWVi47PfvEfJMoun09vUqrV5A)
- Repo de desarrollo (futuro, hermano): `/Users/lewricka/Development/Virtualan/virtualan`
