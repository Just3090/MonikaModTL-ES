import glob
import re

COM_ING_LINE = re.compile(r'^\s*#\s')

def _extraer_contenido(linea: str):
    """
    Devuelve el contenido dentro de las primeras comillas de la linea,
    si no encuentra comillas devuelve None.
    """
    m = re.search(r'"(.*?)"', linea)
    return m.group(1) if m else None

def contar_traduccion():
    total = 0
    traducidas = 0

    for archivo in glob.glob("files/*.rpy"):
        with open(archivo, encoding="utf-8") as f:
            prev_old_original = None
            prev_comment_original = None
            for linea in f:
                l = linea.rstrip("\n")

                # old/new strings
                if l.strip().startswith('old "') and l.strip().endswith('"'):
                    prev_old_original = _extraer_contenido(l)
                    total += 1
                    continue

                if l.strip().startswith('new "'):
                    nuevo = _extraer_contenido(l)
                    if prev_old_original is not None:
                        if nuevo and nuevo != prev_old_original:
                            traducidas += 1
                    prev_old_original = None
                    continue

                # comentario con original en ingles
                if COM_ING_LINE.match(l):
                    # extrae posible texto original del comentario
                    orig = _extraer_contenido(l)
                    if orig is not None:
                        prev_comment_original = orig
                    else:
                        prev_comment_original = None
                    continue

                # linea potencial de traducción tras comentario
                if prev_comment_original is not None:
                    # ignorar si esta linea es otro comentario o no contiene comillas
                    if not l.strip().startswith('#'):
                        trad = _extraer_contenido(l)
                        if trad is not None:
                            total += 1
                            if trad and trad != prev_comment_original:
                                traducidas += 1
                            prev_comment_original = None
                        # si no tiene comillas mantenemos el original hasta encontrar una linea válida
                    continue

    return total, traducidas

if __name__ == "__main__":
    total, traducidas = contar_traduccion()
    porcentaje = (traducidas/total*100) if total else 0
    progreso_md = f"# Progreso de traducción\n\n**{traducidas} de {total} líneas traducidas**\n\n**Progreso:** {porcentaje:.2f}%\n"
    with open("TRANSLATION_PROGRESS.md", "w", encoding="utf-8") as f:
        f.write(progreso_md)

    # Actualizar README.md entre los delimitadores
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
