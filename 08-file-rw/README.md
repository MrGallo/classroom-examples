# File Read/Write Section Goals
- [Write to a file](#write-to-a-file)
- [Read from a file](#read-from-a-file)
- [Append to a file](#append-to-file)
- [Read multiple lines from a file](#read-multiple-lines-from-a-file)
- [Store dictionary data as JSON](#store-dict-data-as-json)
- [Read in JSON data](#read-json-data)

## Write to a file
```python
with open("some_file.txt", 'w') as f:
    f.write("hello")
```

## Read from a file
```python
with open("some_file.txt", 'r') as f:
    contents = f.read()

print(contents)
```

## Append to file
Will populate a file with numbers 1-50. One number per line.
```python
with open("some_file.txt", "a") as f:
    for number in range(1, 51):
        f.write(number + "\n")
```

## Read multiple lines from a file
Each line should be stripped of any whitespace in the beginning and end the string.
```python
lines = []
with open("some_file.txt", "r") as f:
    for line in f:
        lines.append(line.strip())
```

# Store Dict data as JSON
```python
import json

some_dict = {
    "name": "Example",
    "color": "Blue",
    "height": 50,
    "is_happy": False
}

with open("data.json", "w") as f:
    json.dump(some_dict, f)
```

## Read JSON data
```python
import json


with open("data.json", "r") as f:
    # convert JSON to Python Dictionary
    data = json.load(f)
```