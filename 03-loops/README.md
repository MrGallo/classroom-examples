# Loops Section Goals
- [Print out something 5 times (**counter variable**)](#counter-variable)
- [Create a loop to count from 0 to 10](#count-from-0-to-10)
- [Count from 0 to 100 by 5](#)
- [Calculate the sum of the numbers from 1-10 (**accumulator variable**)](#accumulator-variable)
- [`break` out of a loop](#break)
- [Skip loop code (`continue`)](#continue)
- [Add up user input in a loop](#add-input-in-a-loop)
- [Stop gathering input with a sentinel value](#sentinal-value)
- [**Iterate** over a collection (lists, strings)](#loop-through-a-string)
- [Convert a while loop to a for loop](#convert-while-to-for)
- [Use a for loop with `range()`](#for-loop-with-range)
- Convert a for loop to a while loop
- [String building in a loop (**accumulator variable**)](#string-building)

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

## Accumulator Variable
```python
total = 0  # accumulator
i = 1  # counter
while i <= 10:
    total += i  # add to the accumulator
    i += 1  # increase the counter
```

## `break`
```python
i = 0

while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1

```

## `continue`
```python
i = 0

while i <= 10:
    if i == 5 or i == 7:
        i += 1
        continue
    print(i)
    i += 1
```

## Add Input in a Loop
This is broken down in three patterns:
1. Can I create a loop that iterates five times?
2. Can I take user input in the loop?
3. Can I use an accumulator variable to store the input?
```python
i = 0
total = 0

while i < 5:
    num = int(input("Enter number: "))
    total += num
    i += 1

print(total)
```

## Sentinel Value
```python
total = 0

while True:
    num = int(input("Enter number, -1 to stop: "))
    if num == -1:
        break
    total += num
    
print(total)
```

## Loop through a string
```python
name = "Mr. Gallo"

i = 0
while i < len(name):
    print(name[i])
    i += 1
```

## Loop through a list
```python
friends = ["Frank", "Sally", "Jimbo"]

i = 0
while i < len(friends):
    print(friends[i])
    i += 1
```

## Convert `while` to `for`
```python 
name = "Mr. Gallo"

i = 0
while i < len(name):
    character = name[i]
    print(character)
    i += 1

# Converted...
for character in name:
    print(character)
```

```python
friends = ["Frank", "Sally", "Jimbo"]

i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1

# Converted...
# For every friend in my list of friends
# print the friend
for friend in friends:
    print(friend)
```

## `for` loop with `range`
```python
# while loop print 50-100
i = 50
while i <= 100:
    print(i)
    i += 1

# range(start, end)... Goes up to, but, doesn't include the end
for num in range(50, 101):
    print(num)


# while loop print 1-25 by 5
i = 0
while i <= 25:
    print(i)
    i += 5

# range(start, end, step)
for num in range(0, 26, 5):
    print(num)

```

## String building
```python
# create a new string without any of the vowels.

# While loop version
some_string = "Hello, World!"
new_str = ""

for char in some_string:
    if char.lower() in "aeiou":
        new_str += char

print(new_str)
```
