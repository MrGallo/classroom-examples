# Recursion-1 > endX (p105722)

from solutions.endX import endX


def test_0():
    assert endX("xxre") == "rexx"

def test_1():
    assert endX("xxhixx") == "hixxxx"

def test_2():
    assert endX("xhixhix") == "hihixxx"

def test_3():
    assert endX("hiy") == "hiy"

def test_4():
    assert endX("h") == "h"

def test_5():
    assert endX("x") == "x"

def test_6():
    assert endX("xx") == "xx"

def test_7():
    assert endX("") == ""

def test_8():
    assert endX("bxx") == "bxx"

def test_9():
    assert endX("bxax") == "baxx"

def test_10():
    assert endX("axaxax") == "aaaxxx"

def test_11():
    assert endX("xxhxi") == "hixxx"
