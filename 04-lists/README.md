# Lists Section Goals
- [Append user input to a list using a loop](#append-in-loop)
- [Count the number of words that start/end with a specific string](#count-startswith)
- [Check if a value is in a list](#search-list)
- [Find the largest item in a list](#find-largest)
- [Filter a list](#filter-a-list)

## Append in loop
```python
# create a loop that will read in 5 integer values into a list.

numbers = []  # initialize list
for _ in range(5):
    num = int(input(f"Enter a number: "))
    numbers.append(num)  # append number to list

print(numbers)
```

## Count Startswith
```python
# create a program that will count the number of words that start with 
# the letter "h"

words = ["hello", "hat", "bat", "shell", "tv", "livingroom", "heavy"]
count = 0
for word in words:
    if word.startswith("h"):  # modify to check first two letters
        count += 1

print(count)
```

## Search list
```python
# Create a program that will search a list for a particular value and print out its index location.
words = ["one", "two", "three", "four", "five"]

target = input("Enter search-word: ")
index = -1
i = 0
while i < len(words):
    word = words[i]
    if word == target:
        index = i
        break
    i += 1

print(index)
```

## Find largest
```python
# Create a program that will scan a list for the largest value and print out the value.
marks = [65, 87, 34, 98, 33, 75, 12, 76, 99, 76]

highest = marks[0]
for mark in marks:
    if mark > highest:
        highest = mark

print(highest)
```

## Filter a List
```python
# Create a copy of an integer list, but only the values which are greater than or equal to 50.
```

```python
# Filter out all strings from a list that start with the letter a.
```
