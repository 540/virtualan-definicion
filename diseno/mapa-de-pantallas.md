# Mapa de pantallas

Extraído del Figma el 2026-10-27. Fuente: [Figma «CulturApp · Design system»](https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=0-1) · páginas «Prototipo · Panel MVP» y «Prototipo · App».

> Nota de la extracción: el conector de Figma limitó las llamadas (asiento de vista, plan Professional). Los frames marcados «(solo estructura)» se leyeron por nombres de capa, sin captura; sus textos y campos quedan en REVISAR. Lista de frames pendientes de captura al final.

## Panel

### Arquitectura

Frame «Arquitectura · Panel MVP» ([enlace](https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=431-12301), captura). Azul = Lugares, verde = Administradores, gris = Acceso. «Información» y «Puntos de interés» son las dos pestañas de la ficha de lugar. «Borrar lugar», «Invitar administrador» y «Quitar acceso» figuran como nodos del árbol (acciones que en las pantallas son modal, menú o tostada). No aparece nada de QR como nodo propio: el QR vive dentro de la ficha del lugar, del punto y de las filas/listas. No hay nodos de Configuración general ni de idiomas aparte: los idiomas se configuran dentro de la ficha del lugar. No hay diagrama de flujo aparte: los flujos se deducen del árbol y de los nombres de frame.

- Panel de administración (raíz)
  - 1 · Acceso
  - 1 · Lugares
    - 2 · Nuevo lugar
    - 2 · Ficha de lugar
      - 3 · Información
      - 3 · Puntos de interés
        - 4 · Nuevo punto
        - 4 · Punto de interés
          - 5 · Añadir contenido
          - 5 · Editor de contenido
    - 2 · Borrar lugar
  - 1 · Administradores
    - 2 · Invitar administrador
    - 2 · Quitar acceso

### Acceso

#### Acceso (login)
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=165-3514 (captura)
- Muestra: fondo azul de marca con logo CulturApp. Título «Entrar en el panel», subtítulo «Gestiona tus lugares, contenidos y códigos QR.» Formulario con Correo electrónico (icono de sobre), Contraseña (icono de candado y ojo para mostrar/ocultar), casilla «Recordarme», enlace «¿Has olvidado la contraseña?» y botón «Entrar». Pie: «¿No tienes acceso? Pídelo al administrador de tu entidad.»
- Acciones:
  - Escribir correo electrónico
  - Escribir contraseña
  - Mostrar/ocultar contraseña (icono de ojo)
  - Marcar/desmarcar «Recordarme»
  - Pulsar «¿Has olvidado la contraseña?»
  - Pulsar «Entrar»
- Llega desde: inicio del panel / URL del panel (REVISAR: cierre de sesión no visible).
- Lleva a: Lista de lugares (por «Entrar»); recuperación de contraseña (no hay pantalla, REVISAR).
- Variantes:
  - Acceso · contraseña incorrecta (estado de error): https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=177-863 (captura). Mismo formulario con el campo de contraseña resaltado y aviso rojo «La contraseña no es correcta. Vuelve a escribirla o usa «¿Has olvidado la contraseña?».» Acciones: las mismas que Acceso. Llega desde Acceso tras «Entrar» con contraseña errónea; lleva a Lista de lugares (si acierta) o recuperación de contraseña (sin pantalla).

### Lugares

#### Lista de lugares
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=165-2229 (captura)
- Muestra: menú lateral (logo, «Lugares» activo, «Administradores», usuario «Iker Ibero · Administrador global» con chevron abajo). Cabecera «Lugares» con resumen «4 lugares · 2 publicados · 2 en borrador» y botón «Crear lugar». Tabla con columnas Lugar (miniatura, nombre, municipio · provincia), Entidad, Puntos, Idiomas (chips ES/EU/EN/FR; borde discontinuo = idioma que falta), Código QR («Mostrar código» o «—» si no hay), Estado (Publicado / Borrador) y menú «···» por fila. Pie «1–4 de 4 lugares» con paginación. Filas de ejemplo: Fortalezas de Navarra, Ruta de las sardineras, Molinos del Lea, Palacio Real de Olite. No hay buscador ni filtros.
- Acciones:
  - Pulsar «Crear lugar»
  - Pulsar una fila / nombre del lugar (presumible, REVISAR: la captura no muestra hover ni enlace)
  - Pulsar «Mostrar código» (QR del lugar) en una fila
  - Abrir menú «···» de una fila (Editar, Borrar)
  - Paginar (anterior / siguiente)
  - Ir a «Administradores» desde el menú lateral
  - Abrir menú del usuario (chevron en pie del menú lateral; contenido no visible)
- Llega desde: Acceso; menú lateral; Ficha del lugar (migas de pan «Lugares»); tras guardar nuevo lugar (presumible).
- Lleva a: Nuevo lugar; Ficha del lugar (Editar); modal de confirmar borrado; QR del lugar (destino de «Mostrar código» no mostrado); Administradores.
- Variantes:
  - Menú de fila · Acciones del lugar: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=184-2201 (captura; componente `184:2391`, https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=184-2391). Menú «···» abierto sobre la fila «Molinos del Lea» con «Editar» (lápiz) y «Borrar» (papelera, rojo). Acciones: pulsar «Editar»; pulsar «Borrar»; cerrar el menú (presumible). Lleva a Ficha del lugar (Editar) o al modal de borrado.
  - Modal · confirmar borrado: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=170-752 (captura). Velo oscuro y modal «¿Borrar «Molinos del Lea»?»: «Se borran también sus puntos, contenidos y códigos QR. Los carteles impresos con esos códigos dejarán de funcionar.» Botones «Cancelar» y «Borrar lugar» (rojo), X para cerrar. Acciones: pulsar «Borrar lugar»; pulsar «Cancelar»; pulsar X para cerrar. Lleva a lugar borrado (confirmar) o a la lista (cancelar).
  - Tostada · lugar borrado: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=177-960 (captura; tostada `177:1155`, https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=177-1155). Lista sin «Molinos del Lea», resumen «3 lugares · 2 publicados · 1 en borrador», pie «1–3 de 3 lugares» y tostada oscura abajo a la izquierda ««Molinos del Lea» se ha borrado.» con «Deshacer» y X. Acciones: pulsar «Deshacer»; cerrar la tostada (X); el resto de acciones de la lista. Lleva a la lista (con el lugar restaurado si «Deshacer»). REVISAR cuánto dura el «Deshacer» y si el borrado es real o diferido.

#### Ficha del lugar · Información
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=165-2862 (captura)
- Muestra: migas «Lugares > Fortalezas de Navarra», título con badge «Publicado», subtítulo «Gotorlekuak · Fortalezas de Navarra · Pamplona, Navarra · ES, EU», interruptor «Publicado en la app» y botón «Guardar lugar». Pestañas «Información» (activa) y «Puntos de interés 6». «Información general» con tarjetas: Idiomas (casillas ES, EU, EN, FR, CA, GL; «Añadir idioma»; Idioma predeterminado), Código QR del lugar (imagen, nombre «Inicio del lugar», URL `qr.culturapp.es/fn-ruta`, «412 escaneos», «Descargar», «Copiar enlace»), Imágenes (Portada 3:2 · 1200×800, Tarjeta del listado 4:5 · 800×1000, Fondo de bienvenida 4:5 · 1080×1350, Logo de la entidad 1:1 · PNG transparente 400×400, Galería del lugar hasta 6 imágenes 3:2 · 1200×800, «3 de 6»; si tiene otra proporción se recorta desde el centro), Ubicación (dirección o punto de encuentro, municipio, provincia opcional, mapa de Google con marcador arrastrable; «el mapa y las coordenadas se rellenan solos»). Bloque «En cada idioma» → «Textos en cada idioma»: chips ES/EU, «Nombre», «Presentación» (textarea) y «Audio de bienvenida» (MP3, opcional).
- Acciones:
  - Navegar con la miga «Lugares»
  - Activar/desactivar «Publicado en la app»
  - Pulsar «Guardar lugar»
  - Cambiar de pestaña: «Información» / «Puntos de interés»
  - Marcar/desmarcar idiomas (ES, EU, EN, FR, CA, GL)
  - Pulsar «Añadir idioma»
  - Elegir idioma predeterminado (desplegable)
  - Pulsar «Descargar» (QR del lugar)
  - Pulsar «Copiar enlace» (QR del lugar)
  - «Cambiar» portada / tarjeta del listado / fondo de bienvenida / logo de la entidad
  - «Añadir» imagen a la galería del lugar
  - Editar dirección o punto de encuentro, municipio, provincia
  - Arrastrar el marcador del mapa
  - Cambiar de idioma con los chips (ES/EU)
  - Editar «Nombre» y «Presentación» por idioma
  - Subir o quitar «Audio de bienvenida» por idioma
- Llega desde: Lista de lugares (Editar / fila); Nuevo lugar (tras guardar, presumible).
- Lleva a: Lista de lugares (miga); pestaña Puntos de interés.
- Variantes:
  - Ficha · Información · euskera: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=180-1247 (captura). Chip EU activo en «Textos en cada idioma»: «Nombre (EU)» vacío (placeholder «Izena euskaraz»), «Presentación (EU)» vacía (placeholder «Bi edo hiru esaldi»), «Audio de bienvenida (EU)»: «Aún no hay audio en EU». La tarjeta Idiomas añade «Añadir uno nuevo solo puede hacerlo el administrador global.» (la variante ES no lo mostraba, REVISAR cuál es la vigente). Acciones: las de Ficha · Información; escribir nombre y presentación en EU y subir audio EU.

#### Nuevo lugar
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=180-1542 (captura)
- Muestra: ficha vacía. Migas «Lugares > Nuevo lugar», título «Nuevo lugar» con badge «Borrador», texto «Rellena lo básico y guárdalo. Podrás publicarlo cuando esté completo.» Interruptor «Publicar en la app» apagado y botón «Guardar lugar». Pestaña «Puntos de interés 0». Solo ES marcado y predeterminado. Tarjeta QR: «Se crea al guardar el lugar. Después podrás descargarlo para el cartel.» Imágenes con botón «Subir», Ubicación y Textos con placeholders, «Aún sin audio».
- Acciones:
  - Las mismas que Ficha del lugar · Información, con «Subir» imágenes
  - Rellenar los campos del lugar
  - Pulsar «Guardar lugar» (crea el lugar y su QR)
  - Activar «Publicar en la app» (REVISAR: requisitos para publicar)
- Llega desde: Lista de lugares («Crear lugar»).
- Lleva a: Ficha del lugar (tras guardar, presumible); Lista de lugares (miga).

#### Puntos del lugar (pestaña Puntos de interés)
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=165-2990 (captura)
- Muestra: cabecera de la ficha (sin botón «Guardar lugar» visible) y pestaña «Puntos de interés 6» activa. Texto «El orden es el de la visita en la app. Cada punto tiene su código QR y puede tener uno por contenido.» Botón «Añadir punto de interés». Lista de 6 puntos con número de orden, miniatura, título, duración, contadores por tipo de contenido, chips de idiomas, badge «Falta EU», «Aún sin contenidos», flechas subir/bajar (deshabilitadas en primero y último), «Mostrar código QR» y menú «···». Puntos: Castillo de Irurita, Villa medieval de Etxarri Aranatz, Torre de Arbizu, Uharte Arakil, Castillo de Gorriti, Torre de Leitza.
- Acciones:
  - Cambiar a la pestaña «Información»
  - Activar/desactivar «Publicado en la app»
  - Pulsar «Añadir punto de interés»
  - Pulsar un punto (presumible, abre el punto)
  - Subir / bajar un punto en el orden (flechas)
  - Pulsar «Mostrar código QR» de un punto
  - Abrir menú «···» de un punto (contenido no visible)
- Llega desde: pestaña Información; Punto de interés (miga).
- Lleva a: Nuevo punto; Punto de interés; QR del punto; pestaña Información.

#### Punto
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=165-3297 (captura)
- Muestra: migas «Lugares > Fortalezas de Navarra > Castillo de Irurita», título con número de orden «1», subtítulo «8 min · 9 contenidos» y botón «Guardar punto». Tarjetas Duración (estimada, opcional, en min), Código QR del punto (URL `qr.culturapp.es/fn-irurita`, «286 escaneos», «Descargar», «Copiar enlace»), Imágenes (imagen principal 3:2 · 1200×800 con «Cambiar» y «Eliminar»; galería hasta 8 imágenes con «Añadir») y Textos en cada idioma (chips ES/EU, «Título», «Descripción breve» opcional). Sección «Contenidos» con «Añadir contenido» y grupos Textos (4), Audios (2), Vídeos (1), Imágenes (1) y Antes y después (1), cada uno con «Añadir»; cada elemento con miniatura, título, chips de idioma, badge «Falta EU» o «2 de 2 idiomas», lápiz y menú «···». El texto de la sección menciona «vídeo 360» (REVISAR si entra en el MVP; no hay grupo «Vídeo 360»).
- Acciones:
  - Navegar con las migas (Lugares, Fortalezas de Navarra)
  - Pulsar «Guardar punto»
  - Editar duración estimada (min)
  - Pulsar «Descargar» (QR del punto)
  - Pulsar «Copiar enlace» (QR del punto)
  - «Cambiar» o «Eliminar» imagen principal
  - «Añadir» imagen a la galería del punto (hasta 8)
  - Cambiar de idioma con chips (ES/EU)
  - Editar «Título» y «Descripción breve» por idioma
  - Pulsar «Añadir contenido» (menú desplegable por tipo)
  - Pulsar «Añadir» en cada grupo (Textos, Audios, Vídeos, Imágenes, Antes y después)
  - Pulsar lápiz de un contenido (editarlo)
  - Abrir menú «···» de un contenido (contenido no visible)
- Llega desde: Puntos del lugar (fila / «Añadir punto de interés» tras guardar); Editor de contenido (miga).
- Lleva a: Puntos del lugar (miga «Fortalezas de Navarra»); Lista de lugares; Editor de contenido (Texto/Audio/…); menú Añadir contenido.
- Variantes:
  - Punto · euskera: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=181-1520 (solo estructura). Variante con el chip EU activo en «Textos en cada idioma» (por el nombre y el patrón de la variante de lugar). Contenido exacto REVISAR. Acciones: las de Punto (editar título y descripción en EU).
  - Menú · Añadir contenido: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=181-2313 (solo estructura; instancia `181:2649`, https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=181-2649, 256×266 px). Menú desplegable abierto bajo el botón «Añadir contenido». Opciones no leídas (por altura probablemente 6: texto, audio, vídeo, imagen, antes y después, vídeo 360; REVISAR). Cada elemento de contenido incluye datos de «Idiomas», «Archivos», «Códigos» y «Sin código QR propio». Acciones: elegir tipo de contenido a añadir (opciones sin confirmar); cerrar el menú. Lleva a Editor de contenido (por tipo).

#### Nuevo punto
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=181-1862 (solo estructura)
- Muestra: por capas, migas, título «Nuevo punto de interés» con número de orden, «Aún sin contenidos» y botón «Guardar punto». Tarjetas Duración, Código QR del punto («Se crea al guardar el punto. Después podrás descargarlo para el cartel.»), Imágenes (principal y galería hasta 8) y Textos en cada idioma (chips Castellano/Euskera). Sección «Contenidos» con estado vacío «Aún no hay contenidos. Usa «Añadir contenido» para el primero: texto, audio, vídeo, imagen, antes y después o vídeo 360.»
- Acciones:
  - Pulsar «Guardar punto» (crea el punto y su QR)
  - Editar duración
  - Subir imagen principal y galería («Añadir»)
  - Escribir título y descripción por idioma (chips ES/EU)
  - Pulsar «Añadir contenido» (presumiblemente tras guardar, REVISAR)
- Llega desde: Puntos del lugar («Añadir punto de interés»).
- Lleva a: Punto (tras guardar, presumible); Puntos del lugar (miga).

#### Editor de contenido · Texto
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=182-2048 (solo estructura)
- Muestra: por capas, migas, título «Comienza la historia», subtítulo «Texto · Castillo de Irurita» y dos botones de acción en la cabecera (rótulos REVISAR). Bloque «En cada idioma»: «Título y texto, uno por idioma.» Tarjeta «Textos en cada idioma» con chips Castellano/Euskera, campos de título y texto, e «Imagen en el texto» con fila «Galería intermedia» (miniatura, «Galería del lugar», 3:2 · 1200×800 · «3 de 6» y un botón). Los textos de esa fila parecen copiados de la ficha del lugar (REVISAR).
- Acciones:
  - Cambiar idioma con chips (Castellano/Euskera)
  - Editar título y texto por idioma
  - Gestionar «Imagen en el texto» (botón de la galería intermedia, rótulo REVISAR)
  - Dos botones de la cabecera (rótulos no leídos)
- Llega desde: Punto (lápiz de un texto / «Añadir» en Textos / menú Añadir contenido).
- Lleva a: Punto (miga o al guardar, presumible).

#### Editor de contenido · Audio
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=182-2366 (solo estructura)
- Muestra: por capas, migas, título «Audioguía del castillo», subtítulo «Audio · Castillo de Irurita» y dos botones de acción en la cabecera (rótulos REVISAR). «En cada idioma»: «Título y archivo de audio, uno por idioma.» Tarjeta con chips Castellano/Euskera, campo de título, «Audio en castellano» («MP3 · hasta 20 MB») y archivo «audioguia-castillo-es.mp3 · 4:12» con botón de icono (quitar, presumible). Solo existen editores de Texto y Audio en el MVP del Figma.
- Acciones:
  - Cambiar idioma con chips
  - Editar título por idioma
  - Subir/quitar archivo MP3 por idioma (máx. 20 MB)
  - Dos botones de la cabecera (rótulos no leídos)
- Llega desde: Punto (lápiz de un audio / «Añadir» en Audios).
- Lleva a: Punto.

#### QR (del lugar y del punto)
- Figma: sin frame propio (solo estructura; el QR está integrado en otras pantallas)
- Muestra: el QR aparece en la tarjeta «Código QR del lugar» de la ficha (QR, URL, escaneos, «Descargar», «Copiar enlace»), en la columna «Código QR» de la lista («Mostrar código»), en el botón «Mostrar código QR» de cada punto, en la tarjeta «Código QR del punto» y, en estado «Se crea al guardar…», en Nuevo lugar y Nuevo punto. Los contenidos del punto muestran «Sin código QR propio» y «Códigos».
- Acciones:
  - Pulsar «Descargar» (QR del lugar o del punto)
  - Pulsar «Copiar enlace» (QR del lugar o del punto)
  - Pulsar «Mostrar código» (lista de lugares; destino no mostrado, REVISAR si abre modal, panel o la ficha)
  - Pulsar «Mostrar código QR» (lista de puntos; destino no mostrado)
- Llega desde: Lista de lugares; Ficha del lugar · Información; Puntos del lugar; Punto; Nuevo lugar; Nuevo punto.
- Lleva a: no mostrado en el diseño (REVISAR).

### Administradores

#### Administradores (lista)
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=165-2546 (solo estructura)
- Muestra: por capas, título «Administradores», subtítulo «Quién puede entrar en este panel. Cada a…» (truncado), botón de cabecera (presumiblemente «Invitar administrador») y tabla con columnas Persona, Acceso, Entidad, Lugares y celda final de acción. Filas: Iker Ibero (tú, entidad «Todas», 4 lugares, sin quitar), Ane Goikoetxea (Gotorlekuak), Miren Uriarte (Ayuntamiento de Santurtzi) y Jon Arrieta (Ayuntamiento de Ispaster), con botón «Quitar».
- Acciones:
  - Pulsar el botón de cabecera (invitar administrador)
  - Pulsar «Quitar» en una fila de administrador (no en la propia)
  - Ir a «Lugares» desde el menú lateral
- Llega desde: menú lateral.
- Lleva a: Invitar administrador; Quitar acceso.

#### Invitar administrador
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=179-999 (solo estructura)
- Muestra: la lista de administradores con velo y un «Diálogo · Invitar administrador» encima. Campos y botones del diálogo no leídos (REVISAR).
- Acciones:
  - Rellenar el diálogo y enviar la invitación (campos exactos sin confirmar)
  - Cancelar
- Llega desde: Administradores (lista; botón invitar).
- Lleva a: Administradores con invitación enviada (al enviar); Administradores (al cancelar).
- Variantes:
  - Invitación enviada: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=179-1201 (solo estructura; tostada `179:1339`, https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=179-1339). Lista con una fila nueva «Invitación pendiente» (kultura@olite.eus, «Invitación enviada hoy · aún no ha entrado», entidad «Palacio Real de Olite», botón «Cancelar invitación a kultura@olite.eus») y una tostada abajo a la izquierda (texto no leído). Acciones: cancelar invitación (por fila pendiente); quitar acceso a los demás; cerrar la tostada (presumible). Lleva a Administradores.

#### Quitar acceso
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=179-1341 (solo estructura)
- Muestra: la lista con velo (`179:1479`) y un «Modal» de confirmación de quitar acceso. Texto y botones no leídos (REVISAR).
- Acciones:
  - Confirmar quitar acceso
  - Cancelar
- Llega desde: Administradores (botón quitar de una fila).
- Lleva a: Administradores (con la fila retirada, presumible).

## App

### Arquitectura

Frame «Arquitectura · App del visitante» ([enlace](https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=431-891), captura). Árbol de tres niveles. El cuarto menú de la barra inferior se llama «Ajustes» en el diseño (icono de engranaje), no «Cuenta». Barra inferior (captura de Inicio): cuatro iconos, casa (Inicio), lupa (Explorar), pin de ubicación (Visita) y engranaje (Ajustes); barra flotante tipo píldora, con Inicio activo.

- 1 · Inicio
- 1 · Explorar
  - 2 · Resultados
  - 2 · Sin resultados
- 1 · Visita · desde el QR
  - 2 · Bienvenida → 3 · Cambiar idioma
  - 2 · Portada del lugar → 3 · Mapa de la visita
  - 2 · Punto de interés → 3 · Audio, Texto, Vídeo, Antes y después, Vista 360, Imagen
  - 2 · Fin de la visita
- 1 · Ajustes
  - 2 · Idioma de la visita
  - 2 · Sobre la entidad
  - 2 · Entrar o crear cuenta → 3 · Código de verificación, 3 · Ajustes · con cuenta

### Inicio

#### Inicio (A0)
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=330-621 (captura)
- Muestra: logo CulturApp; titular «Visitas guiadas al patrimonio, en tu móvil»; foto grande (slider); texto «Castillos, rutas y museos con audioguía, textos y vídeos. Sin descargar nada: escaneas el código del cartel y empiezas.»; botón «Explorar visitas»; bloque «Cómo funciona» con tres pasos (Escanea el código QR · Elige el idioma · Escucha, lee y mira); sección «Explora visitas» con «Ver todas» y dos tarjetas de visita (Fortalezas de Navarra, Ruta de las sardineras); barra inferior. Pantalla con scroll.
- Acciones:
  - Pulsar «Explorar visitas»
  - Pulsar «Ver todas»
  - Pulsar una tarjeta de visita
  - Desplazar la pantalla
  - Cambiar de menú desde la barra inferior (Inicio, Explorar, Visita, Ajustes)
  - Gesto sobre la foto/slider: REVISAR (el nombre de capa es «Foto · slider1»; no se ve si es carrusel)
- Llega desde: abrir la app sin QR (sección de Figma «Abrir la app sin QR»), barra inferior.
- Lleva a: Explorar («Explorar visitas»/«Ver todas»); Portada del lugar (tarjeta de visita; REVISAR destino exacto); otros menús de la barra.

### Explorar

#### Explorar visitas (D5)
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=311-493 (solo estructura)
- Muestra: título «Explorar visitas»; buscador; leyenda «Todas son gratuitas» (oculta en el frame, con icono de candado oculto: preparada para fase 2 de pago); lista de tarjetas de visita (Fortalezas de Navarra, Ruta de las sardineras); barra inferior.
- Acciones:
  - Escribir en el buscador
  - Pulsar una tarjeta de visita
  - Desplazar la lista
  - Cambiar de menú desde la barra inferior
- Llega desde: Inicio («Explorar visitas», «Ver todas»); barra inferior.
- Lleva a: resultados de búsqueda (al buscar); Portada del lugar (tarjeta).
- Variantes:
  - Explorar · resultados (D6): https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=356-976 (solo estructura). Buscador con botón «Cancelar», leyenda «1 visita para «Pamplona»» y tarjeta(s) que coinciden. Acciones: modificar la búsqueda; pulsar «Cancelar» (vuelve al listado completo; REVISAR comportamiento exacto); pulsar una tarjeta de resultado. Llega desde Explorar visitas (al escribir); lleva a Explorar visitas (Cancelar) o Portada del lugar (tarjeta).
  - Explorar · sin resultados (D7): https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=356-1011 (solo estructura). Buscador con «Cancelar» y bloque de estado vacío «Sin resultados» (108 px de alto). Texto del estado vacío REVISAR (no leído). Acciones: modificar la búsqueda; pulsar «Cancelar»; otras acciones dentro del estado vacío (p. ej. botón): REVISAR. Llega desde Explorar visitas (búsqueda sin coincidencias); lleva a Explorar visitas (Cancelar).

### Visita

#### Bienvenida (A1)
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=50-2 (solo estructura)
- Muestra: REVISAR (el frame no devolvió capas hijas en los metadatos y no se pudo capturar). Por la arquitectura es la entrada de «Visita · desde el QR»; incluye acceso a Cambiar idioma.
- Acciones:
  - Cambiar idioma (por arquitectura)
  - Resto REVISAR
- Llega desde: QR físico.
- Lleva a: Cambiar idioma; Portada del lugar (REVISAR).

#### Cambiar idioma (A2)
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=61-116 (solo estructura)
- Muestra: REVISAR (sin capas hijas en metadatos; sin captura). Nivel 3 bajo Bienvenida.
- Acciones:
  - Elegir idioma (por nombre)
  - Resto REVISAR
- Llega desde: Bienvenida; botón «Idioma» de las cabeceras (presente en Portada y en el reproductor de audio).
- Lleva a: pantalla desde la que se abrió (REVISAR).

#### Portada del lugar (B1 · visita gratuita en curso)
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=227-905 (solo estructura)
- Muestra: imagen de portada; título «Fortalezas de Navarra»; «Gotorlekuak · Pamplona» con «Cómo llegar»; datos «6 puntos», «37 min», «ES · EU»; alerta (oculta); descripción; galería de tres fotos; «Selecciona el punto de interés» con recorrido en línea y lista de 6 puntos; pie «Desarrollado por»; botón «Idioma» fijo; barra inferior.
- Acciones:
  - Cambiar idioma desde el botón «Idioma» (siempre a la vista)
  - Pulsar «Cómo llegar»
  - Deslizar la galería de fotos (REVISAR si es carrusel)
  - Pulsar un punto de la lista
  - Desplazar la pantalla
  - Cambiar de menú desde la barra inferior
- Llega desde: Bienvenida; Inicio/Explorar (tarjeta de visita); barra inferior (menú Visita); Fin de la visita («Volver a la portada»).
- Lleva a: Punto de interés (cualquier punto); Cambiar idioma; Mapa de la visita (REVISAR: no hay frame «Mapa de la visita» en la página); Ajustes/Inicio/Explorar por la barra.
- Variantes:
  - Botón «Idioma» (componente fijo): https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=227-909.
  - Alerta de Portada (oculta, `227:931`): https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=227-931. Mensaje no visible.

#### Punto de interés
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=53-53 (solo estructura; Punto 1 · Castillo de Irurita, B2)
- Muestra: foto del punto; barra superior; título «Castillo de Irurita»; datos «8 min» y «9 contenidos»; descripción corta; «Selecciona el tipo de contenido» con pestañas (Audios, Textos, 360º, Vídeos, Imágenes, Antes y después) y flecha «Ver más pestañas» (carril desplazable). Por pestaña: Audios con «Audioguía de la villa» y «Leyenda de la cueva»; Textos con «Comienza la historia», «El valle y el río», «La cocina de los gentiles» y «Señores y vasallos»; Vídeos e imágenes con el vídeo «El castillo de Irurita · Vídeo 1:30» y filas «Mira» («La torre y la muralla», «Vista 360 desde la torre», «¿Piedra o toba de campaña?»). Pie «Punto anterior» y «Siguiente punto»; barra inferior. En el último punto el pie es «Punto anterior» y «Terminar la visita».
- Acciones:
  - Cambiar de pestaña de contenido
  - Desplazar el carril de pestañas / pulsar «Ver más pestañas»
  - Abrir un audio (fila)
  - Abrir un texto (fila)
  - Reproducir el vídeo
  - Abrir una fila «Mira» (antes y después, 360, imagen)
  - Pulsar «Punto anterior»
  - Pulsar «Siguiente punto» (botón)
  - Pulsar «Terminar la visita» (solo en el último punto)
  - Volver con la barra superior (REVISAR qué botones lleva)
  - Cambiar idioma (REVISAR si hay botón «Idioma» en esta pantalla; sí está en el reproductor)
  - Cambiar de menú desde la barra inferior
- Llega desde: Portada del lugar (lista de puntos); QR físico de un punto; «Punto anterior»/«Siguiente punto» de otros puntos.
- Lleva a: Audio, Texto, Vídeo, Antes y después, Vista 360, Imagen; Punto anterior/siguiente; Portada del lugar; Fin de la visita (desde el último punto).
- Variantes:
  - Punto 1, pestañas: Textos https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=454-5329; Vídeos https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=454-5446; 360º https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=516-1056; Imágenes https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=516-1101; Antes y después https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=516-1146.
  - Punto 2 · Villa medieval de Etxarri Aranatz (B9): https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=62-573. Igual que el punto 1 con «6 min», «2 contenidos» y pestañas Audios y Textos en el frame principal. Pestañas: Textos https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=454-5581; 360º https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=530-1535; Vídeos https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=530-1613; Imágenes https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=530-1691; Antes y después https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=530-1769. Los frames 360º/Vídeos/Imágenes/Antes y después repiten el contenido del punto 1 («El castillo de Irurita · Vídeo 1:30»): parece copia de maqueta. REVISAR si el punto 2 realmente tiene esos tipos.
  - Punto 6 · Torre de Leitza, último punto (B11): https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=526-1398. Igual que los anteriores con «6 min» y «2 contenidos»; el pie cambia a «Punto anterior» y «Terminar la visita» (lleva a Fin de la visita). Fila de texto «La torre»; en Audios las filas «Audioguía de la villa» y «Leyenda de la cueva». Pestañas: Audios https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=530-1847; 360º https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=530-1914; Vídeos https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=530-1988; Imágenes https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=530-2062; Antes y después https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=530-2136.

#### Audio
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=54-72 (solo estructura; B3 · Reproductor)
- Muestra: cabecera con «Cerrar», título «Punto 1 · Castillo de Irurita» y botón «Idioma»; foto cuadrada; título del audio («Audioguía del castillo» · «En castellano · 4:12»); descripción; barra de progreso con tiempos (1:24 / −2:48); controles Pausar/Reproducir visibles; Velocidad, −15 s y +15 s existen pero ocultos; navegación «Audio anterior» y «Siguiente audio»; nota oculta «Sigue sonando aunque bloquees el móvil o…».
- Acciones:
  - Reproducir / pausar
  - Arrastrar la barra de progreso (REVISAR si es interactiva)
  - Pulsar «Audio anterior»
  - Pulsar «Siguiente audio»
  - Cambiar velocidad, −15 s, +15 s (REVISAR: ocultos en el diseño)
  - Cambiar idioma («Idioma»)
  - Cerrar el reproductor
- Llega desde: Punto de interés · pestaña Audios.
- Lleva a: Punto de interés (Cerrar); Cambiar idioma; otro audio.
- Variantes:
  - Audio 2: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=535-2215. Título «Leyenda de la cueva · 2:48».
  - Botón «Idioma» del reproductor: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=523-16167.

#### Texto
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=54-104 (solo estructura; B4, 1 de 4)
- Muestra: barra superior; foto superior; etiqueta «Texto 1 de 4»; título («Comienza la historia»); varios párrafos de ejemplo; navegación «Anterior» y «Siguiente texto».
- Acciones:
  - Pulsar «Siguiente texto»
  - Pulsar «Anterior»
  - Desplazar para leer
  - Volver con la barra superior
- Llega desde: Punto de interés · pestaña Textos.
- Lleva a: Texto anterior/siguiente; Punto de interés.
- Variantes:
  - 2 de 4: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=535-2269
  - 3 de 4: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=535-2284
  - 4 de 4: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=535-2299

#### Vídeo
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=63-254 (solo estructura; B5)
- Muestra: barra superior; reproductor de vídeo; «Vídeo · 1:30 · en castellano»; título «El castillo de Irurita»; descripción; alerta oculta (REVISAR su uso; podría avisar de que el vídeo no está en el idioma elegido).
- Acciones:
  - Reproducir / pausar
  - Controles del reproductor: REVISAR (no leídos)
  - Volver con la barra superior
- Llega desde: Punto de interés · pestaña Vídeos e imágenes.
- Lleva a: Punto de interés.
- Variantes:
  - Alerta del Vídeo (oculta, `141:2545`): https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=141-2545.

#### Antes y después
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=54-140 (solo estructura; B6)
- Muestra: barra superior; etiqueta «Antes y después»; título «La torre y la muralla»; comparador con imagen «Hoy» y «Antes», tirador (flechas izquierda/derecha), etiqueta «Antes» y botón «Pantalla completa»; alternativa accesible con «Ver antes» y «Ver hoy»; ayuda «Desliza el tirador para comparar. La ima…».
- Acciones:
  - Arrastrar el tirador para comparar
  - Pulsar «Ver antes»
  - Pulsar «Ver hoy»
  - Pulsar «Pantalla completa» (abre la versión horizontal)
  - Volver con la barra superior
- Llega desde: Punto de interés (fila «Mira · La torre y la muralla»).
- Lleva a: Antes y después · pantalla completa; Punto de interés.

#### Antes y después · pantalla completa
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=454-5288 (solo estructura)
- Muestra: frame apaisado de 812×375; comparador a pantalla completa con etiquetas «Hoy» y «Antes», tirador con flechas y botón «Volver».
- Acciones:
  - Arrastrar el tirador
  - Pulsar «Volver»
  - Girar el móvil: REVISAR (no consta si entra al girar o con el botón)
- Llega desde: Antes y después (botón «Pantalla completa»).
- Lleva a: Antes y después.

#### Vista 360
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=63-289 (solo estructura; B7)
- Muestra: REVISAR (frame sin capas hijas en metadatos; sin captura).
- Acciones:
  - REVISAR (por tipo, arrastrar para mirar alrededor: no confirmado)
- Llega desde: Punto de interés (fila «Mira · Vista 360 desde la torre»; pestaña 360º).
- Lleva a: Punto de interés (REVISAR).

#### Imagen
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=63-312 (solo estructura; B8)
- Muestra: barra superior; foto; título «¿Piedra o toba de campaña?»; descripción; bloque de audio de la imagen «Escuchar la explicación · Audio · 0:58» con botón reproducir.
- Acciones:
  - Reproducir el audio de la imagen
  - Ampliar o hacer zoom en la imagen: REVISAR
  - Volver con la barra superior
- Llega desde: Punto de interés (fila «Mira · ¿Piedra o toba de campaña?»; pestaña Imágenes).
- Lleva a: Punto de interés.

#### Fin de la visita
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=63-339 (solo estructura; B10)
- Muestra: foto del último punto; insignia (Badge, oculta); «Has terminado la visita»; «Gracias por recorrer Fortalezas de Navar…»; pie «Desarrollado por»; botón «Volver a la portada».
- Acciones:
  - Pulsar «Volver a la portada»
  - Cambiar de menú desde la barra (REVISAR si hay barra inferior)
- Llega desde: Punto de interés último («Terminar la visita»).
- Lleva a: Portada del lugar.

#### Mapa de la visita
- Figma: sin frame en la página «Prototipo · App»; solo aparece como caja en la arquitectura (nivel 3 bajo Portada del lugar). Solo estructura.
- Muestra: REVISAR: no existe diseño. Puede ser la línea de recorrido de la Portada u otra pantalla pendiente.
- Acciones:
  - REVISAR
- Llega desde: Portada del lugar (por arquitectura).
- Lleva a: REVISAR.

### Cuenta (en el diseño: «Ajustes»)

#### Ajustes · con cuenta (D2)
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=350-993 (solo estructura)
- Muestra: REVISAR (frame sin capas hijas en metadatos; sin captura). Por la arquitectura, es el estado del menú Ajustes con la sesión iniciada. No se ha visto el Ajustes sin cuenta (¿existe frame? no consta).
- Acciones:
  - REVISAR
- Llega desde: Código de verificación (al entrar); barra inferior.
- Lleva a: Idioma de la visita, Sobre la entidad (por arquitectura); REVISAR.

#### Idioma de la visita
- Figma: sin frame propio en la página; aparece en la arquitectura (nivel 2 bajo Ajustes). Solo estructura.
- Muestra: REVISAR: puede ser la misma hoja «Cambiar idioma» (A2).
- Acciones:
  - REVISAR
- Llega desde: Ajustes (por arquitectura).
- Lleva a: REVISAR.

#### Sobre la entidad (D3)
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=66-397 (solo estructura)
- Muestra: barra superior; logo de la entidad; «Gotorlekuak» / «Fortalezas de Navarra»; texto de presentación; filas de contacto (Web gotorlekuak.eus con icono de enlace externo, Teléfono 948 000 000, Horario de atención «Lunes a viernes, 9:00 a 14:00»); filas legales con flecha (Aviso legal, Privacidad y cookies, Declaración de accesibilidad); pie «Con la tecnología de» + logo CulturApp.
- Acciones:
  - Abrir la web de la entidad (enlace externo)
  - Llamar al teléfono: REVISAR (la fila no muestra icono de acción)
  - Abrir Aviso legal
  - Abrir Privacidad y cookies
  - Abrir Declaración de accesibilidad
  - Volver con la barra superior
- Llega desde: Ajustes.
- Lleva a: Aviso legal, Privacidad y cookies, Declaración de accesibilidad (frames no diseñados: REVISAR); web externa.

#### Entrar con correo (A5)
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=309-16968 (solo estructura; «Entrar o crear cuenta»)
- Muestra: logo; título «Entra para guardar tu visita»; texto «Te enviaremos un código de 6 cifras. No …»; campo Correo; casilla «Acepto las condiciones de compra y la po…» con enlaces «Condiciones de uso» y «Privacidad»; botón «Enviar código»; separador «o»; botón «Continuar con Google»; pie; botón «Atrás».
- Acciones:
  - Escribir el correo
  - Marcar la casilla de aceptación
  - Abrir Condiciones de uso
  - Abrir Privacidad
  - Pulsar «Enviar código»
  - Pulsar «Continuar con Google»
  - Pulsar «Atrás»
  - Estados de error del campo (correo no válido, casilla sin marcar): REVISAR
- Llega desde: Ajustes (sin cuenta).
- Lleva a: Código de verificación; Ajustes · con cuenta (por Google; REVISAR); Ajustes.

#### Código de verificación (A6)
- Figma: https://www.figma.com/design/1RBvs1NprjX6oR3P76wE99/CulturApp-%C2%B7-Design-system?node-id=309-16990 (solo estructura)
- Muestra: logo; «Escribe el código»; «Lo hemos enviado a ana.larranaga@gmail.c…»; seis casillas de cifra; ayudas «Reenviar código» y «Cambiar correo»; aviso «¿No te llega? Revisa el correo no desead…»; botón «Entrar»; botón «Atrás».
- Acciones:
  - Escribir las 6 cifras
  - Pulsar «Entrar»
  - Pulsar «Reenviar código»
  - Pulsar «Cambiar correo»
  - Pulsar «Atrás»
  - Estado de código incorrecto o caducado: REVISAR
- Llega desde: Entrar con correo.
- Lleva a: Ajustes · con cuenta; Entrar con correo.

## Fase 2 (visible en Figma, fuera de alcance)

Solo se lista lo que las extracciones anotan como fase 2 o posible fase 2; no se define.

- Vídeo 360: mencionado en el texto de Punto y de Nuevo punto del panel (según contexto, 3D/RA y 360 son fase 2; REVISAR si entra en el MVP). En la app existen la pestaña «360º» y la pantalla Vista 360.
- Escaneos: «412 escaneos» y «286 escaneos» en las tarjetas QR del panel (REVISAR si es MVP o fase 2).
- Multi-entidad: columna «Entidad» en la lista de lugares y en Administradores; sin selector de entidad.
- Buscador y filtros de la lista de lugares: no aparecen (coherente con «buscador» en fase 2).
- Papelera: no hay; el borrado de lugar usa «Deshacer» (REVISAR).
- Gestión de usuarios de la app: no visible en el panel (fase 2).
- Pago en la app: leyenda «Todas son gratuitas» con candado oculto en Explorar y nombre de frame «Portada · visita gratuita (en curso)».
- Otros rastros de pago: molécula «Pago seguro con Stripe» (página `153:208`, fuera del Prototipo, no leída) y casilla «Acepto las condiciones de compra…» en Entrar con correo.
- No se encontró la sección «Fase 2 · Pago» en la página «Prototipo · App» (`48:2`), cuyas secciones de primer nivel son «1 · Inicio», «2 · Explorar», «3 · Visita», «4 · Ajustes» y el frame de arquitectura.
- No se encontró el tablero «Preguntas y dudas» en la página de la app ni como página del archivo. Posibles ubicaciones: otra página (p. ej. «Portada» `0:1` o «Descartes» `2:23`), un archivo de FigJam o Notion. Sin transcripción: 0 preguntas leídas.

## REVISAR

### Frames descritos solo por estructura

El conector de Figma agotó su cuota durante la extracción, así que 30 frames se describieron por nombres de capa, sin verlos. El 2026-10-27 se capturaron todos desde el prototipo en el navegador: están en `estrategia/capturas/<id>.jpg` con su catálogo en `estrategia/capturas/frames.json`, y se ven en el tablero `estrategia/user-story-mapping.html`. Lo que falta es contrastar las descripciones de esos frames con la captura y quitar sus REVISAR.

- Panel (9): Nuevo punto `181-1862`, Punto · añadir contenido `181-2313`, Editor · Texto `182-2048`, Editor · Audio `182-2366`, Administradores `165-2546`, Administradores · invitar `179-999`, Administradores · invitación enviada `179-1201`, Administradores · confirmar borrado `179-1341`, Punto · euskera `181-1520`.
- App (21): todos salvo Inicio `330-621`. Bienvenida `50-2`, Cambiar idioma `61-116`, Vista 360 `63-289` y Ajustes · con cuenta `350-993` no tenían capas hijas en los metadatos y están sin describir: la captura es la única fuente.

### Pantallas que la arquitectura nombra y no existen como frame

Panel:
- «Editor de contenido» solo existe para Texto y Audio; faltan Vídeo, Imagen, Antes y después y Vídeo 360 (aunque Punto ya lista contenidos de Vídeo, Imagen y Antes y después).
- Frame de «Borrar punto» y «Borrar contenido» (el menú «···» de las filas de punto y de contenido no se muestra abierto).
- Recuperación de contraseña («¿Has olvidado la contraseña?»).
- «Mostrar código» (QR del lugar desde la lista) y «Mostrar código QR» (QR del punto desde la lista de puntos).
- «Añadir idioma» (enlace en la tarjeta Idiomas; el texto dice que solo el administrador global puede añadir uno nuevo).
- Menú de usuario (chevron «Iker Ibero · Administrador global» en el menú lateral): cierre de sesión / perfil.

App:
- «Mapa de la visita» e «Idioma de la visita»: nodos de arquitectura sin frame propio.
- «Aviso legal», «Privacidad y cookies» y «Declaración de accesibilidad»: filas de Sobre la entidad sin pantalla diseñada.
- Ajustes sin cuenta (con el acceso «Entrar o crear cuenta»): no existe frame, solo D2 «con cuenta». No hay pantalla de perfil con cerrar sesión visible.
- Estados de carga, error de red, QR no válido y vista previa de 360: no hay frames. Solo existe «Explorar · sin resultados».

### Comportamiento no definido en el diseño

Panel:
- Roles: se ve «Administrador global» (Iker Ibero) y administradores de entidad. No se ven las diferencias de permisos entre ambos salvo «Añadir idioma nuevo solo lo puede hacer el administrador global» y la columna «Entidad: Todas».
- Estado Publicado/Borrador: requisitos para publicar un lugar; qué pasa con un lugar publicado que se despublica (QR, app).
- Nuevo lugar: tras guardar, ¿a qué pantalla va? El QR se crea al guardar.
- Contenidos del punto: «Cada contenido puede tener su propio código QR» y «Sin código QR propio» aparecen en el diseño, pero no hay pantalla de gestión de QR por contenido.
- Borrado de lugar: el modal avisa de que se borran puntos, contenidos y QR y de que los carteles dejan de funcionar, pero hay tostada «Deshacer». REVISAR plazo de deshacer y si el borrado es lógico (papelera es fase 2).
- Lista de lugares: no se ve estado vacío, ordenación ni filtros, ni cómo se abre la ficha (clic en fila). No se ve qué hace «Mostrar código».
- Idiomas: la ficha de lugar en ES (`165:2862`) y en EU (`180:1247`) difieren en el texto de la tarjeta Idiomas (la EU añade «Añadir uno nuevo solo puede hacerlo el administrador global»). Cuál es el vigente.
- Idiomas faltantes: se marcan con borde discontinuo y badge «Falta EU», pero no se ve si bloquea publicar.
- Ficha → Puntos de interés: no hay botón «Guardar lugar» visible en esta pestaña (sí en Información); REVISAR si los cambios de ficha se guardan por pestaña.
- Ficha: marcador del mapa de Google y geocodificación («el mapa y las coordenadas se rellenan solos») sin detalle de errores.
- Escaneos («412 escaneos», «286 escaneos»): métricas visibles en el QR; no se sabe si es MVP o fase 2.
- Duración, galerías y límites: tamaños y proporciones se ven, pero no los errores de subida (tamaño, formato). Audio máximo 20 MB solo visible en Editor de contenido · Audio.
- Administradores (`165:2546`): texto completo del subtítulo (truncado «Cada a…»), rótulo del botón de cabecera y rótulo del badge de acceso (rol) de cada fila.
- Administradores · invitar (`179:999`): campos del diálogo (¿correo? ¿entidad? ¿lugares? ¿rol?), botones y validaciones.
- Administradores · confirmar borrado (`179:1341`): texto del modal y consecuencias.
- Administradores · invitación enviada (`179:1201`): texto de la tostada.
- Menú · Añadir contenido (`181:2649`): opciones exactas (¿incluye vídeo 360?).
- Editor de contenido · Texto (`182:2048`) y Audio (`182:2366`): rótulos de los dos botones de la cabecera (¿«Guardar»/«Eliminar»?). El bloque «Imagen en el texto» de Texto tiene textos que parecen copiados de la galería del lugar.
- Punto · euskera (`181:1520`): no leído.

App:
- Menú 4 se llama «Ajustes» en diseño y arquitectura, no «Cuenta». Confirmar nombre.
- Punto 2 y punto 6: los frames de 360º, Vídeos, Imágenes y Antes y después repiten contenido del punto 1.
- Botones ocultos del reproductor (Velocidad, −15 s, +15 s) y texto «Sigue sonando aunque bloquees el móvil o…»: confirmar si entran en MVP.
- Comportamientos sin confirmar: cambio de idioma dentro de un punto, destino exacto de las tarjetas de visita en Inicio, acción de «Cómo llegar», contenido de la Vista 360, zoom de Imagen, estados de error (correo, código), carga y error de red.
- Estado «Sin resultados»: texto y acciones no leídos.
- Texto de varios párrafos cortado por los metadatos (descripciones de punto, textos, «Gracias por recorrer…»).
- Tablero «Preguntas y dudas» y sección «Fase 2 · Pago»: no existen en la página `48:2`.
