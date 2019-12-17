# Recursion-1 > changePi (p170924)

from solutions.changePi import changePi


def test_0():
    assert changePi("xpix") == "x3.14x"

def test_1():
    assert changePi("pipi") == "3.143.14"

def test_2():
    assert changePi("pip") == "3.14p"

def test_3():
    assert changePi("pi") == "3.14"

def test_4():
    assert changePi("hip") == "hip"

def test_5():
    assert changePi("p") == "p"

def test_6():
    assert changePi("x") == "x"

def test_7():
    assert changePi("") == ""

def test_8():
    assert changePi("pixx") == "3.14xx"

def test_9():
    assert changePi("xyzzy") == "xyzzy"
