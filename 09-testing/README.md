# Tests Section Goals

- [Create a simple test file](#create-simple-test-file)


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