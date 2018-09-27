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
