from pathlib import Path
from typing import Literal

PKG_AUTHOR = "UK AI Security Institute"
PKG_AUTHOR_DIR = "UK-AISI"
PKG_NAME = Path(__file__).parent.parent.stem
PKG_PATH = Path(__file__).parent.parent
DEFAULT_EPOCHS = 1
DEFAULT_MAX_CONNECTIONS = 10
DEFAULT_MAX_TOKENS = 2048
DEFAULT_VIEW_PORT = 7575
DEFAULT_SERVER_HOST = "127.0.0.1"
HTTP = 15
HTTP_LOG_LEVEL = "HTTP"
TRACE = 13
TRACE_LOG_LEVEL = "TRACE"
ALL_LOG_LEVELS = [
    "DEBUG",
    TRACE_LOG_LEVEL,
    HTTP_LOG_LEVEL,
    "INFO",
    "WARNING",
    "ERROR",
    "CRITICAL",
]
DEFAULT_LOG_LEVEL = "warning"
DEFAULT_LOG_LEVEL_TRANSCRIPT = "info"
ALL_LOG_FORMATS = ["eval", "json"]
DEFAULT_LOG_FORMAT: Literal["eval", "json"] = "eval"
EVAL_LOG_FORMAT = "eval"
DEFAULT_DISPLAY = "full"
LOG_SCHEMA_VERSION = 2
SCORED_SUFFIX = "-scored"
SAMPLE_SUBTASK = "sample"
CONSOLE_DISPLAY_WIDTH = 120
BASE_64_DATA_REMOVED = "<base64-data-removed>"
SANDBOX_SETUP_TIMEOUT = 300
NO_CONTENT = "(no content)"
