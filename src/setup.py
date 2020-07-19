
"""This file contains the necessary functionality to package stocktracker application"""
import os
from setuptools import setup, find_packages #type:ignore

NAME = "src"
APPNAME = "stocktracker"
DIRNAME = os.path.dirname(__file__)
EXTRAS = {}

def read(filename):
    """
    Read a given filename in the directory of the current file and
    return the content of the file

    Keyword arguments:
        filename (str): name of the file that needs to be read
    """
    filepath = os.path.join(DIRNAME, filename)
    with open(filepath, "r") as file_name:
        data = file_name.read().strip()
        return data

def reqs(name):
    """
    Entry Point Method for the package

    Keyword arguments:
        filename (str): name of the file that needs to be read
    """
    filename = f"requirements-{name}.txt"
    return read(filename)

REQUIRES = read("requirements.txt").split("\n")

EXTRAS["dev"] = reqs("dev").split("\n")

setup(
        name=APPNAME,
        version=read("VERSION"),
        description="Python app to track stock prices over time!",
        packages=find_packages(),
        install_requires=REQUIRES,
        extras_require=EXTRAS,
        entry_points={
            "console_scripts": [
                f"{NAME} = {NAME}.main:main",
                ],
            },
        )
