# reFactor Friday

When we program, we write code that just works.
The result will likely be a jumbled and ugly mess that only
the author can understand. To complete your code, you MUST
clean it up to make it more readable. 
Don't submit RUDE code!

### 1.1
```python
"""
Will take a two-digit number and swap the digits.
"""
a = int(input())
print(str(a % 10) + str(a //10))
```



## Solutions

### 1.1
```python
number = int(input())

right_digit = str(number % 10)
left_digit = str(number // 10)

swapped_digits = right_digit + left_digit

print(swapped_digits)
```
