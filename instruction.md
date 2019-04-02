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

## Loops and user input

1. Create a program that takes 10 integers from the user as input and adds up all the numbers.
2. Create a program that takes 10 letters from the user and counts how many vowels were given.
```python
# 1
total = 0

for _ in range(10):
    num = int(input("Enter a number: "))
    total += num

print(total)


# 2
count = 0

for _ in range(10):
    letter = input("Enter a letter: ")
    if letter in 'aeiou':
        count += 1

print(count)

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

## Intro to Lists
```python
# Execute the commands from a Python shell. Don't type the comments.
# Element lookup and slicing:

>>> marks =  [6, 2, 8, 5, 0, 4, 1]   # Initalizing a list
>>> marks[0]                         # Access single element by index
6
>>> marks[3]
5
>>> marks[3:5]                       # Slice list from index 3 up to (not including) 5
[5, 0]
>>> marks[:5]                        # Slice list from beginning up to (not including) 5
[6, 2, 8, 5, 0]
>>> marks[3:]                        # Slice list from 3 to the end
[5, 0, 4, 1]
>>> marks[:-1]                       # Slice list from beginning to (not including) the last element
[6, 2, 8, 5, 0, 4]
>>> marks[:]                         # Slice from beginning to the end (copy whole list)
[6, 2, 8, 5, 0, 4, 1]
>>> marks[::2]                       # Slice from beginning to the end stepping by 2
[6, 8, 0, 1]
>>> marks[::-1]                      # Slice from beginning to the end backwards
[1, 4, 0, 5, 8, 2, 6]

>>> friends = ['Jim', 'Sally', 'Frank']
>>> friends.append("ABC")                   # .append() adds to a list
>>> friends
['Jim', 'Sally', 'Frank', 'ABC']
>>> friends.append("Bob")
>>> friends
['Jim', 'Sally', 'Frank', 'ABC', 'Bob']

>>> friends[2] = "Frankie"                  # Reassign a specific list element at index
>>> friends
['Jim', 'Sally', 'Frankie', 'ABC', 'Bob']

>>> friends.remove("Frankie")               # Search list for a specific value and remove it
>>> friends
['Jim', 'Sally', 'ABC', 'Bob']

>>> friends
['Jim', 'Sally', 'ABC', 'Bob']
>>> del friends[2]                          # Remove specific element at index
>>> friends
['Jim', 'Sally', 'Bob']
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
