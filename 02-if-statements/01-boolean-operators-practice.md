# Boolean Operators Practice

## Simple Boolean expressions
For the following, assume `x = 5`, `y = 7`, `z = 10`.
1. `x >= 5`
2. `y < x`
3. `y < 2 * y`
4. `z <= x`
5. `x + 5 == z`

## Truth Tables
Complete the truth tables for the following *Boolean operators*. For each operator, give **three** real-life example, in english and in pseudo code of the the operator in an if statement. See below `AND` for an example.

### AND
For `and`, both conitions need to evaluate to `True`.

| A | B | A and B |
|:-:|:-:|:-------:|
| T | T |         |
| T | F |         |
| F | T |         |
| F | F |         |

**Examples**

### e.g.,
**Plain english**: `If you are older than 5 and taller than 100 cm, you can ride on the roller coaster.`

**Pseudo-code**:
```
if age > 5 and height > 100:
    you can ride
```

### OR
For `or`, only one condition needs to evaluate to `True`.

| A | B | A or B |
|:-:|:-:|:------:|
| T | T |        |
| T | F |        |
| F | T |        |
| F | F |        |

### NOT
`Not` will invert the Boolean value.

| A | not A |
|:-:|:-----:|
| T |       |
| F |       |

## Boolean Operator Practice
Evaluate the following to `True` or `False`. Examples from [Learn Python the Hard Way](http://cglab.ca/~morin/teaching/1405/lpthw/book/ex28.html).
1. True and True
2. False and True
3. 1 == 1 and 2 == 1
4. "test" == "test"
5. 1 == 1 or 2 != 1
6. True and 1 == 1
7. False and 0 != 0
8. True or 1 == 1
9. "test" == "testing"
10. 1 != 0 and 2 == 1
11. "test" != "testing"
12. "test" == 1
13. not (True and False)
14. not (1 == 1 and 0 != 1)
15. not (10 == 1 or 1000 == 1000)
16. not (1 != 10 or 3 == 4)
17. not ("testing" == "testing" and "Zed" == "Cool Guy")
18. 1 == 1 and not ("testing" == 1 or 1 == 0)
19. "chunky" == "bacon" and not (3 == 4 or 3 == 3)
20. 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
