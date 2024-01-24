import logging

import typer

import sampleinfo_samplesheet.cli.kunyuan as kunyuan
from sampleinfo_samplesheet.logging.helper import config_console_debug_logger

log = logging.getLogger(__name__)
config_console_debug_logger(__name__)

SIG_KUNYUAN = "kunyuan"

APP = typer.Typer()

APP.add_typer(kunyuan.APP, name=kunyuan.SIG)


def main():
    APP()


if __name__ == "__main__":
    main()
