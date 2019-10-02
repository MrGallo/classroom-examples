import math


# test sum(numbers: List[float]) -> float
def test_sum():
    assert sum([]) == 0
    assert sum([1, 2, 3]) == 6
    assert sum([5, 5, 5]) == 15
    assert sum([1] * 1000) == 1000


# test math.ceil(float) -> int
def test_math_ceil():
    assert math.ceil(6.0001) == 7
    assert math.ceil(6.0) == 6
    assert math.ceil(6.9999) == 7


# test math.floor(float) -> int
# test f strings
# test .format()

