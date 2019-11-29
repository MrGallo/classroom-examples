# Recursion-1 > strDist (p195413)

from solutions.strDist import strDist


def test_0():
    assert strDist("catcowcat", "cat") == 9

def test_1():
    assert strDist("catcowcat", "cow") == 3

def test_2():
    assert strDist("cccatcowcatxx", "cat") == 9

def test_3():
    assert strDist("abccatcowcatcatxyz", "cat") == 12

def test_4():
    assert strDist("xyx", "x") == 3

def test_5():
    assert strDist("xyx", "y") == 1

def test_6():
    assert strDist("xyx", "z") == 0

def test_7():
    assert strDist("z", "z") == 1

def test_8():
    assert strDist("x", "z") == 0

def test_9():
    assert strDist("", "z") == 0

def test_10():
    assert strDist("hiHellohihihi", "hi") == 13

def test_11():
    assert strDist("hiHellohihihi", "hih") == 5

def test_12():
    assert strDist("hiHellohihihi", "o") == 1

def test_13():
    assert strDist("hiHellohihihi", "ll") == 2
