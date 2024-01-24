import logging
from pathlib import Path

import typer

from sampleinfo_samplesheet.cli import helper
from sampleinfo_samplesheet.logging.helper import (
    LoggingLevel,
    config_console_debug_logger,
)

log = logging.getLogger(__name__)
config_console_debug_logger(__name__)

APP = typer.Typer()
SIG = "kunyuan"


@APP.command(SIG)
def palindrome_artifact(
    _: bool = typer.Option(
        None, "--version", callback=helper.version_callback, is_eager=True
    ),
    verbosity: LoggingLevel = typer.Option(
        LoggingLevel.INFO,
        "-v",
        "--verbosity",
        envvar=("_".join([SIG, "verbosity"])).upper(),
        case_sensitive=False,
        help="logging level",
    ),
    logfile: Path = typer.Option(
        None,
        "-l",
        "--logfile",
        file_okay=True,
        dir_okay=False,
        resolve_path=True,
        envvar=("_".join([SIG, "logfile"])).upper(),
        help="path to log file",
    ),
):
    logging.basicConfig(level=verbosity.upper())
    for _name in []:
        logging.getLogger(_name).setLevel(logging.ERROR)
    rfh = helper.get_rotating_file_handler(logfile=logfile)

    if rfh:
        rfh.setLevel(verbosity.upper())
        log.addHandler(rfh)
        logging.getLogger("sampleinfo_samplesheet.cli.helper").addHandler(rfh)
        logging.getLogger("sampleinfo_samplesheet.logging.helper").addHandler(rfh)
        logging.getLogger().addHandler(rfh)

    # TODO Add main script here
