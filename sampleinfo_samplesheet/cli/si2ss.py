import logging
from pathlib import Path
from typing import List

import typer

from sampleinfo_samplesheet.cli import helper
from sampleinfo_samplesheet.logging.helper import (
    LoggingLevel,
    config_console_debug_logger,
)

# from typing_extensions import Annotated


log = logging.getLogger(__name__)
config_console_debug_logger(__name__)

APP = typer.Typer()
KUNYUAN = "kunyuan"


@APP.command(KUNYUAN)
def kunyuan(
    _: bool = typer.Option(
        None, "--version", callback=helper.version_callback, is_eager=True
    ),
    input: List[Path] = typer.Option(
        ...,
        "-i",
        "--input",
        exists=True,
        file_okay=True,
        dir_okay=False,
        help="Path to the input excel file",
    ),
    output: Path = typer.Option(
        ...,
        "-o",
        "--output",
        exists=False,
        file_okay=False,
        dir_okay=True,
        help="Directory to the output sample sheet.",
    ),
    config_file: Path = typer.Option(
        None,
        "-c",
        "--config",
        exists=True,
        file_okay=True,
        dir_okay=False,
        resolve_path=True,
        help="Path to the parameter config file.",
    ),
    verbosity: LoggingLevel = typer.Option(
        LoggingLevel.INFO,
        "-v",
        "--verbosity",
        envvar=("_".join([KUNYUAN, "verbosity"])).upper(),
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
        envvar=("_".join([KUNYUAN, "logfile"])).upper(),
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
    log.info(input)
    log.info(output)


@APP.callback()
def callback():
    """
    Convert a sequencing sample info excel to a sample sheet for bcl2fastq
    """


def main():
    APP()


if __name__ == "__main__":
    main()
