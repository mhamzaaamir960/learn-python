# Conditions in Python

Conditional statements in python allow a program to make decisions based on specific conditions. They help control the flow of exection by executing different code blocks depending on whether a condition is `True` or `False`.

Python provides the following conditional statements:

1. **`if` statement**: Executes a block of code if a condition is `True`.
2. **`if-else` statement**: Executes one block if the condition is `True`, otherwise executes another block.
3. **`if-elif-else` statement**: Checks multiple conditions in sequence.
4. **Nested `if` statements**: An `if` statement inside another `if` statement.

## Boolean Expressions and Truthy/Falsy Values

Python treats some values as `True` or `False` even without an explicit True or False condition.

### Truthy Values:

- Non-zero numbers `(1, -1, 2.5)`
- Non-empty strings `("Hello")`
- Non-empty lists, tuples, sets, dictionaries (`[1]`, `(2,)`, `{"a": 1}`)

### Falsy Values:

- `0`, `0.0`, `0j` (zero in different types)
- `""` (empty string)
- `[]`, `{}`, `set()` (empty collections)
- `None`


### Ternary Operator in Python?

A ternary operator in Python is a one-liner if-else statement that allows you to assign values based on a condition in a concise way.

- **Syntax**: `value_if_true if condition else value_if_false`
