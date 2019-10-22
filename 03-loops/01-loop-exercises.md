Create a loop that will:
1. print out the numebrs form 0-99 (inclusive)
2. print out the numbers from 50 to 100 counting by 5
3. Print out the numbers from 3 to 600 counting by 10
4. print out the numbers from 100 to 0 counding down by 7
5. add up all the numbers fom 50 to 75.
6. add up all the multiples of 5 from 0-100
7. add up all multiples of 3 and 5 from 100-200
8. add up all multiples of 7 and 11 from 0-1000 except the numbers divisible by both.

## Solutions
### 1
```python
count = 0

while count <= 99:
    print(count)
    count += 1
```

### 2
```python
count = 50

while count <= 100:
    print(count)
    count += 5
```

### 3
```python
i = 3
while i <= 600:
    print(i)
    i += 10
```

### 4
```python
count = 100
while count >= 0:
    print(count)
    count -= 7
```

### 5
```python 
count = 50
total = 0
while count <= 75:
    total += count
    count += 1
```

### 6
```python
count = 0
total = 0
while count <= 100:
    if count % 5 == 0:
        total += count
    count += 1

# OR
count = 0
total = 0
while count <= 100:
    total += count
    count += 5
```

### 7
```python
count = 100
total = 0
while count <= 200:
    if count % 3 == 0 or count % 5 == 0:
        total += count
    count += 1
```

### 8
```python
count = 0
total = 0
while count <= 1000:
    is_multiple_of_7 = count % 7 == 0
    is_multiple_of_11 = count % 11 == 0

    if is_multiple_of_7 and is_multiple_of_11:
        count += 1
        continue
    elif is_multiple_of_7 or is_multiple_of_11:
        total += count
    
    count += 1
```
