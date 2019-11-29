# Recursion-1 > nestParen (p183174)

from solutions.nestParen import nestParen


def test_0():
    assert nestParen("(())") == True

def test_1():
    assert nestParen("((()))") == True

def test_2():
    assert nestParen("(((x))") == False

def test_3():
    assert nestParen("((())") == False

def test_4():
    assert nestParen("((()()") == False

def test_5():
    assert nestParen("()") == True

def test_6():
    assert nestParen("") == True

def test_7():
    assert nestParen("(yy)") == False

def test_8():
    assert nestParen("(())") == True

def test_9():
    assert nestParen("(((y))") == False

def test_10():
    assert nestParen("((y)))") == False

def test_11():
    assert nestParen("((()))") == True

def test_12():
    assert nestParen("(())))") == False

def test_13():
    assert nestParen("((yy())))") == False

def test_14():
    assert nestParen("(((())))") == True
