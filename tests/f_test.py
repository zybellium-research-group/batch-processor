import pytest
import sys


from batch_processor.__main__ import f


def test_f():
    assert f(True) == False
    assert f(False) == True


def test_f_type():
    assert type(f()) == bool


def test_f_fail():
    with pytest.raises(TypeError, match=r"No!"):
        f("fail")
