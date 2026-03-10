import streamlit as st
import json
import os
import uuid
import subprocess
from datetime import datetime
from io import BytesIO

# Configuración de página
st.set_page_config(page_title="ZAC BMC Board", layout="wide", page_icon="📋")

# Rutas de datos
DATA_PATH = "data/bmc_state.json"
EXPORT_SCRIPT = "scripts/export_bmc_to_md.py"
QA_SCRIPT_ESTILO = "scripts/validar_estilo_equipo.py"
QA_SCRIPT_ESTRUCTURA = "scripts/validar_entregables.py"
REPORT_DIR = "reports"

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

TAGS = ["hipotesis", "hecho", "accion"]

# Funciones de persistencia
def load_data():
    if os.path.exists(DATA_PATH):
        try:
            with open(DATA_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return {k: [] for k in BLOCK_NAMES}

def save_data(data):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def check_style_warning(text):
    forbidden = ["yo", "nosotros", "mi", "nuestro", "nuestra", "mis", "nuestros", "nuestras", "creo", "pienso", "opino"]
    words = [w.lower().strip(".,;:()") for w in text.split()]
    for f in forbidden:
        if f in words:
            return True
    return False

# Funciones CRUD
def add_note(block, text, tag, color="#ffffff"):
    new_note = {
        "id": str(uuid.uuid4()),
        "block": block,
        "text": text,
        "tag": tag,
        "color": color,
        "order": len(st.session_state.bmc_data[block]),
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "updated_at": datetime.now().strftime("%Y-%m-%d")
    }
    st.session_state.bmc_data[block].append(new_note)
    save_data(st.session_state.bmc_data)

def update_note(block, note_id, new_text, new_tag, new_block=None, new_color="#ffffff"):
    notes = st.session_state.bmc_data[block]
    for i, n in enumerate(notes):
        if n["id"] == note_id:
            n["text"] = new_text
            n["tag"] = new_tag
            n["color"] = new_color
            n["updated_at"] = datetime.now().strftime("%Y-%m-%d")
            
            if new_block and new_block != block:
                n["block"] = new_block
                n["order"] = len(st.session_state.bmc_data[new_block])
                st.session_state.bmc_data[new_block].append(n)
                notes.pop(i)
                # Reorder old block
                for j, old_n in enumerate(notes):
                    old_n["order"] = j
            break
    save_data(st.session_state.bmc_data)

def delete_note(block, note_id):
    notes = st.session_state.bmc_data[block]
    st.session_state.bmc_data[block] = [n for n in notes if n["id"] != note_id]
    # Reorder
    for j, n in enumerate(st.session_state.bmc_data[block]):
        n["order"] = j
    save_data(st.session_state.bmc_data)

def move_order(block, note_id, direction):
    notes = st.session_state.bmc_data[block]
    idx = next((i for i, n in enumerate(notes) if n["id"] == note_id), -1)
    if idx == -1: return
    
    if direction == "up" and idx > 0:
        notes[idx], notes[idx-1] = notes[idx-1], notes[idx]
    elif direction == "down" and idx < len(notes)-1:
        notes[idx], notes[idx+1] = notes[idx+1], notes[idx]
        
    for j, n in enumerate(notes):
        n["order"] = j
    save_data(st.session_state.bmc_data)

def execute_export_and_qa():
    st.info("Exportando a Markdown...")
    try:
        subprocess.run(["uv", "run", "python", EXPORT_SCRIPT], check=True, capture_output=True, text=True)
        st.success("BMC exportado a Markdown correctamente.")
    except subprocess.CalledProcessError as e:
        st.error(f"Error al exportar: {e.stderr}")
        return

    st.info("Ejecutando QA (Estilo y Estructura)...")
    qa_results = []
    
    # 1. Validar estilo
    try:
        report_estilo = os.path.join(REPORT_DIR, "reporte_estilo_bloque_1.md")
        result_estilo = subprocess.run(
            ["uv", "run", "python", QA_SCRIPT_ESTILO, "--bloque", "output/bloque_1", "--salida", report_estilo],
            capture_output=True, text=True
        )
        qa_results.append(("Estilo", result_estilo.returncode == 0, report_estilo, result_estilo.stdout or result_estilo.stderr))
    except Exception as e:
        qa_results.append(("Estilo", False, "", str(e)))

    # 2. Validar estructura
    try:
        report_estructura = os.path.join(REPORT_DIR, "reporte_validacion_bloque_1.md")
        result_estructura = subprocess.run(
            ["uv", "run", "python", QA_SCRIPT_ESTRUCTURA, "--bloque", "output/bloque_1", "--salida", report_estructura],
            capture_output=True, text=True
        )
        qa_results.append(("Estructura", result_estructura.returncode == 0, report_estructura, result_estructura.stdout or result_estructura.stderr))
    except Exception as e:
        qa_results.append(("Estructura", False, "", str(e)))

    for name, success, report, details in qa_results:
        if success:
            st.success(f"✅ QA {name}: PASS")
        else:
            st.error(f"❌ QA {name}: FAIL")
            with st.expander(f"Detalles de error {name}"):
                st.code(details)

# UI Main
if "bmc_data" not in st.session_state:
    st.session_state.bmc_data = load_data()

st.title("Business Model Canvas - ZAC Board")

# Top Bar / Controls
col_ctrl1, col_ctrl2, col_ctrl3 = st.columns([2, 1, 1])

with col_ctrl1:
    if st.button("📤 Exportar a MD y QA", use_container_width=True):
        found_warning = False
        for blk, notes in st.session_state.bmc_data.items():
            for n in notes:
                if check_style_warning(n["text"]):
                    found_warning = True
                    break
        if found_warning:
            st.warning("⚠️ Hay notas que usan primera persona ('yo', 'nosotros'). Se recomienda corregirlas para mantener voz institucional.")
        execute_export_and_qa()

with col_ctrl2:
    st.download_button(
        label="💾 Descargar JSON",
        data=json.dumps(st.session_state.bmc_data, indent=2),
        file_name="bmc_state.json",
        mime="application/json",
        use_container_width=True
    )

with col_ctrl3:
    uploaded_file = st.file_uploader("📥 Importar JSON", type=["json"], label_visibility="collapsed")
    if uploaded_file is not None:
        if st.button("⚠️ Confirmar Importación", use_container_width=True):
            try:
                data = json.load(uploaded_file)
                if all(k in data for k in BLOCK_NAMES):
                    st.session_state.bmc_data = data
                    save_data(data)
                    st.success("Importado exitosamente.")
                    st.rerun()
                else:
                    st.error("JSON no válido para BMC.")
            except Exception:
                st.error("Error leyendo JSON.")

st.divider()

# Colores de post-its
COLORS = {
    "hipotesis": "#fff3cd",
    "hecho": "#d1e7dd",
    "accion": "#cff4fc"
}

BLOCK_COLORS = {
    "key_partners": "#fdf3e7",
    "key_activities": "#e8f4f8",
    "key_resources": "#e8f4f8",
    "value_propositions": "#fff8e1",
    "customer_relationships": "#e8f5e9",
    "channels": "#e8f5e9",
    "customer_segments": "#fce4ec",
    "cost_structure": "#f3e5f5",
    "revenue_streams": "#f1f8e9"
}

def render_block(block_key):
    notes = sorted(st.session_state.bmc_data[block_key], key=lambda x: x.get("order", 0))
    st.markdown(f'<div style="background-color: {BLOCK_COLORS[block_key]}; padding: 10px; border-radius: 5px; text-align: center; border: 1px solid #ccc; margin-bottom: 10px;"><b>{BLOCK_NAMES[block_key]} ({len(notes)})</b></div>', unsafe_allow_html=True)
    
    with st.popover("➕ Nuevo", use_container_width=True):
        text_input = st.text_area("Texto", key=f"new_txt_{block_key}")
        tag_sel = st.selectbox("Etiqueta", options=TAGS, key=f"new_tag_{block_key}")
        color_sel = st.color_picker("Color de fondo de nota", value="#fff9c4", key=f"new_color_{block_key}")
        if st.button("Crear", key=f"btn_create_{block_key}"):
            if text_input.strip():
                add_note(block_key, text_input.strip(), tag_sel, color_sel)
                st.rerun()
                
    for idx, note in enumerate(notes):
        bg_color = COLORS.get(note["tag"], "#ffffff")
        note_color = note.get("color", "#ffffff")
        with st.container(border=True):
            st.markdown(f'<div style="background-color: {note_color}; padding: 10px; border-radius: 5px; color: #000; margin-bottom: 5px; box-shadow: inset 0 0 0 1px rgba(0,0,0,0.1);">'
                        f'<div style="background-color: {bg_color}; padding: 3px 6px; border-radius: 3px; font-size: 0.7em; display: inline-block; margin-bottom: 8px;"><b>{note["tag"].upper()}</b></div>'
                        f'<div style="font-size: 0.95em;">{note["text"]}</div>'
                        f'</div>', unsafe_allow_html=True)
            
            if check_style_warning(note["text"]):
                st.markdown('<span style="color:red; font-size:0.8em;">⚠️ Estilo: evitar "yo/nosotros"</span>', unsafe_allow_html=True)
                
            c1, c2, c3, c4 = st.columns([1,1,1,1])
            with c1:
                with st.popover("✏️"):
                    edit_text = st.text_area("Texto", value=note["text"], key=f"text_{note['id']}")
                    edit_tag = st.selectbox("Etiqueta", options=TAGS, index=TAGS.index(note["tag"]), key=f"tag_{note['id']}")
                    edit_block = st.selectbox("Mover a bloque", options=list(BLOCK_NAMES.keys()), format_func=lambda x: BLOCK_NAMES[x], index=list(BLOCK_NAMES.keys()).index(block_key), key=f"move_{note['id']}")
                    edit_color = st.color_picker("Color de fondo", value=note.get("color", "#ffffff"), key=f"color_{note['id']}")
                    if st.button("Guardar", key=f"save_{note['id']}"):
                        update_note(block_key, note['id'], edit_text, edit_tag, edit_block, edit_color)
                        st.rerun()
            with c2:
                if st.button("🗑️", key=f"del_{note['id']}"):
                    delete_note(block_key, note['id'])
                    st.rerun()
            with c3:
                if st.button("↑", key=f"up_{note['id']}", disabled=(idx == 0)):
                    move_order(block_key, note['id'], "up")
                    st.rerun()
            with c4:
                if st.button("↓", key=f"down_{note['id']}", disabled=(idx == len(notes) - 1)):
                    move_order(block_key, note['id'], "down")
                    st.rerun()

# Layout del BMC tipo Grid Clásico
# Row 1: 5 Columnas
col_kp, col_ka_kr, col_vp, col_cr_ch, col_cs = st.columns([1, 1, 1, 1, 1])

with col_kp:
    render_block("key_partners")

with col_ka_kr:
    render_block("key_activities")
    st.divider()
    render_block("key_resources")

with col_vp:
    render_block("value_propositions")

with col_cr_ch:
    render_block("customer_relationships")
    st.divider()
    render_block("channels")

with col_cs:
    render_block("customer_segments")

st.divider()

# Row 2: 2 Columnas inferioes (Mitad y Mitad)
col_cost, col_rev = st.columns(2)

with col_cost:
    render_block("cost_structure")

with col_rev:
    render_block("revenue_streams")
