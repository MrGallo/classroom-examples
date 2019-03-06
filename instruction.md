# Instruction
## Output
```python
name = "Frank"
age = 50

print("Hello, my name is " + name + ". I am " + str(age) + " years old.")  # concatenation (messy)
print(f"Hello, my name is {name}. I am {age} years old.")                  # f-strings     (clear)
print("Hello, my name is {}. I am {} years old.".format(name, age))        # "dot" format  (clear)
```

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

## Looping through iterables
```python
"""
- Iterables
    - Things through which you are ABLE TO ITERATE
    - Loop or go through them

- Strings
    - Iterate through a string and say each character.
    - "hello"
- Lists
- Tuples
- Ranges
"""

my_str = "hello"
for char in my_str:
    """For every character in the string my_str, print the character"""
    print(char)


numbers = [7, 7, 2, 7, 11]
for num in numbers:
    """For every number in the list of numbers, print the number."""
    print(num)


marks = [84, 89, 90, 45, 67]
for mark in marks:
    """For every mark in the list of marks, print the mark"""
    print(mark)


for num in range(10):
    """For every number in the range, print the number"""
    print(num)


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
