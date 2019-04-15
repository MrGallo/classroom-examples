# Introduction to Programming

## Topics
- Variables
    - Assignment operator
    - Variables as containers
- Datatypes
    - Integer
    - Float
    - String
    - Boolean
- Output
    - f-strings
    - `.format()`
- Input
    - Prompting
    - Type conversion

## Goals
- Get item cost and quantity. Calculate subtotal, tax, and total 💻
- Make change using modulus 💻
- Refactor variables from drawing 🕹️
- Get square to: 🕹️
    - move
    - accelerate

## Projects
- Math formula calculator
- Madlibs
- Point of Sale (quantity and total + make change)
- Arcade
    - artwork with variables
    - simple animation


```python
TAX_RATE = 0.13

item_cost = float(input("Item cost: "))
quantity = int(input("Quantity: "))

subtotal = item_cost * quantity
tax = subtotal * TAX_RATE
total = subtotal + tax

print()
print(f"Subtotal: ${round(subtotal, 2)}")
print(f"Tax: ${round(tax, 2)}")
print(f"Total: ${round(total, 2)}")

"""
variables
constants
variables calculated from other variables
datatypes string, int, float
datatype conversion
output
f strings or .format
round()
input
variables storing input
"""
```