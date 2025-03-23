# Functions in Python

A function in python is a **block of resuable code** that performs a specific task. Functions help in code modularity, reusability, and organization by breaking complex problems into smaller and manageable parts.

## Function Syntax

### `def function_name(parameters):`

    Function body
    -  `return result`

- `def` => Used to define a function
- `function_name` => Then name of the function (must follow naming rules).
- `parameters` => Inputs that the function accepts (optional).
- `return` => (Optional) Returns a value from the function.

## Types of function

- Bulit-in function (`print()`, `len()`, `sum()`, `enumerate()`, etc)
- User-defined functions (Functions created by the user for specific tasks. `def my_func():`)
- Anonymous (`lambda function` `lambda x: x + 1`) => one-line functions.
- Recursive function (calls it-self, `factorial(n)`)
- Higher-order function (Takes or returns functions, `map(), filter()`)
- Generator Function (Uses `yield` for lazy evaluation, `def gen(): yield`)
- Decorator (Modifies another function, `@decorator`)
- Class Method (Uses `@classmethod`, modifies class, `def increment(cls)`)
- Static Method (Uses `@staticmethod`, no `self`, `def add(x,y)`)
- Coroutine (Pauses & resumes execution, `def coroutine(): yield`)

## Function Parameters and Arguments

- Positional Arguments (The order of arguments must match the function parameters)
- Default Arguments (if no value is provided, the default value is used.)
- Keyword Arguments (Arguments can be passed using key-value pairs)
- Variable-Length Arguments (`*args` and `**kwargs`)
  - `*args` => accepts multiple positional arguments.
  - `**kwargs` => accepts multiple keyword arguments.
