import glob
import re

def contar_traduccion():
    total = 0
    traducidas = 0
    for archivo in glob.glob("files/*.rpy"):
        with open(archivo, encoding="utf-8") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if 'old "' in lines[i]:
                    total += 1
                if 'new "' in lines[i] and not lines[i].strip().endswith('new ""'):
                    traducidas += 1
                if re.match(r'^\s*#.*$', lines[i]):
                    if i+1 < len(lines):
                        linea_trad = lines[i+1].strip()
                        if linea_trad.startswith('"') or re.match(r'^\w+\s*".*"$', linea_trad):
                            total += 1
                            if linea_trad != '""' and not re.match(r'^\w+\s*""$', linea_trad):
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
        nuevo_readme = (readme[:inicio] + "<!-- PROGRESO_TRADUCCION_START -->\n" + progreso_md.replace('# Progreso de traducción\n\n', '') + "<!-- PROGRESO_TRADUCCION_END -->" + readme[fin+len("<!-- PROGRESO_TRADUCCION_END -->"):])
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(nuevo_readme)

