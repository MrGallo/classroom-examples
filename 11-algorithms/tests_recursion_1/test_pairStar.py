# Recursion-1 > pairStar (p158175)

from solutions.pairStar import pairStar


def test_0():
    assert pairStar("hello") == "hel*lo"

def test_1():
    assert pairStar("xxyy") == "x*xy*y"

def test_2():
    assert pairStar("aaaa") == "a*a*a*a"

def test_3():
    assert pairStar("aaab") == "a*a*ab"

def test_4():
    assert pairStar("aa") == "a*a"

def test_5():
    assert pairStar("a") == "a"

def test_6():
    assert pairStar("") == ""

def test_7():
    assert pairStar("noadjacent") == "noadjacent"

def test_8():
    assert pairStar("abba") == "ab*ba"

def test_9():
    assert pairStar("abbba") == "ab*b*ba"
