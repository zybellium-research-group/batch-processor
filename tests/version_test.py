import pytest
import sys
import os

from __init__ import __version__


def test_version():
    assert type(__version__) == str
