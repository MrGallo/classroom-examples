# Recursion-1 > sumDigits (p163932)

from solutions.sumDigits import sumDigits


def test_0():
    assert sumDigits(126) == 9

def test_1():
    assert sumDigits(49) == 13

def test_2():
    assert sumDigits(12) == 3

def test_3():
    assert sumDigits(10) == 1

def test_4():
    assert sumDigits(1) == 1

def test_5():
    assert sumDigits(0) == 0

def test_6():
    assert sumDigits(730) == 10

def test_7():
    assert sumDigits(1111) == 4

def test_8():
    assert sumDigits(11111) == 5

def test_9():
    assert sumDigits(10110) == 3

def test_10():
    assert sumDigits(235) == 10
