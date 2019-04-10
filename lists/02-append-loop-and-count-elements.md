## Lists - Append in loop
```python
# create a loop that will read in 5 integer values into a list.

numbers = []  # initialize list
for pos in range(5):
    num = int(input(f"Enter a number ({pos+1} of 5): "))
    numbers.append(num)  # append number to list

print(numbers)
```

## Lists - Count Startswith
```python
# create a program that will count the number of words that start with 
# the letter "h"

words = ["hello", "hat", "bat", "shell", "tv", "livingroom", "heavy"]
count = 0
for word in words:
    if word.startswith("h"):  # modify to check first two letters
        count += 1

print(count)
