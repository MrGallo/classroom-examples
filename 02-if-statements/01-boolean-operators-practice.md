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
1. `True and True`
2. `False and True`
3. `1 == 1 and 2 == 1`
4. `"test" == "test"`
5. `1 == 1 or 2 != 1`
6. `True and 1 == 1`
7. `False and 0 != 0`
8. `True or 1 == 1`
9. `"test" == "testing"`
10. `1 != 0 and 2 == 1`
11. `"test" != "testing"`
12. `"test" == 1`
13. `not (True and False)`
14. `not (1 == 1 and 0 != 1)`
15. `not (10 == 1 or 1000 == 1000)`
16. `not (1 != 10 or 3 == 4)`
17. `not ("testing" == "testing" and "Zed" == "Cool Guy")`
18. `1 == 1 and not ("testing" == 1 or 1 == 0)`
19. `"chunky" == "bacon" and not (3 == 4 or 3 == 3)`
20. `3 == 3 and not ("testing" == "testing" or "Python" == "Fun")`

# Solutions
## Simple Boolean expressions
For the following, assume `x = 5`, `y = 7`, `z = 10`.
1. `True`
2. `False`
3. `True`
4. `False`
5. `True`

## Truth Tables
For the truth tables, see [If Statements Section Goals](https://github.com/MrGallo/classroom-examples/tree/master/02-if-statements/README.md)

For the examples, please submit your own and I'll place them here.

## Boolean Operator Practice
1. `True`
2. `False`
3. `False`
4. `True`
5. `True`
6. `True`
7. `False`
8. `True`
9. `False`
10. `False`
11. `True`
12. `False`
13. `True`
14. `False`
15. `False`
16. `False`
17. `True`
18. `True`
19. `False`
20. `False`
