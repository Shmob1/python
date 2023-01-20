import os
from logging import getLogger
from pathlib import Path
from typing import Union

import requests  # type: ignore[import]
from tqdm import tqdm

log = getLogger(__name__)


def mkdir(*args: Union[str, Path]):
    """
    Create folders if they doesn't exist
    """
    for fd in args:
        if not os.path.exists(fd):
            os.makedirs(fd)

    return args


def download(url: Union[Path, str], out_file: Union[Path, str]):

    if type(url) is Path:
        url = url.as_posix()

    if type(out_file) is Path:
        out_file = out_file.as_posix()

    mkdir(os.path.dirname(out_file))
    response = requests.get(url, stream=True)  # type: ignore[arg-type]
    size = int(response.headers.get("content-length", 0))
    progress = tqdm(total=size, unit="iB", unit_scale=True)

    with open(out_file, "wb") as f:
        for data in response.iter_content(chunk_size=1024):
            progress.update(len(data))
            f.write(data)

    if os.path.getsize(out_file) != size:
        log.critical("{} is corrupt".format(out_file))
        exit(50)
