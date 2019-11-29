# Recursion-1 > allStar (p183394)

from solutions.allStar import allStar


def test_0():
    assert allStar("hello") == "h*e*l*l*o"

def test_1():
    assert allStar("abc") == "a*b*c"

def test_2():
    assert allStar("ab") == "a*b"

def test_3():
    assert allStar("a") == "a"

def test_4():
    assert allStar("") == ""

def test_5():
    assert allStar("3.14") == "3*.*1*4"

def test_6():
    assert allStar("Chocolate") == "C*h*o*c*o*l*a*t*e"

def test_7():
    assert allStar("1234") == "1*2*3*4"
