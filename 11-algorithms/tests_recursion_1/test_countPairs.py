# Recursion-1 > countPairs (p154048)

from solutions.countPairs import countPairs


def test_0():
    assert countPairs("axa") == 1

def test_1():
    assert countPairs("axax") == 2

def test_2():
    assert countPairs("axbx") == 1

def test_3():
    assert countPairs("hi") == 0

def test_4():
    assert countPairs("hihih") == 3

def test_5():
    assert countPairs("ihihhh") == 3

def test_6():
    assert countPairs("ihjxhh") == 0

def test_7():
    assert countPairs("") == 0

def test_8():
    assert countPairs("a") == 0

def test_9():
    assert countPairs("aa") == 0

def test_10():
    assert countPairs("aaa") == 1
