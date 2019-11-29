# Recursion-1 > triangle (p194781)

from solutions.triangle import triangle


def test_0():
    assert triangle(0) == 0

def test_1():
    assert triangle(1) == 1

def test_2():
    assert triangle(2) == 3

def test_3():
    assert triangle(3) == 6

def test_4():
    assert triangle(4) == 10

def test_5():
    assert triangle(5) == 15

def test_6():
    assert triangle(6) == 21

def test_7():
    assert triangle(7) == 28
