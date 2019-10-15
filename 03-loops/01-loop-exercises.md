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

### 5
```python 
count = 50
total = 0
while count <= 75:
    total += count
    count += 1
```