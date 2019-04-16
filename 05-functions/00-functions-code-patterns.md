# Code Patterns: Functions
- [Create main](#create-main)
- [Refactor main](#refactor-main)
- [Increase global x](#increase-global-x)
- [Increase global x by](#increase-global-x-by)
- [Get Answer to Life](#get-answer-to-life)
- Param and Return

## Create main
Create a `main` function whose only purpose is to print out the phrase `Hello, Functions!`

*Master*  00:30
*Gold*    00:40
*Silver*  00:50
*Bronze*  01:00

*Prerequisets*:
Output,
If Statements

*Resources*: [video](https://youtu.be/hx3W2aiv14c), [code](#code-create-main)

[[top]](#)

## Refactor main
Take the code below and put it in a `main` function. Keep the constant `TAX_RATE` at the global level, at the top of your code, outside of the `main` function.

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
```

*Master*  00:30
*Gold*    00:40
*Silver*  00:50
*Bronze*  01:00

*Prerequisets*:
If Statements,
[Create Main](#create-main)

*Resources*: [video](https://youtu.be/ISSPKc1YMFw), [code](#code-refactor-main)

[[top]](#)

## Increase Global x
Create:
- Global variable called `x`
- Function called `increase_x`
    - The `increase_x` function will increase the value of the global variable `x` by `1` each time it is called.
- A `main` function that will call the `increase_x` function and `print` the value of `x`.

*Master*  00:35
*Gold*    00:50
*Silver*  01:10
*Bronze*  01:30

*Prerequisets*:
[Create Main](#create-main)

*Resources*: [video](https://youtu.be/rHf7JbtLJVk), [code](#code-increase-global-x)

[[top]](#)


## Increase Global x by
- Create a global variable called `x`
- Create a function called `increase_x_by`. It will have one **parameter** called `amount` which will be the number by which to increase the global variable `x`.
- Create a `main` function that will call the `increase_x_by` function and pass `5` as the argument and then print the altered value of global variable `x`.

*Master*  00:50
*Gold*    01:10
*Silver*  01:30
*Bronze*  02:00

*Prerequisets*:
[Increase Global x](#increase-global-x)

*Resources*: [video](https://youtu.be/BJTKpFjSoNk), [code](#code-increase-global-x-by)

[[top]](#)

## Get Answer to Life
Create a `main` function that will call the function `get_answer_to_life` and store it in a local variable called `answer`. Have the `main` function print the secret. The `get_answer_to_life` function will simply `return 42`.

*Master*  00:40
*Gold*    01:00
*Silver*  01:20
*Bronze*  01:40

*Prerequisets*:
[Refactor main](#refactor-main)

*Resources*: [video](https://youtu.be/oM1AE7s7UvU), [code](#code-get-answer-to-life)

[[top]](#)


# Code
### Code: Create Main
```python
def main():
    print("Hello, Functions!")


if __name__ == "__main__":
    main()
```
[[back]](#create-main)


### Code: Refactor Main
```python
TAX_RATE = 0.13 


def main():
    item_cost = float(input("Item cost: "))
    quantity = int(input("Quantity: "))

    subtotal = item_cost * quantity
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    print()
    print(f"Subtotal: ${round(subtotal, 2)}")
    print(f"Tax: ${round(tax, 2)}")
    print(f"Total: ${round(total, 2)}")


if __name__ == "__main__":
    main()
```
[[back]](#refactor-main)


### Code: Increase Global x
```python
x = 5


def main():
    increase_global_x()
    print(x)


def increase_global_x():
    global x
    x += 1


if __name__ == "__main__":
    main()
```
[[back]](#increase-global-x)


### Code: Increase Global x By
```python
x = 50


def main():
    increase_global_x_by(5)
    print(x)


def increase_global_x_by(amount):
    global x
    x += amount


if __name__ == "__main__":
    main()
```
[[back]](#increase-global-x-by)


### Code: Get Answer to Life
```python
def main():
    answer = get_answer_to_life()
    print(answer)


def get_answer_to_life():
    return 42


if __name__ == "__main__":
    main()
```
[[back]](#get-answer-to-life)
