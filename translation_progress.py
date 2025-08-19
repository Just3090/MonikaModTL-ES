import glob
import re

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
            lines = f.readlines()
            for i, linea in enumerate(lines):
                l = linea.strip()

                # old/new strings
                if l.startswith('old "') and l.endswith('"'):
                    total += 1
                    continue
                if l.startswith('new "'):
                    # contar como traducidas solo si el contenido no esta vacio
                    contenido = _extraer_contenido(l)
                    if contenido is not None:
                        if contenido != "":
                            traducidas += 1
                        # el total ya se conto con 'old', asi que no sumamos
                    continue

                # comentario con el texto original del ingles
                if re.match(r'^\s*#\s', linea):
                    if i + 1 < len(lines):
                        siguiente = lines[i+1].strip()
                        # la linea siguiente deberia (si, deberia XD) ser una linea traducible
                        if siguiente and not siguiente.startswith('#'):
                            contenido = _extraer_contenido(siguiente)
                            if contenido is not None:
                                total += 1
                                if contenido != "":
                                    traducidas += 1
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
