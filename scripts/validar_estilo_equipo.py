import argparse
import re
from pathlib import Path
from typing import List, Dict

BANNED_WORDS = [
    r"modo militar", r"misión cumplida", r"letal\w*", r"quirúrg\w*",
    r"mutilad\w*", r"infierno", r"elefant\w*", r"brutal\w*", 
    r"salvando semanas", r"erradicaci[oó]n\w*", r"erradic\w*"
]

FIRST_PERSON = [
    r"\byo\b", r"\bmi\b", r"\bme\b", r"\bmío\b", r"\bconmigo\b"
]

ABSOLUTE_PROMISES = [
    r"garantiza", r"100%", r"mínimo \d+ días", r">95%"
]

def check_file(filepath: Path) -> Dict:
    content = filepath.read_text(encoding="utf-8")
    
    # Comprobar si hay una excepción activa
    exception_match = re.search(r"\*\*Excepción aplicada:\*\*\s*(EXC-\d{4}-\d{2}-\d{2}-\d{2})", content, re.IGNORECASE)
    has_exception = bool(exception_match)
    exception_id = exception_match.group(1) if has_exception else None

    issues = []
    
    # Solo castigamos primera persona si NO hay excepción
    if not has_exception:
        for i, line in enumerate(content.split('\n'), 1):
            for pattern in FIRST_PERSON:
                if re.search(pattern, line, re.IGNORECASE):
                    issues.append(f"L{i}: Primera persona detectada -> '{line.strip()}'")
                    break
        
    for i, line in enumerate(content.split('\n'), 1):
        for pattern in BANNED_WORDS:
            if re.search(pattern, line, re.IGNORECASE):
                issues.append(f"L{i}: Término bélico/grandilocuente prohibido -> '{line.strip()}'")
                break
                
        for pattern in ABSOLUTE_PROMISES:
            if re.search(pattern, line, re.IGNORECASE):
                if "HIPÓTESIS" not in line.upper() and "VALIDAR" not in line.upper():
                    issues.append(f"L{i}: Promesa absoluta sin contexto de [HIPÓTESIS] o validación -> '{line.strip()}'")
                break
    
    return {
        "file": filepath.name,
        "exception": exception_id,
        "issues": issues
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bloque", required=True, help="Directorio del bloque a escanear (ej. cases/logistica/output/bloque_1)")
    parser.add_argument("--salida", required=True, help="Ruta del reporte resultante (ej. cases/logistica/reports/ESTILO.md)")
    args = parser.parse_args()
    
    bloque_path = Path(args.bloque)
    salida_path = Path(args.salida)
    
    if not bloque_path.exists():
        print(f"Ruta no existe: {bloque_path}")
        return
        
    md_files = list(bloque_path.glob("*.md"))
    results = []
    total_issues = 0
    total_files_failed = 0
    
    for f in md_files:
        res = check_file(f)
        results.append(res)
        total_issues += len(res['issues'])
        if res['issues']:
            total_files_failed += 1
            
    report = ["# REPORTE DE ESTILO Y VOZ INSTITUCIONAL (Gate 0)\n"]
    report.append(f"- **Bloque analizado:** `{args.bloque}`")
    report.append(f"- **Total de archivos escaneados:** {len(md_files)}")
    report.append(f"- **Total de archivos con alertas:** {total_files_failed}")
    report.append(f"- **Total de incidencias:** {total_issues}\n")
    report.append("---\n")
    
    for r in results:
        report.append(f"## {r['file']}")
        if r['exception']:
            report.append(f"⚠️ **Atención:** Contiene excepción registrada: `{r['exception']}`. Se permiten desviaciones de voz, pero las palabras prohibidas siguen penalizadas.\n")
        
        if not r['issues']:
            report.append("- ✅ **APTO:** Cumple con tono, prudencia y voz del equipo.\n")
        else:
            report.append("- ❌ **FAIL:** Se detectaron rupturas de estilo:\n")
            for issue in r['issues']:
                report.append(f"  - {issue}")
            report.append("\n")
            
    salida_path.parent.mkdir(parents=True, exist_ok=True)
    salida_path.write_text("\n".join(report), encoding="utf-8")
    
    print(f"OK: Reporte de estilo generado en {salida_path} con {total_issues} alertas.")

if __name__ == '__main__':
    main()
