# Textbook-Tuesday Examples

## Rock wins!
#### Inspired by Chapter 4
We can start creating a rock, scissor, paper game with baby steps. Our goal is to simply: 
- get user input
- check if their choice was rock.
  - If it was rock, they win
  - Otherwise, they lose
```python
user_choice = input("Choose rock scissor or paper:")

if user_choice == 'rock':
    result = "win"
else:
    result = "lose"
```

## Keep asking!
#### Inspired by Chapter 4
Use a loop to continuously ask for user input while the input is invalid. Valid input is 'rock', 'scissors' or 'paper'. There can be a couple ways to do this.

Something to consider: how can these solutions accomodate responses with mixed case? E.g., `rOCk` would be considered invalid.

```python
user_choice = ""
while user_choice != 'rock' and user_choice != 'scissors' and user_choice != 'paper':
    user_choice = input("Please choose: 'rock', 'scissors', or 'paper':")
```

Using **`in`** with a list.
```python
user_choice = ""
while user_choice not in ['rock', 'scissors', 'paper']:
    user_choice = input("Please choose: 'rock', 'scissors', or 'paper':")
```

With infinite loop and `break`.
```python
while True:
    user_choice = input("Please choose: 'rock', 'scissors', or 'paper':")
    if user_choice == 'rock' or user_choice == 'scissors' or user_choice == 'paper':
        break
```
