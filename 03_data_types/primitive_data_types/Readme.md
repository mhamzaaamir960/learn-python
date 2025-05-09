# Primitive Data Types in Python

- String (str)
- Integer (int)
- Float (float)
- Complex (complex)
- Boolean (bool)

## String (str)

- A string `(str)` in Python is a sequence of characters enclosed in single('), double(") or triple quotes (''' or """).
- It is immutable (unchangable) data type.

#### String Methods

1. `.upper()` => All letters will be capital letters.
2. `.lower()` => All letters will be small letters.
3. `.title()` => The first letter of each word will be capital.
4. `.capitalize()` => First letter of first word will be capital.
5. `.swapcase()` => Swap letters (small letters will be capital and capital letters will be small)
6. `.casefold()` => It converts text to lowercase more aggressively than `.lower()`, making it ideal for case-insensitive comparisons, especially in multilingual text.

## Integer (int)

The integer `(int)` data type is used to represent whole numbers, both positive and negative including zero. Python integers have arbitary precision, meaning they can grow as large as the available memory allows. It does not have fixed no. of bits for integers.

## Float (float)

A `float` (floating-point number) is a numeric data type used to represent decimal numbers. It supports positive and negative values including scientific notation.

## Boolean (bool)

A Boolean (`bool`) is data type in python that represents two possible values which is `True` or `False`.

- Python boolean data type is based on integer values
  - `True` is internally represented as `1`.
  - `False` is internally represented as `2`.
  - Example: True + True = 2


## Complex (complex)

Python has a built in complex number type, denoted as `complex`, which is used for mathematical computations involving imaginary numbers.
- Complex numbers are represented as `a+bj`.
  - `a` is real part (a float or integer).
  - `b` is imaginary part (a float or integer).
  - `j` represents the imaginary unit (equivalent to sqrt(-1)).


### None

In Python `None` is a special singletion object that represents the null value.
- None is not same as `0`, an empty string `("")` or `False`. It has its own data type
- None belongs to `NoneType`.
- It is used to signify that a variable has no value or that a function returns nothing.

