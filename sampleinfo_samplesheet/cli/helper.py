import logging
from importlib.metadata import version as fn_version
from logging import Formatter
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Union

import typer
from rich.progress import Progress

from sampleinfo_samplesheet.logging.helper import (
    LOG_FORMAT,
    config_console_debug_logger,
)

log = logging.getLogger(__name__)
config_console_debug_logger(__name__)


def version_callback(value: bool):
    if value:
        print(f"CLI VERSION: {fn_version('varf')}")
        raise typer.Exit()


def get_rotating_file_handler(logfile: Union[Path, None]):
    if logfile is not None:
        logfile.parent.mkdir(parents=True, exist_ok=True)
        rfh = RotatingFileHandler(logfile, maxBytes=10 * 1024 * 1024, backupCount=10)
        rfh.setFormatter(Formatter(LOG_FORMAT))
        return rfh


def _is_progress(progress):
    return progress is not None and isinstance(progress, Progress)
