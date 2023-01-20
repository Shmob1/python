from setuptools import find_packages, setup

setup(
    name="PROJECT",
    version="0.0.1",
    author="",
    author_email="",
    description="",
    packages=find_packages(exclude=("tests",)),
    classifiers=["Programming Language :: Python"],
    entry_points={"console_scripts": ["python-env=src.cli"]},
)
