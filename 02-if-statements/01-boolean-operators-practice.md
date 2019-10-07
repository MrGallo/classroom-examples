# Boolean Operators Practice

## Simple Boolean expressions
For the following, assume `x = 5`, `y = 7`, `z = 10`.
1. `x >= 5`
2. `y < x`
3. `y < 2 * y`
4. `z <= x`
5. `x + 5 == z`

## Truth Tables
Complete the truth tables for the following *Boolean operators*. For each operator, give a real-life example, in english and in pseudo code of the the operator in an if statement. See below `AND` for an example.

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
