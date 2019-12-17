# Recursion-1 > factorial (p154669)

from solutions.factorial import factorial


def test_0():
    assert factorial(1) == 1

def test_1():
    assert factorial(2) == 2

def test_2():
    assert factorial(3) == 6

def test_3():
    assert factorial(4) == 24

def test_4():
    assert factorial(5) == 120

def test_5():
    assert factorial(6) == 720

def test_6():
    assert factorial(7) == 5040

def test_7():
    assert factorial(8) == 40320

def test_8():
    assert factorial(12) == 479001600
