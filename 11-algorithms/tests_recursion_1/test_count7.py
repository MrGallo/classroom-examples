# Recursion-1 > count7 (p101409)

from solutions.count7 import count7


def test_0():
    assert count7(717) == 2

def test_1():
    assert count7(7) == 1

def test_2():
    assert count7(123) == 0

def test_3():
    assert count7(77) == 2

def test_4():
    assert count7(7123) == 1

def test_5():
    assert count7(771237) == 3

def test_6():
    assert count7(771737) == 4

def test_7():
    assert count7(47571) == 2

def test_8():
    assert count7(777777) == 6

def test_9():
    assert count7(70701277) == 4

def test_10():
    assert count7(777576197) == 5

def test_11():
    assert count7(99999) == 0

def test_12():
    assert count7(99799) == 1
