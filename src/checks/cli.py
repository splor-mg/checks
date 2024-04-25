import importlib
import typer
import logging
import importlib.metadata

from requirements import check_packages
from typing import Optional
from typing_extensions import Annotated


logger = logging.getLogger(__name__)

app = typer.Typer()

def version_callback(value: bool):
    if value:
        print(f"checks, version {importlib.metadata.version('dpm')}")
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        Optional[bool],
        typer.Option("--version", callback=version_callback, is_eager=True),
    ] = None,
):
    """
    A package to centralize data checking functionalities related to SEPLAG's SPLOR subsecretariat.
    """


@app.command("check_packages")
def cli_packages(
    requirements_file: Annotated[str, typer.Argument()] = 'requirements.in',
    stop_on_missing: Annotated[bool, typer.Option("--stop-missing")] = False,
    stop_on_wrong_version: Annotated[bool, typer.Option("--stop-wrong-package")] = False,

):
    check_packages(requirements_file, stop_on_missing, stop_on_wrong_version)