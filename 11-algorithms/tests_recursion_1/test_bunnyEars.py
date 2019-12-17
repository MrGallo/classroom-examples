# Recursion-1 > bunnyEars (p183649)

from solutions.bunnyEars import bunnyEars


def test_0():
    assert bunnyEars(0) == 0

def test_1():
    assert bunnyEars(1) == 2

def test_2():
    assert bunnyEars(2) == 4

def test_3():
    assert bunnyEars(3) == 6

def test_4():
    assert bunnyEars(4) == 8

def test_5():
    assert bunnyEars(5) == 10

def test_6():
    assert bunnyEars(12) == 24

def test_7():
    assert bunnyEars(50) == 100

def test_8():
    assert bunnyEars(234) == 468
