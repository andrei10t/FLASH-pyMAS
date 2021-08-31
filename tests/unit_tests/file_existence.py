import os.path
from os import path
import pytest


def checkFileExistence():
    assert path.exists("/opt/pyflash/src/agent.py") == True
