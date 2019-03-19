# -*- coding: utf-8 -*-

from .context import src

def test_addition():
    assert src.addition(2,3) == 5

def test_soustraction():
    assert src.soustraction(4,3) == 1
