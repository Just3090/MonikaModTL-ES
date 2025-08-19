import glob
import re

def _extraer_contenido(linea: str):
    m = re.search(r'"(.*?)"', linea)
    return m.group(1) if m else None

def contar_traduccion():
    total = 0
    traducidas = 0

    for archivo in glob.glob("files/*.rpy"):
        with open(archivo, encoding="utf-8") as f:
            dentro_translate = False
            original_text = None
            prev_old_original = None
            for linea in f:
                l = linea.strip()

                if l.startswith("translate spanish"):
                    dentro_translate = True
                    original_text = None
                    continue

                if dentro_translate and l == "":
                    dentro_translate = False
                    original_text = None
                    continue

                if l.startswith('old "') and l.endswith('"'):
                    prev_old_original = _extraer_contenido(l)
                    total += 1
                    continue

                if l.startswith('new "'):
                    nuevo = _extraer_contenido(l)
                    if prev_old_original is not None:
                        if nuevo and nuevo != prev_old_original:
                            traducidas += 1
                    prev_old_original = None
                    continue

                if dentro_translate:
                    if l.startswith("#"):
                        original_text = _extraer_contenido(l)
                        continue

                    if l.startswith("m") or l.startswith("extend"):
                        trad_text = _extraer_contenido(l)
                        if original_text is not None:
                            total += 1
                            if trad_text and trad_text != original_text:
                                traducidas += 1
                            original_text = None
                        elif trad_text is not None:
                            total += 1
                            if trad_text:
                                traducidas += 1
                        continue

    return total, traducidas

if __name__ == "__main__":
    total, traducidas = contar_traduccion()
    porcentaje = (traducidas/total*100) if total else 0
    progreso_md = f"# Progreso de traducción\n\n**{traducidas} de {total} líneas traducidas**\n\n**Progreso:** {porcentaje:.2f}%\n"
    with open("TRANSLATION_PROGRESS.md", "w", encoding="utf-8") as f:
        f.write(progreso_md)

    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
    inicio = readme.find("<!-- PROGRESO_TRADUCCION_START -->")
    fin = readme.find("<!-- PROGRESO_TRADUCCION_END -->")
    if inicio != -1 and fin != -1:
        nuevo_readme = (
            readme[:inicio]
            + "<!-- PROGRESO_TRADUCCION_START -->\n"
            + progreso_md.replace('# Progreso de traducción\n\n', '')
            + "<!-- PROGRESO_TRADUCCION_END -->"
            + readme[fin+len("<!-- PROGRESO_TRADUCCION_END -->"):]
        )
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(nuevo_readme)