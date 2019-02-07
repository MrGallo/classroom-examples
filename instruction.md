# Instruction

## Input
```python

TAX_RATE = 0.13


print("Enter item cost:")
item_cost = float(input())

print("Enter quantity:")
quantity = int(input())

subtotal = item_cost * quantity
tax = subtotal * TAX_RATE
total_cost = subtotal + tax

print("Subtotal: $", subtotal)
print("Tax: $", tax)
print("Total: $", total_cost)

# some message with the total cost
# different ways you can format text
print()
print("Your total cost is:", total_cost)
print(f"Your total cost is: {total_cost}")
print("Your total cost is: {}".format(total_cost))

```

## Functions
```python
def print_sum(a, b):
    """Takes two numbers as arguments, but, does not return a value.
    Simply prints the sum to the console. This result is NOT retrieveable by the
    main program that called this function.
    
    Args:
        a (int): first number
        b (int): second number
    """
    print(a + b)


print_sum(5, 7)    # output: 13
print_sum(13, 10)  # output: 23
total = print_sum(1, 3)
print(total)  # output: None, because the function returned NOTHING to the main program.


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
