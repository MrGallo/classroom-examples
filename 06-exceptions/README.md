## Exceptions Goals
- [Keep asking until inturrupt](#exceptions---keep-asking-if-not-int)
- [Ensure valid selection from menu](#exceptions---choose-valid-list-index)


### Exceptions - Keep asking if not int
```python
total = 0
while True:
    try:
        num = int(input("Enter an integer, [ctrl+c] to stop: "))
    except ValueError:
        print(f"Error: not a valid integer. Try again.")
    except KeyboardInterrupt:
        print("DONE\n")
        break
    else:
        total += num

print(f"The sum of your numbers is: {total}")
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
