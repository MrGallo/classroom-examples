# Recursion-1 > parenBit (p137918)

from solutions.parenBit import parenBit


def test_0():
    assert parenBit("xyz(abc)123") == "(abc)"

def test_1():
    assert parenBit("x(hello)") == "(hello)"

def test_2():
    assert parenBit("(xy)1") == "(xy)"

def test_3():
    assert parenBit("not really (possible)") == "(possible)"

def test_4():
    assert parenBit("(abc)") == "(abc)"

def test_5():
    assert parenBit("(abc)xyz") == "(abc)"

def test_6():
    assert parenBit("(abc)x") == "(abc)"

def test_7():
    assert parenBit("(x)") == "(x)"

def test_8():
    assert parenBit("()") == "()"

def test_9():
    assert parenBit("res (ipsa) loquitor") == "(ipsa)"

def test_10():
    assert parenBit("hello(not really)there") == "(not really)"

def test_11():
    assert parenBit("ab(ab)ab") == "(ab)"
