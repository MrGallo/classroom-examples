# Recursion-1 > array6 (p108997)

from solutions.array6 import array6


def test_0():
    assert array6([1, 6, 4], 0) == True

def test_1():
    assert array6([1, 4], 0) == False

def test_2():
    assert array6([6], 0) == True

def test_3():
    assert array6([], 0) == False

def test_4():
    assert array6([6, 2, 2], 0) == True

def test_5():
    assert array6([2, 5], 0) == False

def test_6():
    assert array6([1, 9, 4, 6, 6], 0) == True

def test_7():
    assert array6([2, 5, 6], 0) == True
