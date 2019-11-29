# Recursion-1 > countAbc (p161124)

from solutions.countAbc import countAbc


def test_0():
    assert countAbc("abc") == 1

def test_1():
    assert countAbc("abcxxabc") == 2

def test_2():
    assert countAbc("abaxxaba") == 2

def test_3():
    assert countAbc("ababc") == 2

def test_4():
    assert countAbc("abxbc") == 0

def test_5():
    assert countAbc("aaabc") == 1

def test_6():
    assert countAbc("hello") == 0

def test_7():
    assert countAbc("") == 0

def test_8():
    assert countAbc("ab") == 0

def test_9():
    assert countAbc("aba") == 1

def test_10():
    assert countAbc("aca") == 0

def test_11():
    assert countAbc("aaa") == 0
