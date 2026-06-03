# File: src/orchestrator/states.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definición de estados y eventos para el Orquestador.
# Rol: Enums y constantes para la máquina de estados.
# ──────────────────────────────────────────────────────────────────────

from enum import Enum

class PhaseStatus(str, Enum):
    IDLE = "IDLE"
    PREPARING = "PREPARING"
    EXECUTING = "EXECUTING"
    AWAITING_USER = "AWAITING_USER"
    AUDITING = "AUDITING"
    BLOCKED = "BLOCKED"
    REVISING = "REVISING"
    READY = "READY"
    CLOSED = "CLOSED"
    PAUSED = "PAUSED"

class OrchestratorEvent(str, Enum):
    START_PHASE = "START_PHASE"
    READY_FOR_EXEC = "READY_FOR_EXEC"
    NEED_INPUT = "NEED_INPUT"
    INPUT_RECEIVED = "INPUT_RECEIVED"
    FINISH_EXEC = "FINISH_EXEC"
    GATE_FAIL_CRITICAL = "GATE_FAIL_CRITICAL"
    GATE_FAIL_HUMAN = "GATE_FAIL_HUMAN"
    SUCCESS_ALL = "SUCCESS_ALL"
    COMMIT_SESSION = "COMMIT_SESSION"
    USER_ABANDON = "USER_ABANDON"
    RESUME_SESSION = "RESUME_SESSION"
