# Recursion-1 > array11 (p135988)

from solutions.array11 import array11


def test_0():
    assert array11([1, 2, 11], 0) == 1

def test_1():
    assert array11([11, 11], 0) == 2

def test_2():
    assert array11([1, 2, 3, 4], 0) == 0

def test_3():
    assert array11([1, 11, 3, 11, 11], 0) == 3

def test_4():
    assert array11([11], 0) == 1

def test_5():
    assert array11([1], 0) == 0

def test_6():
    assert array11([], 0) == 0

def test_7():
    assert array11([11, 2, 3, 4, 11, 5], 0) == 2

def test_8():
    assert array11([11, 5, 11], 0) == 2
