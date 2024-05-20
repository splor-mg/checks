import importlib
import typer
import logging
import importlib.metadata

from .requirements import check_installed_packages
from typing import Optional
from typing_extensions import Annotated


logger = logging.getLogger(__name__)

app = typer.Typer()

def version_callback(value: bool):
    if value:
        print(f"checks, version {importlib.metadata.version('checks')}")
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


@app.command("installed-packages")
def cli_packages(
    requirements_file: Annotated[str, typer.Argument()] = 'requirements.in',
    stop_on_failure: Annotated[bool, typer.Option("--stop-on-failure", help="stop execution if a package has the wrong version or is missing.")] = False,

):
    check_installed_packages(requirements_file, stop_on_failure)