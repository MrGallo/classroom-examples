# File Read/Write Section Goals
- [Write to a file](#write-to-a-file)
- [Read from a file](#read-from-a-file)
- Append to a file
- Read multiple lines from a file
- Store dictionary data as JSON
- Read in JSON data

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
