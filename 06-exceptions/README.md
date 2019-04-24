## Exceptions Goals
- [Catch an error from user input](#catch-user-input-error)
- [Keep asking until inturrupt](#exceptions---keep-asking-if-not-int)
- [Ensure valid selection from menu](#exceptions---choose-valid-list-index)


### Catch User Input Error
Start with...
```python
num = int(input("Enter a number: "))
result = num * 2
print(f"{num} * 2 = {result}")
```
Solution:
```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("OOPS. Cant convert that to int.")
else:
    result = num * 2
    print(f"{num} * 2 = {result}")
```

### Exceptions - Keep asking if not int
```python
while True:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("OOPS. Cant convert that to int.")
    else:
        break

result = num * 2
print(f"{num} * 2 = {result}")
```

### Exceptions - Choose valid list index
```python
word_list = [...]  # some list of words

while True:
    # Print out the menu options
    print("Select a list item from the menu:")
    for i, word in enumerate(word_list):
        print(f"[{i}] {word}")

    try:
        index = int(input("Your choice: "))
        selected_word = word_list[index]
    except ValueError:
        print(f"Error: not a valid integer. Try again.")
    except IndexError:
        print(f"Not a valid menu option. Press [Enter] to try again.")
        input()
    else:
        break

print(f"Your chose: {selected_word}")
```
