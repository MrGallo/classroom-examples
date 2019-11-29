# Recursion-1 > strCount (p186177)

from solutions.strCount import strCount


def test_0():
    assert strCount("catcowcat", "cat") == 2

def test_1():
    assert strCount("catcowcat", "cow") == 1

def test_2():
    assert strCount("catcowcat", "dog") == 0

def test_3():
    assert strCount("cacatcowcat", "cat") == 2

def test_4():
    assert strCount("xyx", "x") == 2

def test_5():
    assert strCount("iiiijj", "i") == 4

def test_6():
    assert strCount("iiiijj", "ii") == 2

def test_7():
    assert strCount("iiiijj", "iii") == 1

def test_8():
    assert strCount("iiiijj", "j") == 2

def test_9():
    assert strCount("iiiijj", "jj") == 1

def test_10():
    assert strCount("aaabababab", "ab") == 4

def test_11():
    assert strCount("aaabababab", "aa") == 1

def test_12():
    assert strCount("aaabababab", "a") == 6

def test_13():
    assert strCount("aaabababab", "b") == 4
