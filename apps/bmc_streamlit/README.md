# App Streamlit "BMC Board"

Aplicación interactiva y local para gestionar el Business Model Canvas (BMC) del proyecto de forma estructurada, persistente y auditable.

## 1. Funcionamiento y Persistencia
- **Fuente de verdad:** Todo el estado del tablero se guarda automáticamente en `data/bmc_state.json`.
- **Estructura estricta:** Solo existen 9 bloques oficiales del BMC.
- **Tipos de notas (Tags):**
  - `hipotesis`: Supuestos que requieren ser validados (generarán su propia sección en el export).
  - `hecho`: Datos fácticos basados en entrevistas o investigación.
  - `accion`: Siguientes pasos acordados.

## 2. Instalación de dependencias
El manejo de dependencias se realiza mediante `uv` a nivel del repositorio raíz.
Para asegurar que tienes todo lo necesario, sitúate en la raíz del repositorio y ejecuta:

```bash
uv sync
```
*(Esto instalará `streamlit` y el resto de paquetes según `pyproject.toml`)*

## 3. Ejecución de la App
Para levantar el servidor local de Streamlit, desde la raíz del repositorio ejecuta:

```bash
uv run streamlit run apps/bmc_streamlit/streamlit_app.py
```
Esto abrirá la aplicación en tu navegador (por defecto en `http://localhost:8501`).

## 4. Flujo de Exportación y QA Automático
1. En la app, asegúrate de haber redactado las notas con **voz institucional** (tercera persona). Si usas "yo" o "nosotros", la UI te mostrará un *Warning* preventivo.
2. Pulsa el botón **📤 Exportar a MD y QA**.
3. La aplicación utilizará `scripts/export_bmc_to_md.py` para:
   - Hacer un **backup** del export anterior en `output/bloque_1/archive/`.
   - Generar la versión en Markdown en `output/bloque_1/10_business_model_canvas_app.md`.
4. Inmediatamente después, lanzará los *scripts de QA* del equipo:
   - `validar_estilo_equipo.py`
   - `validar_entregables.py`
5. La UI de Streamlit mostrará si el código de salida de estos QA es exitoso (PASS) o si fallaron (FAIL), permitiéndote desplegar los errores. Los reportes completos se almacenarán en `reports/`.

## 5. Limitaciones del MVP
- No soporta "Drag & Drop" libre para arrastrar notas. El reordenamiento se hace con los botones **[↑]** y **[↓]**, y los movimientos de bloque mediante el desplegable al editar una nota.
- El script sobrescribirá ciegamente el `.md` (tras hacer backup) apoyándose estrictamente en lo que exista en el JSON, no se conservarán ediciones manuales que se hagan directamente sobre el Markdown.
