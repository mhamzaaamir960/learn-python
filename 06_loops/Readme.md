# Loops in Python

Loops allow us to execute a block of code multiple times based on a condition. They help automate repetitive tasks efficiectly.

## Types of loops in python

1. **`for` loop:** Iterates over a sequence (list, tuple, string, range, etc.).
2. **`while` loop:** Repeats as long as a condition is `True`.

- **Nested Loops:** Loops inside loops

## Loop Control Statements

1. **`break` (Exit Loop):** Stops the loop immediately.
2. **`continue` (Skip Iteration):** Skips the current iteration and moves to the next.
3. **`pass` (Do nothing):** Used as a placeholder when the loop structure is required but no logic is implemented yet.


## Inner working of loops
- Python loops internally use **iterators** and **condition checks**.

### How `for` loop works internally
- `for` loop calls the `iter()` function on the sequence.
- The `next()` function fetches the next value.
- The loop stops when `StopIteration` is raised.

### How `While` loop works internally
- Python checks the condition before each iteration.
- If `True`, the loop executes.
- If `False`, the loop stops.
