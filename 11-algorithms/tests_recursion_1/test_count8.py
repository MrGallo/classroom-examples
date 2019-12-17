# Recursion-1 > count8 (p192383)

from solutions.count8 import count8


def test_0():
    assert count8(8) == 1

def test_1():
    assert count8(818) == 2

def test_2():
    assert count8(8818) == 4

def test_3():
    assert count8(8088) == 4

def test_4():
    assert count8(123) == 0

def test_5():
    assert count8(81238) == 2

def test_6():
    assert count8(88788) == 6

def test_7():
    assert count8(8234) == 1

def test_8():
    assert count8(2348) == 1

def test_9():
    assert count8(23884) == 3

def test_10():
    assert count8(0) == 0

def test_11():
    assert count8(1818188) == 5

def test_12():
    assert count8(8818181) == 5

def test_13():
    assert count8(1080) == 1

def test_14():
    assert count8(188) == 3

def test_15():
    assert count8(88888) == 9

def test_16():
    assert count8(9898) == 2

def test_17():
    assert count8(78) == 1
