# Recursion-1 > noX (p118230)

from solutions.noX import noX


def test_0():
    assert noX("xaxb") == "ab"

def test_1():
    assert noX("abc") == "abc"

def test_2():
    assert noX("xx") == ""

def test_3():
    assert noX("") == ""

def test_4():
    assert noX("axxbxx") == "ab"

def test_5():
    assert noX("Hellox") == "Hello"
