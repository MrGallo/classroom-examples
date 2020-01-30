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
