# Recursion-1 > countHi2 (p143900)

from solutions.countHi2 import countHi2


def test_0():
    assert countHi2("ahixhi") == 1

def test_1():
    assert countHi2("ahibhi") == 2

def test_2():
    assert countHi2("xhixhi") == 0

def test_3():
    assert countHi2("hixhi") == 1

def test_4():
    assert countHi2("hixhhi") == 2

def test_5():
    assert countHi2("hihihi") == 3

def test_6():
    assert countHi2("hihihix") == 3

def test_7():
    assert countHi2("xhihihix") == 2

def test_8():
    assert countHi2("xxhi") == 0

def test_9():
    assert countHi2("hixxhi") == 1

def test_10():
    assert countHi2("hi") == 1

def test_11():
    assert countHi2("xxxx") == 0

def test_12():
    assert countHi2("h") == 0

def test_13():
    assert countHi2("x") == 0

def test_14():
    assert countHi2("") == 0

def test_15():
    assert countHi2("Hellohi") == 1
