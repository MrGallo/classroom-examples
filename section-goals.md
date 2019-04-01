# Section Goals
- [Lists](#lists-goals)
- [Exceptions](#exceptions-goals)

## Lists Goals
### 11
- [Count the number of words that start/end with a specific string.](#lists---count-prefix)
- [Find the largest item in a list](#lists---largest-item)
- [Items whose length is greater than a specific value.](#lists---count-larger-than)
- [Replace items that meet a certain criteria.](#lists---replace-with)
- [Filter a list (create a new list) of words to include only words that begin with a certain letter.](#lists---filter-first-letter)

[back to top](#section-goals)

### Lists - Count Prefix
```python
def count_prefix(word_list: List[str], prefix: str) -> int:
    """Count the number of words that start with a specific prefix."""
    count = 0
    for word in word_list:
        if word.startswith(prefix):
            count += 1
    return count
```
[back to list goals](#lists-goals)

### Lists - Largest Item
```python
def longest_string(word_list: List[str]) -> str:
    """Find the longest string in a list."""
    try:
        largest_word = word_list[0]
    except IndexError:
        return None
    
    for word in word_list:
        if len(word) > len(largest_word):
            largest_word = word
    return largest_word


def largest_number(number_list: List[float]) -> float:
    """Find the largest number in a list."""
    try:
        largest_number = number_list[0]
    except IndexError:
        return None

    for num in number_list:
        if num > largest_number:
            largest_number = num
    return largest_number
```
[back to list goals](#lists-goals)

### Lists - Count Larger Than
```python
def count_larger_than(numbers: List[int], target_size: int) -> int:
    """Return the number of elements larger than the target size."""
    count = 0
    for num in numbers:
        if num > target_size:
            count += 1
    
    return count
```
[back to list goals](#lists-goals)

### Lists - Replace with
With while loop:
```python
def replace_substring_with(words: List[str], substr: str, replacement: str) -> List[str]:
    i = 0
    while i < len(words):
        if words[i].find(substr) != -1:
            words[i] = replacement
        i += 1
    return words
```
With enumerate:
```python
def replace_with(words: List[str], search_string: str, replacement: str) -> List[str]:
    for i, word in enumerate(words):
        if word.find(search_string) != -1:
            words[i] = replacement
    return words
```
[back to list goals](#lists-goals)

### Lists - Filter first letter
```python
def filter_starts_with_letter(words: List[str], letter: str) -> List[str]:
    """Returns a filtered list of only the words that start with the given letter."""
    new_list = []
    for word in words:
        if word[0] == letter:
            new_list.append(word)
    return new_list
```
[back to list goals](#lists-goals)

## Exceptions Goals
### 11
- [Keep asking until inturrupt](#exceptions---keep-asking-if-not-int)
- [Ensure valid selection from menu](#exceptions---choose-valid-list-index)

[back to top](#section-goals)

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
[back to exceptions goals](#exceptions-goals)

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
[back to exceptions goals](#exceptions-goals)

