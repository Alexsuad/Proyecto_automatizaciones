import json
import os
import re
import uuid
from datetime import datetime

MD_PATH = "output/bloque_1/10_business_model_canvas.md"
JSON_PATH = "data/bmc_state.json"

MAPEO_BLOQUES = {
    "asociaciones clave": "key_partners",
    "actividades clave": "key_activities",
    "recursos clave": "key_resources",
    "propuesta de valor": "value_propositions",
    "relaciones con clientes": "customer_relationships",
    "canales": "channels",
    "segmentos de clientes": "customer_segments",
    "estructura de costes": "cost_structure",
    "fuentes de ingreso": "revenue_streams"
}

def clean_text(text):
    text = re.sub(r'^\s*-\s*', '', text)
    return text.strip()

def determine_tag(text):
    text_lower = text.lower()
    if "hipótesis" in text_lower or "hipotesis" in text_lower or "[hipótesis]" in text_lower:
        return "hipotesis"
    if "acción" in text_lower or "accion" in text_lower or "próximo paso" in text_lower:
        return "accion"
    return "hecho"

def import_md_to_json():
    if not os.path.exists(MD_PATH):
        print(f"Error: No se encuentra el archivo {MD_PATH}")
        return

    # Iniciar estado vacio
    state = {k: [] for k in MAPEO_BLOQUES.values()}

    with open(MD_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_block = None
    parsing_hypothesis = False
    
    for line in lines:
        line_s = line.strip()
        
        # Detectar cabecera de hipótesis especiales
        if line_s.startswith("## Hipótesis + Cómo se valida"):
            parsing_hypothesis = True
            current_block = None
            continue
            
        # Detectar fin de la lectura útil
        if line_s.startswith("**Nota de Registro NotebookLM**"):
            break

        # Detectar cabecera normal
        if line_s.startswith("## "):
            block_title = line_s.replace("## ", "").strip().lower()
            current_block = None
            for key in MAPEO_BLOQUES.keys():
                if block_title.startswith(key):
                    current_block = MAPEO_BLOQUES[key]
                    break
            parsing_hypothesis = False
            continue

        # Si estamos dentro de un bloque y encontramos una lista
        if current_block and line_s.startswith("- "):
            text = clean_text(line_s)
            tag = determine_tag(text)
            
            # Quitar tags duros del markdown si los pasamos como property
            text = text.replace("**[HIPÓTESIS]**", "").strip()
            
            note = {
                "id": str(uuid.uuid4()),
                "block": current_block,
                "text": text,
                "tag": tag,
                "order": len(state[current_block]),
                "created_at": datetime.now().strftime("%Y-%m-%d"),
                "updated_at": datetime.now().strftime("%Y-%m-%d")
            }
            state[current_block].append(note)

        # Si estamos parseando las hipótesis genéricas al final y encontramos la declaración
        elif parsing_hypothesis and line_s.startswith("- **[HIPÓTESIS]**"):
            # Tratar de ubicar de dónde viene según contexto, pero si no, ponerlo temporalmente en Value Proposition u otro.
            # En realidad esto suele reemplazar o expandir las hipótesis de arriba. Ignoramos por ahora si ya lo capturamos arriba.
            pass

    # Extras "Supuestos" o "Proximo paso"
    for line in lines:
        line_s = line.strip()
        if line_s.startswith("- ¿"):
             note = {
                "id": str(uuid.uuid4()),
                "block": "customer_segments", # asig aleatoriamente pero modificable
                "text": "Supuesto a desaturar: " + clean_text(line_s),
                "tag": "hipotesis",
                "order": len(state["customer_segments"]),
                "created_at": datetime.now().strftime("%Y-%m-%d"),
                "updated_at": datetime.now().strftime("%Y-%m-%d")
            }
             state["customer_segments"].append(note)

    # Guardar JSON
    os.makedirs(os.path.dirname(JSON_PATH), exist_ok=True)
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
        
    print(f"✅ Importación exitosa a {JSON_PATH}")

if __name__ == "__main__":
    import_md_to_json()
