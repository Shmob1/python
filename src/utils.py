import os
import random
from logging import getLogger
from pathlib import Path
from typing import Union

import numpy as np
import requests
import yaml
from munch import Munch
from tqdm import tqdm

log = getLogger(__name__)


class Params(Munch):
    @classmethod
    def fromYaml(cls, path):
        with open(path) as f:
            return cls.fromDict(yaml.safe_load(f))


def seed(sed: int):
    """
    seed everything
    """
    random.seed(sed)
    np.random.seed(sed)


def mkdir(*args: Union[str, Path]):
    """
    Create folders if they doesn't exist
    """
    for fd in args:
        fd = Path(fd)
        if not os.path.exists(fd):
            os.makedirs(fd)

    if len(args) == 1:
        return args[0]
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
