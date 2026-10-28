# User Story Mapping · CulturApp MVP

Borrador del 2026-10-27. El corte 0 (walking skeleton) está validado por Iker Mariñelarena el 2026-10-27 y el backbone (usuarios y actividades) está validado el 2026-10-28; las historias de los cortes 1 a 4 están pendientes de validar con Marta y Olaia. Fuentes: `diseno/mapa-de-pantallas.md` (extracción del Figma del mismo día, parcial), `contexto.md` (decisiones del 28 de septiembre al 26 de octubre). El panel actual no se ha podido revisar: pide credenciales.

Este mapa sirve para dos cosas: ver de un vistazo qué hace cada usuario y decidir en qué orden se construye. Cada historia tiene un corte (entregable) y un caso (`casos/<slug>.md`) donde se definirá el detalle.

## Cómo leer el mapa

- **Usuario**: quién hace la actividad.
- **Actividad**: columna del mapa, en orden narrativo (lo que hace la persona de principio a fin).
- **Historia**: una fila bajo la actividad. Una historia cabe en un caso; un caso puede agrupar varias historias de la misma actividad.
- **Corte**: entregable al que pertenece. Los cortes son acumulativos: el 1 incluye el 0.
- **REVISAR**: lo que ni el diseño ni las decisiones resuelven. Con la fuente que falta.

## Usuarios

| Usuario | Quién es | Producto |
|---|---|---|
| Administrador de entidad | Persona del ayuntamiento, museo o fundación que da de alta su lugar, sus puntos y sus contenidos, y coloca los carteles con QR. | Panel |
| Administrador global | Virtualan. Ve todas las entidades, invita administradores y es el único que puede añadir idiomas nuevos. El resto de diferencias de permisos está `REVISAR` (no se ven en el diseño). | Panel |
| Visitante | Persona que escanea un cartel o entra en la web y recorre la visita en su móvil, sin descargar nada. | App |

## Cortes (entregables)

| Corte | Nombre | Qué demuestra | Criterio de hecho |
|---|---|---|---|
| 0 | Walking skeleton · **validado el 2026-10-27** | Que la cadena entera funciona de punta a punta con lo mínimo: un administrador entra, crea un lugar con un punto y un texto, publica, se le asocia el QR creado fuera, y un visitante escanea ese QR, entra en el punto y lee el texto. | Hecho con un dato real en cada eslabón, desplegado en un entorno accesible desde un móvil. Sin diseño final: componentes base del design system, sin estados de error ni idiomas; el QR viene de fuera, no lo genera el panel. |
| 1 | Visita completa en castellano | Una entidad puede montar y publicar una visita completa en un idioma, y el visitante la recorre entera con todos los tipos de contenido. Es la primera demo creíble para Iker Ibero. | Un lugar real con sus puntos, todos los tipos de contenido y los QR impresos funcionando. Pantallas al diseño de Figma. |
| 2 | Multiidioma | La visita existe en varios idiomas y el visitante cambia de idioma en cualquier momento. | Lugar con ES y EU completos, idioma predeterminado, avisos de idioma incompleto en el panel, cambio de idioma en la app sin perder el sitio. |
| 3 | Entidades y administradores | Varias entidades conviven en el mismo panel, cada una con sus administradores, y el visitante sabe quién está detrás de la visita. | Administrador global invita a una entidad, esta entra y solo ve lo suyo. «Sobre la entidad» y textos legales en la app. |
| 4 | Descubrimiento y cuenta | El visitante que no viene por QR encuentra visitas, y puede identificarse. | Inicio y Explorar con buscador. Entrar con correo y código, y con Google. |

El orden de los cortes 3 y 4 es una decisión de alcance y plazos (Pablo, Marta): se proponen así porque el 3 desbloquea a las entidades para cargar contenido en paralelo al desarrollo del 4.

Lo transversal que no es una historia pero condiciona el corte 0: elección del backend, modelo de datos (entidad, lugar, punto, contenido, idioma, administrador), despliegue del panel (react-native-web) y de la app (web móvil), y la migración de datos del panel actual (`REVISAR`: no hay decisión sobre si se migran los lugares existentes y los QR impresos con QR Kit; pregunta abierta para Virtualan).

## Mapa · Panel (administrador)

### P1 · Entrar en el panel

| Historia | Corte | Pantallas | Caso | Figma | REVISAR |
|---|---|---|---|---|---|
| Entrar con correo y contraseña | 0 | Acceso | `entrar-en-el-panel` | 165-3514 | — |
| Ver el error de contraseña incorrecta | 1 | Acceso · contraseña incorrecta | `entrar-en-el-panel` | 177-863 | — |
| Recordar la sesión («Recordarme») | 1 | Acceso | `entrar-en-el-panel` | 165-3514 | Duración de la sesión: no está en el diseño. |
| Recuperar la contraseña | 3 | Sin frame | `entrar-en-el-panel` | — | No hay pantalla en Figma. Pedir a Olaia o definir solo por correo. |
| Cerrar sesión | 1 | Sin frame (menú de usuario del lateral) | `entrar-en-el-panel` | — | El chevron del usuario no tiene menú diseñado. |

### P2 · Ver mis lugares

Es la pantalla de entrada tras el acceso y el punto al que se vuelve siempre: desde aquí se ve el estado de cada lugar y se entra a editarlo.

| Historia | Corte | Pantallas | Caso | Figma | REVISAR |
|---|---|---|---|---|---|
| Ver la lista de lugares con su nombre y número de puntos | 0 | Lista de lugares | `lista-de-lugares` | 165-2229 | — |
| Ver la entidad de cada lugar en la lista | 3 | Lista de lugares | `lista-de-lugares` | 165-2229 | Decisión del 26 de octubre. ¿Qué ve un administrador de entidad: solo sus lugares? |
| Paginar la lista | 1 | Lista de lugares | `lista-de-lugares` | 165-2229 | — |
| Abrir la ficha de un lugar desde la lista | 0 | Lista de lugares, Lugares · acciones | `lista-de-lugares` | 165-2229, 184-2201 | — |

### P3 · Crear el lugar

| Historia | Corte | Pantallas | Caso | Figma | REVISAR |
|---|---|---|---|---|---|
| Crear un lugar con nombre y presentación, y guardarlo | 0 | Nuevo lugar, Ficha · Información | `crear-lugar` | 180-1542, 165-2862 | — |
| Rellenar la ubicación (dirección, municipio, provincia, marcador en el mapa) | 1 | Nuevo lugar, Ficha · Información | `editar-informacion-del-lugar` | 180-1542, 165-2862 | Geocodificación automática y sus errores: no están en el diseño. |
| Subir las imágenes del lugar (portada, tarjeta, fondo de bienvenida, logo de la entidad, galería hasta 6) | 1 | Ficha · Información | `editar-informacion-del-lugar` | 165-2862 | Logo de la entidad: pregunta abierta de Iker Ibero del 22 de octubre. Errores de tamaño y formato sin diseñar. |
| Subir el audio de bienvenida | 1 | Ficha · Información | `editar-informacion-del-lugar` | 165-2862 | — |

### P4 · Configurar los idiomas del lugar

| Historia | Corte | Pantallas | Caso | Figma | REVISAR |
|---|---|---|---|---|---|
| Guardar todo en castellano por defecto: el lugar nace con ES como único idioma y predeterminado | 0 | Nuevo lugar | `configurar-idiomas-del-lugar` | 180-1542 | — |
| Marcar los idiomas disponibles del lugar (ES · EU · EN · FR · CA · GL) | 2 | Ficha · Información | `configurar-idiomas-del-lugar` | 165-2862 | — |
| Elegir el idioma predeterminado | 2 | Ficha · Información | `configurar-idiomas-del-lugar` | 165-2862 | Decisión del 26 de octubre: ningún idioma obligatorio, hay predeterminado. |
| Cambiar de idioma con los chips y rellenar los textos de cada idioma | 2 | Ficha · Información · euskera, Punto · euskera | `configurar-idiomas-del-lugar` | 180-1247, 181-1520 | — |
| Ver qué idioma falta en cada lugar, punto y contenido («Falta EU», chip discontinuo) | 2 | Lista de lugares, Puntos del lugar, Punto | `configurar-idiomas-del-lugar` | 165-2229, 165-2990, 165-3297 | ¿Un idioma incompleto bloquea publicar? |
| Añadir un idioma nuevo al sistema (solo administrador global) | 3 | Sin frame («Añadir idioma») | `configurar-idiomas-del-lugar` | — | No hay pantalla. El texto de la tarjeta difiere entre las dos variantes de la ficha. |

### P5 · Ver los puntos del lugar

Pestaña «Puntos de interés» de la ficha. Es el centro desde el que se abre, se añade y se ordena cada punto, igual que la lista de lugares para el panel.

| Historia | Corte | Pantallas | Caso | Figma | REVISAR |
|---|---|---|---|---|---|
| Ver los puntos del lugar, en el orden en que se crearon, y abrir uno | 0 | Puntos del lugar | `puntos-del-lugar` | 165-2990 | — |
| Ver en cada punto su duración y cuántos contenidos tiene de cada tipo | 1 | Puntos del lugar | `puntos-del-lugar` | 165-2990 | Los chips de idioma y «Falta EU» llegan con la historia del corte 2. |
| Cambiar el orden de los puntos (flechas) | 1 | Puntos del lugar | `ordenar-puntos` | 165-2990 | Solo flechas, sin arrastrar. |
| Ver el estado vacío cuando el lugar aún no tiene puntos | 1 | Nuevo lugar (pestaña «Puntos de interés 0») | `puntos-del-lugar` | 180-1542 | No hay frame del estado vacío de la pestaña. |

### P6 · Añadir puntos de interés

| Historia | Corte | Pantallas | Caso | Figma | REVISAR |
|---|---|---|---|---|---|
| Crear un punto con título y guardarlo | 0 | Nuevo punto | `anadir-punto-de-interes` | 181-1862 | — |
| Rellenar duración, descripción breve, imagen principal y galería (hasta 8) | 1 | Punto | `editar-punto-de-interes` | 165-3297 | — |
| Borrar un punto | 1 | Sin frame (menú ··· del punto) | `borrar-punto` | — | No hay modal diseñado. ¿Aviso de que su QR deja de funcionar, como en borrar lugar? |

### P7 · Cargar contenidos en un punto

| Historia | Corte | Pantallas | Caso | Figma | REVISAR |
|---|---|---|---|---|---|
| Añadir un texto (título y texto) | 0 | Punto · añadir contenido, Editor · Texto | `anadir-contenido-de-texto` | 181-2313, 182-2048 | — |
| Añadir una imagen opcional entre el título y el texto | 1 | Editor · Texto | `anadir-contenido-de-texto` | 182-2048 | Decisión del 26 de octubre. Rótulo del botón de la galería intermedia sin leer. |
| Añadir un audio (MP3 hasta 20 MB, uno por idioma) | 1 | Editor · Audio | `anadir-contenido-de-audio` | 182-2366 | — |
| Añadir un vídeo | 1 | Sin frame | `anadir-contenido-de-video` | — | No hay editor diseñado. Formato, tamaño, ¿subida o enlace? |
| Añadir una imagen con descripción y audio de explicación | 1 | Sin frame | `anadir-contenido-de-imagen` | — | No hay editor diseñado. La app muestra imagen con audio de 0:58. |
| Añadir un antes y después (dos imágenes) | 1 | Sin frame | `anadir-contenido-antes-y-despues` | — | No hay editor diseñado. |
| Añadir una imagen o vídeo 360 | 1 | Sin frame | `anadir-contenido-360` | — | Kick off: 360 priorizado. No hay editor y la app tiene el frame de Vista 360 vacío. Confirmar que entra en el MVP. |
| Editar un contenido existente (lápiz) | 1 | Editores | `editar-y-borrar-contenido` | 182-2048, 182-2366 | — |
| Borrar un contenido (menú ···) | 1 | Sin frame | `editar-y-borrar-contenido` | — | No hay modal diseñado. |
| Dar a un contenido su propio QR | — | Sin frame | — | — | El diseño menciona «Sin código QR propio» en los contenidos, pero el aterrizaje decidió «un QR por destino» (lugar y punto). Confirmar si es fase 2 o texto obsoleto. |

### P8 · Preparar los QR

| Historia | Corte | Pantallas | Caso | Figma | REVISAR |
|---|---|---|---|---|---|
| Asociar a cada lugar el QR creado fuera (QR Kit) de la forma más sencilla, aunque sea directamente en base de datos, para que se entre al lugar desde la app | 0 | — | `asociar-qr-externo` | — | — |
| Obtener el QR del lugar al guardarlo y descargarlo para el cartel | 2 | Ficha · Información (tarjeta QR) | `descargar-qr` | 165-2862 | Formato de descarga (PNG, SVG, PDF) y tamaño: sin diseño. |
| Obtener el QR del punto al guardarlo y descargarlo | 3 | Punto (tarjeta QR) | `descargar-qr` | 165-3297 | — |
| Copiar el enlace del QR | 1 | Ficha · Información, Punto | `descargar-qr` | 165-2862, 165-3297 | — |
| Mostrar el QR desde la lista de lugares y desde la lista de puntos | 1 | Lista de lugares, Puntos del lugar | `descargar-qr` | 165-2229, 165-2990 | Destino de «Mostrar código» sin diseñar (¿modal?). |
| Que la URL del QR no cambie al editar el lugar o el punto | 1 | — | `descargar-qr` | — | Dolor de partida número uno. Criterio técnico, no de pantalla. |
| Ver cuántas veces se ha escaneado cada QR | 3 | Tarjetas QR («412 escaneos») | `descargar-qr` | 165-2862, 165-3297 | Hoy solo se registra el primer escaneo. Pregunta abierta para Virtualan. ¿MVP o fase 2? |
| Migrar los QR ya impresos con QR Kit | — | — | — | — | Pregunta abierta para Virtualan. Sin decisión. |

### P9 · Publicar y mantener el lugar

| Historia | Corte | Pantallas | Caso | Figma | REVISAR |
|---|---|---|---|---|---|
| Publicar el lugar en la app (interruptor) | 0 | Ficha, Lista de lugares | `publicar-lugar` | 165-2862, 165-2229 | — |
| Ver el estado Publicado o Borrador en la ficha y en la lista | 1 | Ficha, Lista de lugares | `publicar-lugar` | 165-2862, 165-2229 | — |
| Despublicar un lugar (vuelve a borrador) | 3 | Ficha | `publicar-lugar` | 165-2862 | ¿Qué ve el visitante que abre un QR de un lugar en borrador? |
| Editar un lugar ya creado | 1 | Lugares · acciones, Ficha | `editar-informacion-del-lugar` | 184-2201, 165-2862 | — |
| Borrar un lugar con confirmación y deshacer | 1 | Lugares · confirmar borrado, Lugares · lugar borrado | `borrar-lugar` | 170-752, 177-960 | Plazo del «Deshacer» y si el borrado es real o diferido (papelera es fase 2). |

### P10 · Gestionar quién entra

| Historia | Corte | Pantallas | Caso | Figma | REVISAR |
|---|---|---|---|---|---|
| Ver quién tiene acceso, con su entidad y sus lugares | 3 | Administradores | `ver-administradores` | 165-2546 | Frame leído solo por estructura: rótulo del rol y del botón de cabecera. |
| Invitar a un administrador por correo | 3 | Administradores · invitar | `invitar-administrador` | 179-999 | Campos del diálogo (¿entidad? ¿lugares? ¿rol?) sin leer. Correo de invitación y alta del invitado sin diseñar. |
| Ver la invitación pendiente y cancelarla | 3 | Administradores · invitación enviada | `invitar-administrador` | 179-1201 | Texto de la tostada. |
| Quitar el acceso a un administrador | 3 | Administradores · confirmar borrado | `quitar-acceso` | 179-1341 | Texto del modal. |
| Permisos: qué puede hacer el administrador de entidad frente al global | 3 | — | `ver-administradores` | — | Solo se ve «Añadir idioma» y «Entidad: Todas». Dolor de partida: los subadministradores no tienen gestión clara. |

## Mapa · App (visitante)

### V1 · Llegar a la visita

| Historia | Corte | Pantallas | Caso | Figma | REVISAR |
|---|---|---|---|---|---|
| Abrir el QR del lugar y ver la portada | 0 | Bienvenida, Portada del lugar | `llegar-por-qr` | 50-2, 227-905 | — |
| Abrir el QR de un punto y caer directamente en ese punto | 3 | Punto de interés | `llegar-por-qr` | 53-53 | Depende del QR del punto (corte 3). ¿Pasa por Bienvenida o va directo? |
| Elegir idioma en la bienvenida | 2 | Bienvenida, Cambiar idioma | `llegar-por-qr` | 50-2, 61-116 | Cambiar idioma: frame sin capas. |
| Abrir un QR de un lugar en borrador o borrado | 1 | Sin frame | `llegar-por-qr` | — | Sin diseño de error. |
| Abrir la app sin QR y ver el inicio | 4 | Inicio | `abrir-la-app-sin-qr` | 330-621 | Destino exacto de las tarjetas de visita. |

### V2 · Explorar visitas

| Historia | Corte | Pantallas | Caso | Figma | REVISAR |
|---|---|---|---|---|---|
| Ver todas las visitas publicadas | 4 | Explorar visitas | `explorar-visitas` | 311-493 | — |
| Buscar por nombre o municipio y ver resultados | 4 | Explorar · resultados | `explorar-visitas` | 356-976 | Campos por los que busca. |
| No encontrar nada | 4 | Explorar · sin resultados | `explorar-visitas` | 356-1011 | Texto y acciones del estado vacío sin leer. |

### V3 · Recorrer la visita

| Historia | Corte | Pantallas | Caso | Figma | REVISAR |
|---|---|---|---|---|---|
| Ver la portada: presentación, datos, galería y lista de puntos | 1 | Portada del lugar | `ver-portada-del-lugar` | 227-905 | «Mapa de la visita» está en la arquitectura sin frame. |
| Ir al lugar («Cómo llegar») | 1 | Portada del lugar | `ver-portada-del-lugar` | 227-905 | Acción sin confirmar (¿abre mapas?). |
| Escuchar el audio de bienvenida | 1 | Bienvenida o Portada | `ver-portada-del-lugar` | 50-2, 227-905 | Dónde suena: sin diseño. |
| Abrir un punto y ver sus contenidos por pestañas | 0 | Punto de interés | `recorrer-los-puntos` | 53-53, 454-5329, 454-5446, 516-1056, 516-1101, 516-1146 | — |
| Pasar al punto siguiente o anterior | 1 | Punto de interés | `recorrer-los-puntos` | 53-53 | Decisión del 26 de octubre: «Siguiente punto» como botón. |
| Terminar la visita y ver el cierre | 1 | Punto 6, Fin de la visita | `recorrer-los-puntos` | 526-1398, 63-339 | — |

### V4 · Consumir contenidos

| Historia | Corte | Pantallas | Caso | Figma | REVISAR |
|---|---|---|---|---|---|
| Leer un texto y pasar al siguiente | 0 | Texto | `leer-texto` | 54-104, 535-2269, 535-2284, 535-2299 | — |
| Escuchar un audio con reproductor (progreso, anterior, siguiente) | 1 | Audio · Reproductor | `escuchar-audio` | 54-72, 535-2215 | Velocidad, −15 s, +15 s y «sigue sonando con el móvil bloqueado» están ocultos en el diseño: ¿MVP? |
| Ver un vídeo | 1 | Vídeo | `ver-video` | 63-254 | Controles del reproductor sin leer. Alerta oculta. |
| Ver una imagen con su descripción y audio | 1 | Imagen | `ver-imagen` | 63-312 | Zoom sin confirmar. |
| Comparar antes y después con el tirador, y a pantalla completa | 1 | Antes y después, Antes y después · horizontal | `comparar-antes-y-despues` | 54-140, 454-5288 | ¿Se entra con el botón o al girar el móvil? |
| Mirar una vista 360 | 1 | Vista 360 | `ver-vista-360` | 63-289 | Frame vacío. Confirmar alcance. |

### V5 · Cambiar de idioma

| Historia | Corte | Pantallas | Caso | Figma | REVISAR |
|---|---|---|---|---|---|
| Cambiar el idioma desde el botón fijo «Idioma» sin perder el sitio | 2 | Botón Idioma (Portada, reproductor), Cambiar idioma | `cambiar-idioma-de-la-visita` | 227-905, 54-72, 61-116 | Decisión del 26 de octubre: idioma siempre a la vista. ¿Está en el punto y en los contenidos? |
| Saber que un contenido no está en mi idioma | 2 | Alerta oculta de Vídeo y Portada | `cambiar-idioma-de-la-visita` | 227-905, 63-254 | Mensajes sin leer. |
| Cambiar el idioma desde Ajustes | 2 | «Idioma de la visita» (sin frame) | `cambiar-idioma-de-la-visita` | — | Probablemente la misma hoja que Cambiar idioma. |

### V6 · Cuenta y entidad

| Historia | Corte | Pantallas | Caso | Figma | REVISAR |
|---|---|---|---|---|---|
| Ver quién está detrás de la visita (entidad, web, teléfono, horario) | 3 | Sobre la entidad | `sobre-la-entidad` | 66-397 | Logo de la entidad: pregunta abierta. |
| Leer aviso legal, privacidad y declaración de accesibilidad | 3 | Sin frames | `sobre-la-entidad` | — | Textos sin diseñar. Accesibilidad EN 301 549: pregunta abierta. |
| Entrar con correo y código de 6 cifras | 4 | Entrar con correo, Código de verificación | `entrar-con-cuenta` | 309-16968, 309-16990 | Errores de correo y código sin diseñar. La casilla dice «condiciones de compra»: texto heredado del pago. |
| Entrar con Google | 4 | Entrar con correo | `entrar-con-cuenta` | 309-16968 | — |
| Ver mis ajustes con sesión iniciada y cerrar sesión | 4 | Ajustes · con cuenta | `entrar-con-cuenta` | 350-993 | Frame sin capas. No hay Ajustes sin cuenta. Qué aporta la cuenta en el MVP («Entra para guardar tu visita») no está decidido: sin pago, su valor es dudoso. |

## Walking skeleton · recorrido exacto

Validado el 2026-10-27 (Iker Mariñelarena). Las 13 historias del corte 0 quedan cerradas; cualquier cambio se anota con fecha.

1. Administrador entra en el panel con correo y contraseña.
2. Pulsa «Crear lugar», escribe el nombre en castellano, guarda. Se crea la URL del QR del lugar.
3. Entra en «Puntos de interés», pulsa «Añadir punto de interés», escribe el título, guarda. Se crea la URL del QR del punto.
4. Pulsa «Añadir contenido», elige texto, escribe título y texto, guarda.
5. Activa «Publicado en la app».
6. Se asocia al lugar el QR creado fuera con QR Kit, por la vía más sencilla (en base de datos si hace falta).
7. Visitante escanea el QR del lugar con el móvil, entra en el punto y lee el texto.

Lo que queda fuera a propósito del corte 0: generar QR desde el panel (el del lugar viene de QR Kit), imágenes, idiomas (todo se guarda en castellano por defecto), audio, estados de error, lista de administradores, diseño final.

## Decisiones pendientes para cerrar el mapa

| Decisión | Quién | Afecta a |
|---|---|---|
| Backend: nuevo o sobre el actual; migración de datos existentes | Marta | Corte 0 |
| Alcance del 360 en el MVP (editor en panel y visor en app) | Iker Ibero, Olaia | P7, V4 |
| Editores de vídeo, imagen y antes y después: ¿se diseñan o se derivan del de texto y audio? | Olaia | P7 |
| Qué aporta la cuenta del visitante sin pago | Iker Ibero, Pablo | V6, corte 4 |
| Registro de cada escaneo: ¿MVP? | Iker Ibero | P8 |
| Requisitos para publicar un lugar | Iker Ibero | P9 |
| Orden de los cortes 3 y 4 | Pablo, Marta | Plan |
| Pantallas que faltan en Figma: recuperar contraseña, menú de usuario, borrar punto y contenido, mostrar QR desde listas, añadir idioma, Bienvenida, Vista 360, Ajustes | Olaia | Varios |

## Fuera de alcance (fase 2)

Pago de visitas y acceso temporal a audioguías, escanear QR desde la app, ventas, papelera, usuarios y buscador del panel, precio, 3D y realidad aumentada. Rastros en el diseño: candado y leyenda «Todas son gratuitas» en Explorar, «condiciones de compra» en el acceso, columna Entidad como multi-entidad completa.
