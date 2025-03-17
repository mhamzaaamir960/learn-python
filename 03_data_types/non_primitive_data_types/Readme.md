# Non-Primitive Data Types (Can be mutable or immutable)

1. `List (list)`
2. `Tuple (tuple)`
3. `Set (set)`
4. `Frozen Set (frozenset)`
5. `Dictionary (dict)`
6. `Byte Array (bytearray)`
7. `Memory View (memoryview)`

## List (list)

A list is a built-in mutable data structure in Python that allows you to store ordered collections of items.

- A list can contain different data types such as integers, string, floats or even other lists.
- List is created using square brackets `[]` or `list()` constructor.

### List Characteristics

- `Ordered:` Items in a list maintain their insetion order (since Python 3.7)
- `Mutable:` List allow modifications (adding, removing, and uploading elements)
- `Allows Duplicates:` The same value can appear multiple times.
- `Heterogeneous:` Can store different data types in the same list.

### List Methods

List methods perform various operations on lists.

| Method         | Description                                            |
| -------------- | ------------------------------------------------------ |
| `append(x)`    | Adds item `x` to the end.                              |
| `insert(i, x)` | Inserts `x` at index `i`.                              |
| `remove(x)`    | Removes the first occurrence of `x`.                   |
| `pop(i)`       | Removes and returns item at index `i` (default: last). |
| `clear()`      | Removes all elements.                                  |
| `index(x)`     | Returns index of first occurrence of `x`.              |
| `count(x)`     | Returns number of times `x` appears.                   |
| `sort()`       | Sorts list in ascending order.                         |
| `reverse()`    | Reverses the order of elements.                        |
| `copy()`       | Returns a shallow copy of the list.                    |

## Tuple (tuple)

A tuple is an immutable, ordered collection of elements in Python. It is similar to list, but once a tuple is created, its elements cannot be changed, added or removed.

- Tuple can be created using:
  - Using parentheses `()`
  - Using `tuple()` constructor
  - Comma-seprated values (without parenthesis)

### Key Characteristics of Tuples

- `Ordered:` Items maintain the order in which they are added.
- `Immutable:` Cannot modify elements after creation.
- `Allows Duplicates:` The same element can appear multiple times.
- `Heterogeneous:` Can store different data types.
- `Faster than lists:` Accessing elements is quicker due to immutablity.

### Tuple Methods

| Method     | Description                                       |
| ---------- | ------------------------------------------------- |
| `count(x)` | Returns the number of occurrences of `x`.         |
| `index(x)` | Returns the index of the first occurrence of `x`. |

## Tuple vs List: Key Differences

| Feature          | Tuple                          | List                             |
| ---------------- | ------------------------------ | -------------------------------- |
| **Mutability**   | Immutable (cannot be modified) | Mutable (can be modified)        |
| **Performance**  | Faster (uses less memory)      | Slower (due to mutability)       |
| **Memory Usage** | Requires less memory           | Requires more memory             |
| **Use Case**     | Suitable for fixed collections | Suitable for dynamic collections |
