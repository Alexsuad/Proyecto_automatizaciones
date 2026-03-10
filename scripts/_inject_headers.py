import sys, re
from pathlib import Path

bloque_path = Path(sys.argv[1])
header = """
**Opción activa:** TRANSPORTE  
**Subnicho:** Pyme transportista 10–50 camiones (Zaragoza/Aragón)  
**Dolor:** Viaje → Evidencia (POD/CMR/albarán) → Factura → Cobro (Doc-to-Cash)
"""

for filepath in bloque_path.glob("*.md"):
    if not filepath.is_file():
        continue
    text = filepath.read_text(encoding="utf-8")
    # Ignoramos si ya está la cabecera
    if "Opción activa:" in text:
        continue

    # Insertar justo después del primer '# Título'
    match = re.search(r"^# .+$", text, flags=re.MULTILINE)
    if match:
        insert_pos = match.end()
        new_text = text[:insert_pos] + "\n\n" + header.strip() + "\n" + text[insert_pos:]
        filepath.write_text(new_text, encoding="utf-8")
        print(f"✅ Inyectada cabecera en: {filepath.name}")
    else:
        print(f"⚠️ No hay titulo H1 en: {filepath.name}")
