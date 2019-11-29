# Recursion-1 > stringClean (p104029)

from solutions.stringClean import stringClean


def test_0():
    assert stringClean("yyzzza") == "yza"

def test_1():
    assert stringClean("abbbcdd") == "abcd"

def test_2():
    assert stringClean("Hello") == "Helo"

def test_3():
    assert stringClean("XXabcYY") == "XabcY"

def test_4():
    assert stringClean("112ab445") == "12ab45"

def test_5():
    assert stringClean("Hello Bookkeeper") == "Helo Bokeper"
