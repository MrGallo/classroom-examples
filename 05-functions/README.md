# Functions Section Goals
- [Define and call a main function](#define-and-call-a-main-function)
- [**Define** a function](#define-and-call-custom-functions)
- [**Call** a function that you have defined](#define-and-call-custom-functions)
- [**Global** vs **local** variables](#global-vs-local-variables)
- Pass one or more values to a function (**Arguments** and **Parameters**)
- **Return** one or more results from a function
- [**Refactor** existing code into functions.](#refactor-existing-code)
- Test a function using **assertions**.
- Trace with the call-stack

## Define and call a main function
```python
def main():
    print("Hello, world!")


if __name__ == "__main__":
    main()
```

## Define and call custom functions
```python
def main():
    say_hello()
    say_hello()
    say_goodbye()


def say_hello():
    print("hello")


def say_goodbye():
    print("goodbye")


if __name__ == "__main__":
    main()
```
**Outputs:**
```
hello
hello
goodbye
```

# Global vs Local Variables
```python
x = 50

def main():
    x = 10
    print(x)

print(x)


if __name__ == "__main__":
    main()
    print(x)
```
Outputs:
```
50
10
50
```

```python
x = 50

def main():
    global x
    x += 10
    print(x)

print(x)


if __name__ == "__main__":
    main()
    print(x)
```
Outputs:
```
50
60
60
```
## Refactor Existing Code
Before:
```python
while True:
    print("menu list...")
    
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("invalid choice")
        continue
    
    if choice == 0:
        print("Zero stuff")
    elif choice == 1:
        print("one stuff")
    elif choice == 2:
        print("two stuff")
```
After:
```python
def main():
    while True:
        print("menu list...")
        
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("invalid choice")
            continue
        
        if choice == 0:
            zero_stuff()
        elif choice == 1:
            one_stuff()
        elif choice == 2:
            two_stuff()
    

def zero_stuff():
    print("Zero stuff")


def one_stuff():
    print("one stuff")


def two_stuff():
    print("two stuff")


if __name__ == "__main__":
    main()
```
