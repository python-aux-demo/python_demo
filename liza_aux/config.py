import os
from logging.config import dictConfig
from pathlib import Path

LOG_DIR = Path(os.getenv("LOG_DIR", "."))

PLAIN_LOG_PATH = LOG_DIR / "liza_aux.log"
JSON_LOG_PATH = LOG_DIR / "liza_aux.log"


# === Logging =========================

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "flat_console_formatter": {
            "()": "liza_aux.loggers.CustomFlatFormatter",
            "fmt": "%(levelname)s %(asctime)s %(message)s",
            "datefmt": "%H:%M:%S",
        },
        "flat_file_formatter": {
            "()": "liza_aux.loggers.CustomFlatFormatter",
            "fmt": "%(levelname)s %(module)s %(funcName)s %(asctime)s %(message)s",
        },
        "json_file_formatter": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "fmt": "%(levelname)s %(message)s %(asctime)s %(pathname)s %(module)s %(funcName)",
        },
    },
    "handlers": {
        "flat_console": {
            "level": "INFO",
            "formatter": "flat_console_formatter",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "flat_file": {
            "level": "INFO",
            "formatter": "flat_file_formatter",
            "class": "logging.FileHandler",
            "filename": PLAIN_LOG_PATH,
            "mode": "w",
        },
        "json_file": {
            "level": "INFO",
            "formatter": "json_file_formatter",
            "class": "logging.FileHandler",
            "filename": JSON_LOG_PATH,
            "mode": "w",
        },
    },
    "loggers": {
        "": {
            "handlers": ["flat_console", "flat_file", "json_file"],
            "level": "INFO",
            "propagate": False,
        },
        "alembic.runtime.migration": {
            "handlers": ["flat_console", "flat_file", "json_file"],
            "level": "ERROR",
        },
        "numba.cuda.cudadrv": {
            "handlers": ["flat_console", "flat_file", "json_file"],
            "level": "ERROR",
        },
        "sqlitedict": {
            "handlers": ["flat_console", "flat_file", "json_file"],
            "level": "ERROR",
        },
    },
}


def init_logging() -> None:
    dictConfig(LOGGING_CONFIG)


def init_config() -> None:
    pass


init_logging()
