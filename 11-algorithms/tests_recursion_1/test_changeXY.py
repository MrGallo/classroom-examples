# Recursion-1 > changeXY (p101372)

from solutions.changeXY import changeXY


def test_0():
    assert changeXY("codex") == "codey"

def test_1():
    assert changeXY("xxhixx") == "yyhiyy"

def test_2():
    assert changeXY("xhixhix") == "yhiyhiy"

def test_3():
    assert changeXY("hiy") == "hiy"

def test_4():
    assert changeXY("h") == "h"

def test_5():
    assert changeXY("x") == "y"

def test_6():
    assert changeXY("") == ""

def test_7():
    assert changeXY("xxx") == "yyy"

def test_8():
    assert changeXY("yyhxyi") == "yyhyyi"

def test_9():
    assert changeXY("hihi") == "hihi"
