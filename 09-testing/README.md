# Tests Section Goals

- [Create a simple test file](#create-simple-test-file)
- [Test an internal function](#test-internal-function)
- [Test an external function](#test-external-function)


## Create simple test file
Create a file with a name that starts with `test_`. For example, if you are testing a code in a file called `markbook.py`, call the test file `test_markbook.py`.

First, you should start with a test that fails. All tests need to be in a function that starts with `test_`.
```python
# test_example.py

def test_simple_example():
    assert True is False
```

Run the tests using `pytest` in the terminal. **Ensure** that it says one test failed.

Next, make the test pass:
```python
# test_example.py

def test_simple_example():
    assert True is True
```

Run the test with `pytest`. It should now be "green" and pass.

## Test internal function
Note: this is *not* how things are done in the real world, production code and test code must be in different files.
```python
# test_example.py


def add(a, b):
    return a + b


def test_add():
    assert add(1, 1) == 2
    assert add(3, 4) == 7
```

## Text external function
```python
# math_functions.py



def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```

```python
# test_math_functions.py


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```
