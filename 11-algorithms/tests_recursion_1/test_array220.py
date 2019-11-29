# Recursion-1 > array220 (p173469)

from solutions.array220 import array220


def test_0():
    assert array220([1, 2, 20], 0) == True

def test_1():
    assert array220([3, 30], 0) == True

def test_2():
    assert array220([3], 0) == False

def test_3():
    assert array220([], 0) == False

def test_4():
    assert array220([3, 3, 30, 4], 0) == True

def test_5():
    assert array220([2, 19, 4], 0) == False

def test_6():
    assert array220([20, 2, 21], 0) == False

def test_7():
    assert array220([20, 2, 21, 210], 0) == True

def test_8():
    assert array220([2, 200, 2000], 0) == True

def test_9():
    assert array220([0, 0], 0) == True

def test_10():
    assert array220([1, 2, 3, 4, 5, 6], 0) == False

def test_11():
    assert array220([1, 2, 3, 4, 5, 50, 6], 0) == True

def test_12():
    assert array220([1, 2, 3, 4, 5, 51, 6], 0) == False

def test_13():
    assert array220([1, 2, 3, 4, 4, 50, 500, 6], 0) == True
