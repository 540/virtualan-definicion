#!/usr/bin/env python3
"""Genera estrategia/user-story-mapping.html a partir de estrategia/user-story-mapping.md.

Uso, desde la raíz del repo:  python3 herramientas/generar-tablero.py [--salida RUTA]

Lee:  estrategia/user-story-mapping.md, estrategia/capturas/frames.json, herramientas/tablero-plantilla.html
Solo biblioteca estándar.
"""
import argparse
import datetime
import html
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MD = RAIZ / "estrategia" / "user-story-mapping.md"
FRAMES = RAIZ / "estrategia" / "capturas" / "frames.json"
PLANTILLA = RAIZ / "herramientas" / "tablero-plantilla.html"
SALIDA = RAIZ / "estrategia" / "user-story-mapping.html"

COLUMNAS = ["Historia", "Corte", "Pantallas", "Caso", "Figma", "REVISAR"]
VACIO = "—"


def fallo(msg):
    sys.exit("ERROR: " + msg)


def aviso(msg):
    print("AVISO: " + msg, file=sys.stderr)


# ---------- texto ----------

def esc(t):
    return html.escape(t, quote=False)


def inline_html(t):
    """Escapa HTML y convierte `código` y **negrita** en etiquetas."""
    t = esc(t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return t


def json_script(datos):
    return json.dumps(datos, ensure_ascii=False).replace("</", "<\\/")


# ---------- markdown ----------

def secciones(lineas, nivel):
    """Divide en {titulo: [lineas]} por encabezados del nivel dado (## o ###), en orden."""
    marca = "#" * nivel + " "
    res, actual = [], None
    for l in lineas:
        if l.startswith(marca):
            actual = (l[len(marca):].strip(), [])
            res.append(actual)
        elif actual is not None:
            actual[1].append(l)
    return res


def buscar(secs, prefijo, donde):
    for t, cuerpo in secs:
        if t.startswith(prefijo):
            return t, cuerpo
    fallo(f"falta la sección «{prefijo}» en {donde}.")


def celdas(linea):
    return [c.strip() for c in linea.strip().strip("|").split("|")]


def tabla(cuerpo, cabecera_esperada, donde):
    """Devuelve las filas (listas de celdas) de la primera tabla del cuerpo."""
    filas, dentro = [], False
    for l in cuerpo:
        if l.lstrip().startswith("|"):
            c = celdas(l)
            if not dentro:
                if c != cabecera_esperada:
                    fallo(f"{donde}: la cabecera de la tabla debe ser {' | '.join(cabecera_esperada)}; hay {' | '.join(c)}.")
                dentro = True
            elif all(re.fullmatch(r":?-{3,}:?", x) for x in c):
                continue
            else:
                if len(c) != len(cabecera_esperada):
                    fallo(f"{donde}: fila con {len(c)} celdas, se esperaban {len(cabecera_esperada)}: {l.strip()[:80]}")
                filas.append(c)
        elif dentro:
            break
    if not dentro:
        fallo(f"{donde}: no hay tabla.")
    return filas


def parrafos(cuerpo):
    """Párrafos de texto (sin tablas ni listas), unidos por línea en blanco."""
    res, cur = [], []
    for l in cuerpo + [""]:
        if l.strip() and not l.lstrip().startswith("|") and not re.match(r"\s*\d+\.\s", l):
            cur.append(l.strip())
        elif cur:
            res.append(" ".join(cur)); cur = []
    return res


def lista_numerada(cuerpo):
    return [re.sub(r"^\s*\d+\.\s*", "", l).strip() for l in cuerpo if re.match(r"\s*\d+\.\s", l)]


def parsear(texto):
    lineas = texto.split("\n")
    if not lineas or not lineas[0].startswith("# "):
        fallo("la primera línea de user-story-mapping.md debe ser el título «# ...».")
    titulo = lineas[0][2:].strip()
    h2 = secciones(lineas, 2)
    intro = []
    for l in lineas[1:]:
        if l.startswith("## "):
            break
        intro.append(l)
    intro_p = parrafos(intro)
    m = re.search(r"(\d{4}-\d{2}-\d{2})", intro_p[0]) if intro_p else None
    if not m:
        fallo("el párrafo de estado bajo el título debe incluir una fecha ISO (p. ej. «Borrador del 2026-10-27»).")
    fecha = m.group(1)

    # Cortes
    _, cu = buscar(h2, "Cortes", "user-story-mapping.md")
    cortes = []
    for c in tabla(cu, ["Corte", "Nombre", "Qué demuestra", "Criterio de hecho"], "Cortes"):
        if not c[0].isdigit():
            fallo(f"Cortes: el id de corte debe ser un número, hay «{c[0]}».")
        nombre = c[1]
        val = re.search(r"\*\*validado el (\d{4}-\d{2}-\d{2})\*\*", nombre)
        nombre = re.sub(r"\s*·?\s*\*\*validado el [^*]*\*\*", "", nombre).strip()
        corte = {"id": int(c[0]), "nombre": nombre}
        if val:
            corte["validado"] = val.group(1)
        cortes.append(corte)
    if not cortes:
        fallo("la tabla de Cortes está vacía.")
    ids_corte = {c["id"] for c in cortes}

    # Mapas
    actividades, historias = [], []
    for prefijo in ("Mapa · Panel", "Mapa · App"):
        t, cuerpo = buscar(h2, prefijo, "user-story-mapping.md")
        for t3, c3 in secciones(cuerpo, 3):
            m = re.fullmatch(r"([PV]\d+) · (.+)", t3)
            if not m:
                fallo(f"encabezado de actividad no válido: «### {t3}» (esperado «### P1 · Nombre» o «### V1 · Nombre»).")
            cod, nombre = m.groups()
            producto = "panel" if cod.startswith("P") else "app"
            actividades.append({"codigo": cod, "nombre": nombre, "producto": producto})
            for i, f in enumerate(tabla(c3, COLUMNAS, t3), 1):
                hist, corte, pant, caso, figma, rev = f
                if corte == VACIO or corte == "":
                    corte_v = None
                elif corte.isdigit() and int(corte) in ids_corte:
                    corte_v = int(corte)
                else:
                    fallo(f"{cod}-{i}: corte «{corte}» no existe en la tabla de Cortes.")
                caso_v = None if caso in (VACIO, "") else caso.strip("`")
                ids = [] if figma in (VACIO, "") else [x.strip() for x in figma.split(",") if x.strip()]
                historias.append({
                    "id": f"{cod}-{i}", "actividad": cod, "historia": hist, "corte": corte_v,
                    "pantallas": pant, "caso": caso_v,
                    "revisar": "" if rev == VACIO else rev, "frames": ids,
                })
    if not actividades:
        fallo("no hay actividades (### P1 · ... / ### V1 · ...).")

    # Walking skeleton
    _, sk = buscar(h2, "Walking skeleton", "user-story-mapping.md")
    pasos = lista_numerada(sk)
    ps = parrafos(sk)
    if not pasos or len(ps) < 2:
        fallo("«Walking skeleton» debe tener un párrafo de validación, una lista numerada y un párrafo «Lo que queda fuera…».")

    # Decisiones
    _, de = buscar(h2, "Decisiones pendientes", "user-story-mapping.md")
    decisiones = tabla(de, ["Decisión", "Quién", "Afecta a"], "Decisiones pendientes")

    # Fase 2
    _, f2 = buscar(h2, "Fuera de alcance", "user-story-mapping.md")
    pf2 = parrafos(f2)
    if not pf2:
        fallo("«Fuera de alcance (fase 2)» no tiene párrafo.")

    return {
        "titulo": titulo, "fecha": fecha, "meta": intro_p[0], "cortes": cortes, "actividades": actividades,
        "historias": historias, "sk_nota": ps[0], "sk_pasos": pasos, "sk_fuera": ps[-1],
        "decisiones": decisiones, "fase2": pf2[0],
    }


# ---------- generación ----------

def main():
    ap = argparse.ArgumentParser(description="Genera el tablero HTML del User Story Mapping desde el markdown.")
    ap.add_argument("--salida", default=str(SALIDA), help="ruta del HTML de salida (por defecto estrategia/user-story-mapping.html)")
    args = ap.parse_args()

    for p in (MD, FRAMES, PLANTILLA):
        if not p.exists():
            fallo(f"no existe {p}.")
    d = parsear(MD.read_text(encoding="utf-8"))
    frames = json.loads(FRAMES.read_text(encoding="utf-8"))
    catalogo = {f["id"] for f in frames}

    for h in d["historias"]:
        for fid in h["frames"]:
            if fid not in catalogo:
                fallo(f"{h['id']} («{h['historia']}»): el frame {fid} no está en estrategia/capturas/frames.json.")
    for f in frames:
        if not (RAIZ / "estrategia" / "capturas" / f"{f['id']}.jpg").exists():
            aviso(f"falta estrategia/capturas/{f['id']}.jpg ({f['nombre']}).")

    hoy = datetime.date.today().isoformat()
    validados = [c["id"] for c in d["cortes"] if "validado" in c]
    meta = f'<time datetime="{d["fecha"]}">{d["fecha"]}</time>'
    if validados:
        meta += " · " + ("Corte " + ", ".join(map(str, validados)) + " validado" if len(validados) == 1
                         else "Cortes " + ", ".join(map(str, validados)) + " validados")
        meta += " · resto en borrador para validar con el equipo"
    m_bb0 = re.search(r"backbone[^.]*validad[oa] el (\d{4}-\d{2}-\d{2})", d["meta"], re.I)
    if m_bb0:
        meta += f" · backbone (actividades) validado el {m_bb0.group(1)}"

    cortes_js = ",\n".join(
        "    { id: %d, nombre: %s%s }" % (
            c["id"], json.dumps(c["nombre"], ensure_ascii=False),
            ", validado: " + json.dumps(c["validado"]) if "validado" in c else "")
        for c in d["cortes"])
    opciones = "\n".join(
        '      <option value="%d">%d · %s%s</option>' % (
            c["id"], c["id"], esc(c["nombre"]), " (validado)" if "validado" in c else "")
        for c in d["cortes"])
    pasos = "\n".join(f"    <li>{inline_html(p)}</li>" for p in d["sk_pasos"])
    decis = "\n".join(
        "      <tr>" + "".join(f"<td>{inline_html(c)}</td>" for c in f) + "</tr>" for f in d["decisiones"])
    pie = ("Fuentes: <code>diseno/mapa-de-pantallas.md</code> y <code>contexto.md</code>. La extracción del Figma fue parcial: "
           "varios frames se leyeron solo por estructura y el panel actual no se pudo revisar. "
           f"Generado el {hoy} desde <code>estrategia/user-story-mapping.md</code>.")
    nota = d["sk_nota"]

    m_bb = re.search(r"backbone[^.]*validad[oa] el (\d{4}-\d{2}-\d{2})", d["meta"], re.I)
    backbone = json.dumps(m_bb.group(1) if m_bb else None)
    marcas = {
        "BACKBONE": backbone,
        "HISTORIAS": json_script(d["historias"]),
        "ACTIVIDADES": json_script(d["actividades"]),
        "FRAMES": json_script(frames),
        "CORTES": cortes_js,
        "META": meta,
        "OPCIONES_CORTES": opciones,
        "SKELETON_NOTA": inline_html(nota),
        "SKELETON_PASOS": pasos,
        "SKELETON_FUERA": inline_html(d["sk_fuera"]),
        "DECISIONES": decis,
        "FASE2": inline_html(d["fase2"]),
        "PIE": pie,
    }
    out = PLANTILLA.read_text(encoding="utf-8")
    for k, v in marcas.items():
        marca = "{{%s}}" % k
        if out.count(marca) != 1:
            fallo(f"la plantilla debe contener {marca} exactamente una vez.")
        out = out.replace(marca, v)
    resto = re.findall(r"\{\{[A-Z_]+\}\}", out)
    if resto:
        fallo(f"marcadores sin sustituir: {resto}")

    destino = Path(args.salida)
    destino.write_text(out, encoding="utf-8")
    print(f"Escrito {destino}: {len(d['historias'])} historias, {len(d['actividades'])} actividades, {len(frames)} frames.")


if __name__ == "__main__":
    main()
