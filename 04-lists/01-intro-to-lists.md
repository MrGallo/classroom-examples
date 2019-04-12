# Intro to Lists
```python
# Execute the commands from a Python shell. Don't type the comments.
# Element lookup and slicing:

>>> marks =  [6, 2, 8, 5, 0, 4, 1]   # Initalizing a list
>>> marks[0]                         # Access single element by index
6
>>> marks[3]
5
>>> marks[3:5]                       # Slice list from index 3 up to (not including) 5
[5, 0]
>>> marks[:5]                        # Slice list from beginning up to (not including) 5
[6, 2, 8, 5, 0]
>>> marks[3:]                        # Slice list from 3 to the end
[5, 0, 4, 1]
>>> marks[:-1]                       # Slice list from beginning to (not including) the last element
[6, 2, 8, 5, 0, 4]
>>> marks[:]                         # Slice from beginning to the end (copy whole list)
[6, 2, 8, 5, 0, 4, 1]
>>> marks[::2]                       # Slice from beginning to the end stepping by 2
[6, 8, 0, 1]
>>> marks[::-1]                      # Slice from beginning to the end backwards
[1, 4, 0, 5, 8, 2, 6]

>>> friends = ['Jim', 'Sally', 'Frank']
>>> friends.append("ABC")                   # .append() adds to a list
>>> friends
['Jim', 'Sally', 'Frank', 'ABC']
>>> friends.append("Bob")
>>> friends
['Jim', 'Sally', 'Frank', 'ABC', 'Bob']

>>> friends[2] = "Frankie"                  # Reassign a specific list element at index
>>> friends
['Jim', 'Sally', 'Frankie', 'ABC', 'Bob']

>>> friends.remove("Frankie")               # Search list for a specific value and remove it
>>> friends
['Jim', 'Sally', 'ABC', 'Bob']

>>> friends
['Jim', 'Sally', 'ABC', 'Bob']
>>> del friends[2]                          # Remove specific element at index
>>> friends
['Jim', 'Sally', 'Bob']
```
