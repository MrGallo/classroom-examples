# Recursion-1 > countX (p170371)

from solutions.countX import countX


def test_0():
    assert countX("xxhixx") == 4

def test_1():
    assert countX("xhixhix") == 3

def test_2():
    assert countX("hi") == 0

def test_3():
    assert countX("h") == 0

def test_4():
    assert countX("x") == 1

def test_5():
    assert countX("") == 0

def test_6():
    assert countX("hihi") == 0

def test_7():
    assert countX("hiAAhi12hi") == 0
