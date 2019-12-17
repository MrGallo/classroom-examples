# Recursion-1 > fibonacci (p120015)

from solutions.fibonacci import fibonacci


def test_0():
    assert fibonacci(0) == 0

def test_1():
    assert fibonacci(1) == 1

def test_2():
    assert fibonacci(2) == 1

def test_3():
    assert fibonacci(3) == 2

def test_4():
    assert fibonacci(4) == 3

def test_5():
    assert fibonacci(5) == 5

def test_6():
    assert fibonacci(6) == 8

def test_7():
    assert fibonacci(7) == 13
