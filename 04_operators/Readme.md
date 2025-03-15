# Operators in Python

Operators in Python are special symbols that perform operations on variables and values.

- Python provides several type of operators including:
  - Arithmetic `+, - , *, /, //, %, **`
  - Comparision (Relational) `==, !=, <, >, >=, <=`
  - Logical `and, or, not`
  - Bitwise `&,|,^, ~, <<, >>`
  - Assignment `=, +=, -=, *=, /=, //=, %=, **=`
  - Identity `is, is not`
  - Membership `in, not in`

## Arithmetic Operators in Python

Arithmetic operators perform mathematical operations like addition, subtraction, multiplication, etc.

| Operator       | Symbol | Example       | Description                                  |
| -------------- | ------ | ------------- | -------------------------------------------- |
| Addition       | `+`    | `5 + 3 → 8`   | Adds two numbers                             |
| Subtraction    | `-`    | `5 - 3 → 2`   | Subtracts right operand from left            |
| Multiplication | `*`    | `5 * 3 → 15`  | Multiplies two numbers                       |
| Division       | `/`    | `5 / 2 → 2.5` | Divides left operand by right (float result) |
| Floor Division | `//`   | `5 // 2 → 2`  | Division result rounded down to integer      |
| Modulus        | `%`    | `5 % 2 → 1`   | Remainder after division                     |
| Exponentiation | `**`   | `5 ** 2 → 25` | Raises left operand to power of right        |

## Comparison (Relational) Operators in Python

Comparison operators compare values and return `True` or `False`.

| Operator              | Symbol | Example          | Description                                |
| --------------------- | ------ | ---------------- | ------------------------------------------ |
| Equal                 | `==`   | `5 == 3 → False` | Checks if two values are equal             |
| Not Equal             | `!=`   | `5 != 3 → True`  | Checks if two values are not equal         |
| Greater Than          | `>`    | `5 > 3 → True`   | Checks if left operand is greater          |
| Less Than             | `<`    | `5 < 3 → False`  | Checks if left operand is smaller          |
| Greater Than or Equal | `>=`   | `5 >= 5 → True`  | Checks if left operand is greater or equal |
| Less Than or Equal    | `<=`   | `5 <= 3 → False` | Checks if left operand is smaller or equal |

## Logical Operators in Python

Logical operators combine multiple conditions and return `True` or `False`.

| Operator | Symbol | Example                       | Description                            |
| -------- | ------ | ----------------------------- | -------------------------------------- |
| AND      | `and`  | `(5 > 3) and (10 > 5) → True` | True if both conditions are true       |
| OR       | `or`   | `(5 > 3) or (10 < 5) → True`  | True if at least one condition is true |
| NOT      | `not`  | `not(5 > 3) → False`          | Negates the condition                  |

## Bitwise Operators in Python

Bitwise operators perform operations on binary numbers.

| Operator    | Symbol | Example       | Description                               |
| ----------- | ------ | ------------- | ----------------------------------------- |
| AND         | `&`    | `5 & 3 → 1`   | Bits are compared, 1 if both bits are 1   |
| OR          | `\|`   | `5 \| 3 → 7`  | Bits are compared, 1 if at least one is 1 |
| XOR         | `^`    | `5 ^ 3 → 6`   | 1 if bits are different                   |
| NOT         | `~`    | `~5 → -6`     | Inverts all bits (-(x+1))                 |
| Left Shift  | `<<`   | `5 << 1 → 10` | Shifts bits left (multiply by 2)          |
| Right Shift | `>>`   | `5 >> 1 → 2`  | Shifts bits right (divide by 2)           |

## Assignment Operators

Assignment operators assign values to variables.

| Operator                | Symbol | Example   | Equivalent to             |
| ----------------------- | ------ | --------- | ------------------------- |
| Assign                  | `=`    | `x = 5`   | Assigns value to variable |
| Add and Assign          | `+=`   | `x += 3`  | `x = x + 3`               |
| Subtract and Assign     | `-=`   | `x -= 3`  | `x = x - 3`               |
| Multiply and Assign     | `*=`   | `x *= 3`  | `x = x * 3`               |
| Divide and Assign       | `/=`   | `x /= 3`  | `x = x / 3`               |
| Floor Divide and Assign | `//=`  | `x //= 3` | `x = x // 3`              |
| Modulus and Assign      | `%=`   | `x %= 3`  | `x = x % 3`               |
| Exponent and Assign     | `**=`  | `x **= 3` | `x = x ** 3`              |

## Identity Operators

Identity operators check if two variables reference the same object in memory.

| Operator | Symbol   | Example      | Description                              |
| -------- | -------- | ------------ | ---------------------------------------- |
| Is       | `is`     | `x is y`     | True if both reference the same object   |
| Is Not   | `is not` | `x is not y` | True if they reference different objects |

## Membership Operators

Membership operators check whether a value exists in a sequence (list, tuple, string, etc.).

| Operator | Symbol   | Example                     | Description                      |
| -------- | -------- | --------------------------- | -------------------------------- |
| In       | `in`     | `'a' in 'apple' → True`     | True if value is in sequence     |
| Not In   | `not in` | `'z' not in 'apple' → True` | True if value is not in sequence |
