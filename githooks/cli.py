from logging import getLogger

from pathlib import Path
import click
import yaml  # type: ignore[import]
import munch

from githooks.logger import setup_logging
import githooks

filepath_root = Path(githooks.__file__).parent.parent
filepath_params = filepath_root / "params.yaml"

log = getLogger(__name__)


@click.group()
@click.option(
    "-v",
    "--verbose",
    type=bool,
    help=("Enable to show debug level logging in console."),
)
def cli(verbose: bool = False):
    """Entry point for the CLI."""
    params = munch.munchify(yaml.safe_load(filepath_params.read_text()))
    setup_logging(Path(params.paths.log_path), verbose)
    log.info("Entry point for the CLI.")


@cli.command
def test():
    log.info("made it to test")


if __name__ == "__main__":
    cli()  # python -m githooks.cli [OPTIONS] COMMAND [ARGS]
