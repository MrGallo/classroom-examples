# Loops Section Goals
- [Print out something 5 times (**counter variable**)](#counter-variable)
- [Create a loop to count from 0 to 10](#count-from-0-to-10)
- [Count from 0 to 100 by 5](#)
- Calculate the sum of the numbers from 1-10 (**accumulator variable**)
- [`break` out of a loop](#break)
- Skip loop code (`continue`)
- Add up user input in a loop
- **Iterate** over a collection (lists, strings)
- Convert a while loop to a for loop
- Convert a for loop to a while loop

## Advanced
- For loop with `enumerate()`
- For loop with `zip()`
- itertools


## Counter Variable
```python
i = 0
while i < 5:
    print("hello")
    i += 1
```

## Count from 0 to 10
```python
i = 0

while i <= 10:
    print(i)
    i += 1
```

## Break
```python
i = 0

while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1

```