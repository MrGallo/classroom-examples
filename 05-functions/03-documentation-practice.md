# Documentation Practice

For each function below, add **type annotations* and a *doc string*.

- [double_char](#double-char)
- [count_hi](#count-hi)
- [cat_dog](#cat-dog)
- [count_code](#count-code)
- [count_evens](#count-evens)
- [has_22](#has-22)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>



## double_char
```python
def double_char(text):
    new_str = ""
    for char in text:
        new_str += char * 2
    
    return new_str
```

## count_hi
```python
def count_hi(text):
    count = 0
    for i in range(len(text) - 1):
        if text[i:i+2] == "hi":
            count += 1
    
    return count
```

## cat_dog
```python
def cat_dog(text):
    diff = 0
    for i in range(len(text) - 2):
        slice = text[i:i+3]
        if slice == "cat": diff += 1
        elif slice == "dog": diff -= 1
    
    return diff == 0
```

## count_code
```python
def count_code(text):
    count = 0
    for i in range(len(text) - 3):
        slice = text[i:i+4]
        if slice[0:2] == "co" and slice[-1] == "e":
            count += 1
    
    return count
```


## count_evens
```python
def count_evens(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count
```

## has_22
```python
def has22(nums):
    for i, n in enumerate(nums):
        if i + 1 == len(nums):
            break
        if (n, nums[i+1]) == (2, 2):
            return True
        
    return False
```
