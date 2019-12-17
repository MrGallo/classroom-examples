# Recursion-1 > countHi (p184029)

from solutions.countHi import countHi


def test_0():
    assert countHi("xxhixx") == 1

def test_1():
    assert countHi("xhixhix") == 2

def test_2():
    assert countHi("hi") == 1

def test_3():
    assert countHi("hihih") == 2

def test_4():
    assert countHi("h") == 0

def test_5():
    assert countHi("") == 0

def test_6():
    assert countHi("ihihihihih") == 4

def test_7():
    assert countHi("ihihihihihi") == 5

def test_8():
    assert countHi("hiAAhi12hi") == 3

def test_9():
    assert countHi("xhixhxihihhhih") == 3

def test_10():
    assert countHi("ship") == 1
