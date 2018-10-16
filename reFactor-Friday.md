# reFactor Friday

When we program, we write code that just works.
The result will likely be a jumbled and ugly mess that only
the author can understand. To complete your code, you MUST
clean it up to make it more readable. 
Don't submit RUDE code!

### 1
```python
"""
Will take a two-digit number and swap the digits.
"""
a = int(input())
print(str(a % 10) + str(a //10))
```

### 2
```python
def get_guess(): 
    """Will take the user's guess. Ensures the input is valid.""" 
    validity = False 
    while validity == False: 
        letter = input('Enter a letter:') 
        if letter in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM" and len(letter) == 1: 
            validity = True 
        else: 
            print('Character is invalid. ', end='') 
    
        if validity == True: 
            return letter 
```

## Solutions

### 1
```python
number = int(input())

right_digit = str(number % 10)
left_digit = str(number // 10)

swapped_digits = right_digit + left_digit

print(swapped_digits)
```

### 2
```python
def get_guess(): 
    """Will take the user's guess. Ensures the input is valid.""" 
    while True:
        letter = input('Enter a letter:').lower()
        if letter.isalpha() and len(letter) == 1: 
            return letter
        
        print('Character is invalid. ', end='') 
```
