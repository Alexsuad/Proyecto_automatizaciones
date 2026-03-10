import json
import os
import shutil
from datetime import datetime

# Rutas
DATA_PATH = "data/bmc_state.json"
DOCS_ACTIVA_PATH = "docs/OPCION_ACTIVA.md"
OUTPUT_DIR = "apps/bmc_streamlit/exports"
# ! [ALERTA]: No usar output/bloque_1/ — esa carpeta es para entregables oficiales del cronograma.
# El export de la App BMC se guarda en apps/bmc_streamlit/exports/ para no contaminar el pipeline QA.
ARCHIVE_DIR = os.path.join(OUTPUT_DIR, "archive")
OUTPUT_MD = os.path.join(OUTPUT_DIR, "10_business_model_canvas_app.md")

BLOCK_NAMES = {
    "key_partners": "Asociaciones Clave",
    "key_activities": "Actividades Clave",
    "key_resources": "Recursos Clave",
    "value_propositions": "Propuestas de Valor",
    "customer_relationships": "Relaciones con los Clientes",
    "channels": "Canales",
    "customer_segments": "Segmentos de Mercado",
    "cost_structure": "Estructura de Costes",
    "revenue_streams": "Fuentes de Ingresos"
}

def get_opcion_activa():
    try:
        with open(DOCS_ACTIVA_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
            # Extraer las primeras líneas relevantes
            header_lines = []
            for line in lines:
                if line.strip() and not line.startswith("# "):
                    header_lines.append(line.strip())
                if len(header_lines) >= 3:
                    break
            return "\n".join(header_lines)
    except Exception:
        return "Opción activa no encontrada o no definida explícitamente."

def create_backup_if_exists():
    if os.path.exists(OUTPUT_MD):
        os.makedirs(ARCHIVE_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(ARCHIVE_DIR, f"10_bmc_app_{timestamp}.md")
        shutil.copy2(OUTPUT_MD, backup_path)
        print(f"Backup creado en: {backup_path}")

def generate_markdown(data):
    md_lines = []
    md_lines.append("# Business Model Canvas")
    md_lines.append("")
    md_lines.append("## Contexto y Opción Activa")
    md_lines.append("El equipo define el siguiente contexto para la iniciativa:")
    md_lines.append("")
    md_lines.append(get_opcion_activa())
    md_lines.append("")
    
    all_hypotheses = []

    # Iterar por bloques asegurando el orden correcto
    for key, title in BLOCK_NAMES.items():
        md_lines.append(f"## {title}")
        notes = data.get(key, [])
        if not notes:
            md_lines.append("\n*Sin notas en este bloque.*")
        else:
            # Agrupar por tags
            hechos = [n for n in notes if n.get("tag") == "hecho"]
            hipotesis = [n for n in notes if n.get("tag") == "hipotesis"]
            acciones = [n for n in notes if n.get("tag") == "accion"]

            if hechos:
                md_lines.append("\n**Hechos declarados:**")
                for item in sorted(hechos, key=lambda x: x.get("order", 0)):
                    md_lines.append(f"- {item.get('text', '')}")
            
            if hipotesis:
                md_lines.append("\n**Hipótesis:**")
                for item in sorted(hipotesis, key=lambda x: x.get("order", 0)):
                    md_lines.append(f"- {item.get('text', '')}")
                    all_hypotheses.append(item)
                    
            if acciones:
                md_lines.append("\n**Acciones:**")
                for item in sorted(acciones, key=lambda x: x.get("order", 0)):
                    md_lines.append(f"- {item.get('text', '')}")
                    
        md_lines.append("")

    # Bloque final de Hipótesis y validación
    md_lines.append("## Hipótesis + Cómo se valida")
    if not all_hypotheses:
        md_lines.append("No hay hipótesis definidas en la iniciativa aún.")
    else:
        for item in all_hypotheses:
            texto = item.get('text', '')
            md_lines.append(f"**[HIPÓTESIS]** {texto}")
            md_lines.append("**[CÓMO SE VALIDA]** (Piloto + baseline + métrica pendiente)")
            md_lines.append("")

    # Bloque NotebookLM
    md_lines.append("## Nota de Registro NotebookLM")
    md_lines.append("- **notebook_title:** ZAC_Bloque_1")
    md_lines.append("- **notebook_id:** (pendiente)")
    md_lines.append("- **note_title:** HITO: BMC Export App")
    md_lines.append("- **note_id:** (pendiente)")
    md_lines.append(f"- **fecha:** {datetime.now().strftime('%Y-%m-%d')}")
    md_lines.append("")

    return "\n".join(md_lines)

def main():
    if not os.path.exists(DATA_PATH):
        print(f"Error: {DATA_PATH} no encontrado.")
        return

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    create_backup_if_exists()
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    markdown_content = generate_markdown(data)
    
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(markdown_content)
        
    print(f"BMC exportado exitosamente a {OUTPUT_MD}")

if __name__ == "__main__":
    main()
