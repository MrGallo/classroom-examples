# Recursion-1 > powerN (p158888)

from solutions.powerN import powerN


def test_0():
    assert powerN(3, 1) == 3

def test_1():
    assert powerN(3, 2) == 9

def test_2():
    assert powerN(3, 3) == 27

def test_3():
    assert powerN(2, 1) == 2

def test_4():
    assert powerN(2, 2) == 4

def test_5():
    assert powerN(2, 3) == 8

def test_6():
    assert powerN(2, 4) == 16

def test_7():
    assert powerN(2, 5) == 32

def test_8():
    assert powerN(10, 1) == 10

def test_9():
    assert powerN(10, 2) == 100

def test_10():
    assert powerN(10, 3) == 1000
