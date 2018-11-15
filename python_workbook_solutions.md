# The Python Workbook
The Missing Solutions

## Functions
### Exercise 81: Compute the Hypotenuse
```python
from math import sqrt


def hypotenuse(a, b):
    """Returns the length of the hypotenuse of a right-angle triangle.

    Args:
        a (float): Length of side A
        b (float): Length of side B

    Return:
        float: length of Hypotenuse
    """
    return sqrt(a*a + b*b)


def test_hypotenuse():
    assert hypotenuse(3, 4) == 5
    assert hypotenuse(6, 8) == 10
    print("Passed all tests", end="\n\n")


def main():
    print("Welcome to the Hypotenuse calculator")
    a = float(input("Enter side A:"))
    b = float(input("Enter side B:"))
    hypot = hypotenuse(a, b)
    print("The hypotenuse is: {}".format(hypot))


# test_hypotenuse()
main()
```
