# Recursion-1 > bunnyEars2 (p107330)

from solutions.bunnyEars2 import bunnyEars2


def test_0():
    assert bunnyEars2(0) == 0

def test_1():
    assert bunnyEars2(1) == 2

def test_2():
    assert bunnyEars2(2) == 5

def test_3():
    assert bunnyEars2(3) == 7

def test_4():
    assert bunnyEars2(4) == 10

def test_5():
    assert bunnyEars2(5) == 12

def test_6():
    assert bunnyEars2(6) == 15

def test_7():
    assert bunnyEars2(10) == 25
