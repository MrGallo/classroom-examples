# Recursion-1 > strCopies (p118182)

from solutions.strCopies import strCopies


def test_0():
    assert strCopies("catcowcat", "cat", 2) == True

def test_1():
    assert strCopies("catcowcat", "cow", 2) == False

def test_2():
    assert strCopies("catcowcat", "cow", 1) == True

def test_3():
    assert strCopies("iiijjj", "i", 3) == True

def test_4():
    assert strCopies("iiijjj", "i", 4) == False

def test_5():
    assert strCopies("iiijjj", "ii", 2) == True

def test_6():
    assert strCopies("iiijjj", "ii", 3) == False

def test_7():
    assert strCopies("iiijjj", "x", 3) == False

def test_8():
    assert strCopies("iiijjj", "x", 0) == True

def test_9():
    assert strCopies("iiiiij", "iii", 3) == True

def test_10():
    assert strCopies("iiiiij", "iii", 4) == False

def test_11():
    assert strCopies("ijiiiiij", "iiii", 2) == True

def test_12():
    assert strCopies("ijiiiiij", "iiii", 3) == False

def test_13():
    assert strCopies("dogcatdogcat", "dog", 2) == True
