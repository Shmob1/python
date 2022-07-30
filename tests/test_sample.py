import pytest

from githooks import cli


def add(a, b):
    return a + b


@pytest.mark.parametrize(
    "a, b, c",
    [
        (2, 2, 4),
        (3, 4, 7),
    ],
)
def test_add(a, b, c):
    assert add(a, b) == c


def test_main():
    cli.main()
