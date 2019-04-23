# Assertions Section Goals
- [Test a custom function using assertions](#test-using-assertions)
- [Create a `tests` function for your assertions](#tests-function-for-assertions)
- [Create a test function for each of the functions you want to test](#test-function-for-each-function)


# Test Using Assertions
```python
def add(a, b):
    return a + b


assert add(3, 4) == 7
assert add(-2, -5) == -7
print("All tests passed!")
```

# Tests function for assertions
```python
def add(a, b):
    return a + b


def tests():
    assert add(3, 4) == 7
    assert add(-2, -5) == -7
    print("All tests passed!")


if __name__ == "__main__":
    tests()
```

# Test function for each function
```python

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def tests():
    test_add()
    test_sub()
    print("All tests passed!")


def test_add():
    assert add(3, 4) == 7
    assert add(-2, -5) == -7


def test_sub():
    assert sub(5, 3) == 2


if __name__ == "__main__":
    tests()
```
