# Recursion-1 > count11 (p167015)

from solutions.count11 import count11


def test_0():
    assert count11("11abc11") == 2

def test_1():
    assert count11("abc11x11x11") == 3

def test_2():
    assert count11("111") == 1

def test_3():
    assert count11("1111") == 2

def test_4():
    assert count11("1") == 0

def test_5():
    assert count11("") == 0

def test_6():
    assert count11("hi") == 0

def test_7():
    assert count11("11x111x1111") == 4

def test_8():
    assert count11("1x111") == 1

def test_9():
    assert count11("1Hello1") == 0

def test_10():
    assert count11("Hello") == 0
