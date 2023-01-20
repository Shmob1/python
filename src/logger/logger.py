import logging
import logging.config
from pathlib import Path

import yaml  # type: ignore[import]

filepath_config = Path(__file__).parent / "config.yml"
filepath_output = Path("logs")
SETUP_LOGGING = False


def setup_logging(log_path: Path, show_debug: bool) -> None:
    global SETUP_LOGGING
    if SETUP_LOGGING:
        logging.getLogger(__name__).warning("Tried to reinitialise logger")
        return

    with filepath_config.open("rt") as fh:
        in_config = yaml.safe_load(fh.read())

    # set file names
    in_config["handlers"]["error_file_handler"]["filename"] = log_path / "error.log"
    in_config["handlers"]["debug_file_handler"]["filename"] = log_path / "debug.log"
    in_config["handlers"]["info_file_handler"]["filename"] = log_path / "info.log"

    if show_debug:
        in_config["handlers"]["console"]["level"] = logging.DEBUG

    log_path.mkdir(parents=True, exist_ok=True)
    logging.config.dictConfig(in_config)

    # disable numba logging
    numba_logger = logging.getLogger("numba")
    numba_logger.setLevel(logging.WARNING)

    SETUP_LOGGING = True
    logging.getLogger(__name__).info("init logging")


def set_level_error(*names):
    """Set the level of loggers to ERROR (useful for silencing 3rd party loggers)."""
    for name in names:
        logger = logging.getLogger(name)
        logger.setLevel(logging.ERROR)
