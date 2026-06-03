# File: tests/test_dry_run_saneamiento_fisico.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Pruebas unitarias para el script de dry-run de saneamiento físico.
# Rol: Asegurar la validez, robustez y el comportamiento de solo lectura del auditor.
# ──────────────────────────────────────────────────────────────────────

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import shutil
import pytest
import subprocess
from scripts.dry_run_saneamiento_fisico import run_dry_run

@pytest.fixture
def base_synth_repo(tmp_path):
    """Genera un repositorio sintético básico válido con gobernanza alineada e inicializa Git."""
    # Inicializar git ficticio en el directorio temporal
    subprocess.run(["git", "init"], cwd=str(tmp_path), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    
    # Configurar nombre/email mínimos de git por si acaso
    subprocess.run(["git", "config", "user.name", "Test User"], cwd=str(tmp_path), check=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=str(tmp_path), check=True)

    identity_content = """identity_version: "1.0"
repo_id: "proyecto_automatizaciones"
repo_name: "Proyecto Automatizaciones"
repo_role: "framework_mother"
repo_status: "active"
repo_owner: "equipo_tecnico"
contains_real_data: false
allows_project_creation: true
allows_framework_updates: false
allows_case_data: false
allows_artifact_generation: false
allows_cleanup: false
allows_extraction: false
allows_retention_export: false
requires_human_approval_for:
  - cleanup
"""
    manifest_content = """manifest_version: "1.0"
manifest_status: "draft"
adr_source: "ADR-001"
spec_source: "SPEC-001"
repo_role: "framework_mother"
generated_for_repo: "proyecto_automatizaciones"
artifacts:
  - path: "docs_base/"
    allowed_in_framework: false
    copy_policy: "exclude"
  - path: "output/"
    allowed_in_framework: false
    copy_policy: "exclude"
  - path: "cases/logistica/"
    allowed_in_framework: false
    copy_policy: "exclude"
"""
    
    identity_file = tmp_path / "repo_identity.yml"
    manifest_file = tmp_path / "artifact_manifest.yml"
    
    identity_file.write_text(identity_content, encoding="utf-8")
    manifest_file.write_text(manifest_content, encoding="utf-8")
    
    # Hacer commit inicial de los archivos normativos para que estén trackeados
    subprocess.run(["git", "add", "repo_identity.yml", "artifact_manifest.yml"], cwd=str(tmp_path), check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=str(tmp_path), check=True)
    
    return tmp_path

def test_dry_run_error_tecnico_si_no_es_git_repo(tmp_path):
    """Devuelve ERROR_TECNICO (3) si el directorio no es un repo Git."""
    # Sin git init, debe dar ERROR_TECNICO
    code = run_dry_run(workspace_dir=str(tmp_path))
    assert code == 3

def test_dry_run_error_tecnico_si_faltan_normativos(base_synth_repo):
    """Devuelve ERROR_TECNICO (3) si faltan repo_identity.yml o artifact_manifest.yml."""
    # Borrar un archivo normativo
    os.remove(base_synth_repo / "repo_identity.yml")
    code = run_dry_run(workspace_dir=str(base_synth_repo))
    assert code == 3

def test_dry_run_detecta_contradiccion_rol(base_synth_repo):
    """Detecta discrepancias de rol entre identidad y manifiesto (FAIL = 2)."""
    identity_content = "repo_role: 'framework_mother'\n"
    manifest_content = "repo_role: 'case_study'\n"
    
    (base_synth_repo / "repo_identity.yml").write_text(identity_content, encoding="utf-8")
    (base_synth_repo / "artifact_manifest.yml").write_text(manifest_content, encoding="utf-8")
    
    code = run_dry_run(workspace_dir=str(base_synth_repo))
    assert code == 2

def test_dry_run_detecta_ruta_legacy_y_da_warn_si_no_trackeada(base_synth_repo):
    """Detecta una ruta legacy física y reporta WARN (1) si no está en Git."""
    legacy_dir = base_synth_repo / "docs_base"
    legacy_dir.mkdir()
    (legacy_dir / "temp_file.txt").write_text("contenido", encoding="utf-8")
    
    code = run_dry_run(workspace_dir=str(base_synth_repo))
    assert code == 1
    
    report_file = base_synth_repo / "reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md"
    assert report_file.exists()
    
    report_content = report_file.read_text(encoding="utf-8")
    assert "docs_base" in report_content
    assert "`WARN`" in report_content

def test_dry_run_detecta_ruta_legacy_trackeada_en_git_da_fail(base_synth_repo):
    """Detecta una ruta legacy trackeada en Git y da FAIL (2)."""
    legacy_dir = base_synth_repo / "docs_base"
    legacy_dir.mkdir()
    legacy_file = legacy_dir / "tracked.txt"
    legacy_file.write_text("texto", encoding="utf-8")
    
    # Registrar en Git
    subprocess.run(["git", "add", "docs_base/tracked.txt"], cwd=str(base_synth_repo), check=True)
    subprocess.run(["git", "commit", "-m", "Add tracked file"], cwd=str(base_synth_repo), check=True)
    
    code = run_dry_run(workspace_dir=str(base_synth_repo))
    assert code == 2
    
    report_file = base_synth_repo / "reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md"
    report_content = report_file.read_text(encoding="utf-8")
    assert "`FAIL`" in report_content

def test_dry_run_distingue_referencia_informativa_de_operativa(base_synth_repo):
    """Distingue referencias informativas (WARN) de dependencias operativas (FAIL)."""
    scripts_dir = base_synth_repo / "scripts"
    scripts_dir.mkdir()
    
    # 1. Caso Informativo (comentario y texto de ayuda) - Debería retornar WARN
    script_file_warn = scripts_dir / "script_warn.py"
    script_file_warn.write_text("""
# Esta es una referencia a cases/logistica/ en un comentario
parser.add_argument("--bloque", help="Directorio como cases/logistica/")
""", encoding="utf-8")
    
    code1 = run_dry_run(workspace_dir=str(base_synth_repo))
    assert code1 == 1  # WARN por el comentario
    
    # 2. Caso Operativo (código activo) - Debería retornar FAIL
    script_file_fail = scripts_dir / "script_fail.py"
    script_file_fail.write_text("""
ruta_datos = "cases/logistica/config.json"
""", encoding="utf-8")
    
    code2 = run_dry_run(workspace_dir=str(base_synth_repo))
    assert code2 == 2  # FAIL por código operativo

def test_dry_run_no_modifica_archivos(base_synth_repo):
    """Garantiza que el dry-run no modifica ningún archivo normativo o de código original."""
    legacy_dir = base_synth_repo / "docs_base"
    legacy_dir.mkdir()
    legacy_file = legacy_dir / "info.txt"
    legacy_file.write_text("original text", encoding="utf-8")
    
    scripts_dir = base_synth_repo / "scripts"
    scripts_dir.mkdir()
    script_file = scripts_dir / "runtime_file.py"
    script_file.write_text("def run(): pass", encoding="utf-8")
    
    orig_identity = (base_synth_repo / "repo_identity.yml").read_text(encoding="utf-8")
    orig_manifest = (base_synth_repo / "artifact_manifest.yml").read_text(encoding="utf-8")
    orig_legacy = legacy_file.read_text(encoding="utf-8")
    orig_script = script_file.read_text(encoding="utf-8")
    
    run_dry_run(workspace_dir=str(base_synth_repo))
    
    assert (base_synth_repo / "repo_identity.yml").read_text(encoding="utf-8") == orig_identity
    assert (base_synth_repo / "artifact_manifest.yml").read_text(encoding="utf-8") == orig_manifest
    assert legacy_file.read_text(encoding="utf-8") == orig_legacy
    assert script_file.read_text(encoding="utf-8") == orig_script
    
    assert legacy_file.exists()
    assert script_file.exists()

def test_reporte_caracteres_no_ascii(base_synth_repo):
    """Prueba que el reporte maneje rutas no ASCII o caracteres especiales sin romperse."""
    legacy_dir = base_synth_repo / "docs_base"
    legacy_dir.mkdir()
    special_file = legacy_dir / "diseño_especial_ñ.md"
    special_file.write_text("Diseño con caracteres especiales y acentos.", encoding="utf-8")
    
    code = run_dry_run(workspace_dir=str(base_synth_repo))
    # Debe dar WARN (1)
    assert code == 1
    
    report_file = base_synth_repo / "reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md"
    assert report_file.exists()
    content = report_file.read_text(encoding="utf-8")
    assert "diseño_especial_ñ.md" in content

def test_comodines_del_manifest(base_synth_repo):
    """Prueba que el dry-run soporta y resuelve rutas con comodines declaradas en el manifiesto."""
    # Modificar el manifiesto de prueba para incluir un patrón con comodín
    manifest_content = """manifest_version: "1.0"
manifest_status: "draft"
repo_role: "framework_mother"
artifacts:
  - path: "cases/tmp_*/"
    allowed_in_framework: false
    copy_policy: "exclude"
"""
    (base_synth_repo / "artifact_manifest.yml").write_text(manifest_content, encoding="utf-8")
    
    # Crear la carpeta real de coincidencia
    cases_dir = base_synth_repo / "cases"
    cases_dir.mkdir(exist_ok=True)
    tmp_case_dir = cases_dir / "tmp_prueba_case_lifecycle"
    tmp_case_dir.mkdir()
    (tmp_case_dir / "dummy.txt").write_text("temp", encoding="utf-8")
    
    code = run_dry_run(workspace_dir=str(base_synth_repo))
    # Debe dar WARN (1) ya que detecta la carpeta física real que coincide con el patrón
    assert code == 1
    
    report_file = base_synth_repo / "reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md"
    assert report_file.exists()
    content = report_file.read_text(encoding="utf-8")
    assert "cases/tmp_prueba_case_lifecycle" in content
    assert "cases/tmp_*/" in content
