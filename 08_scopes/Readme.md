# Variable Scope in python

Scope in python refers to the region in the code where a variable is accessible. It defines the visibility and lifetime of a variable with in a program. Some types of scopes.

- Local Scope => A variable declared inside a function is considered local to that function and can be accessed only within that function.
- Enclosing Scope => Enclosing scope occurs in nested functions. If a variable is not found in the local scope, Python looks for it in the enclosing function.
- Global Scope => A variable declared outside any function is in the global scope and can be accessed anywhere in the script.

# Closures in Python

A closure is a function object that remembers values from its enclosing scope even after the scope has finished executing.

- Closures are created when:
  - A nested function references a variable from its enclosing function.
  - The enclosing function returns the nested function.
