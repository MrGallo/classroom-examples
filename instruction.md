# Instruction
## Functions
```python
def print_sum(a, b):
    """Function that takes arguments, but,
    does not return a value
    """
    print(a + b)


print_sum(5, 7)    # output: 13
print_sum(13, 10)  # output: 23


def sum(a, b):
    """Takes two numbers as arguments and returns the sum
    Args:
        a (int): first number
        b (int): second number
    Return:
        (int): sum of the two numbers
    """
    return a + b

balance = 1000
balance = sum(balance, 200)  # balance: 1200
```
