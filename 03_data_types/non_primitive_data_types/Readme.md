# Non-Primitive Data Types (Can be mutable or immutable)

1. `List (list)`
2. `Tuple (tuple)`
3. `Dictionary (dict)`
4. `Set (set)`
5. `Frozen Set (frozenset)`
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

## Dictionary (dict)

A dictioary `dict` in Python is an unordered, mutable data structure that stores key-value pairs. It allows fast **lookups**, **insertions** and **deletions** because it is implemented using **hash tables**.

- Dict can be created using:
  - using curly braces `{}`
  - using `dict()` constructor

### Key Characteristics of Dictionary

- `Unordered:` The order of the items is not guaranteed.
- `Mutable:` You can change, add or remove key-value pairs.
- `Unique Key:` Key must be unique and duplicate keys overwrite previous values.
- `Immutable Key:` Strings, Numbers, and Tuples (immutalble objects) can be used as keys, but lists and dictionaries cannot used as keys.

### Dictionary Methods

| Method                    | Description                                                     |
| ------------------------- | --------------------------------------------------------------- |
| `dict.get(key, default)`  | Returns value of key, or default if key is missing.             |
| `dict.keys()`             | Returns all keys in dictionary.                                 |
| `dict.values()`           | Returns all values in dictionary.                               |
| `dict.items()`            | Returns all key-value pairs as tuples.                          |
| `dict.pop(key, default)`  | Removes key and returns value.                                  |
| `dict.popitem()`          | Removes and returns last inserted key-value pair (Python 3.7+). |
| `dict.update(other_dict)` | Merges another dictionary.                                      |
| `dict.clear()`            | Removes all elements.                                           |

## Set (set)

A set in Python is an unordered, mutable collection of unique, immutable elements. It is implemented using hash tables, making lookups, insertions and deletions very fast (`0(1)`) on average.

- Set can created using two ways:
  - Using curly braces `{}`
  - Using the `set()` constructor => `set()` must be used when creating empty set instead of curly `{}` braces.

### Properties of set

- `Unordered:` Items do not maintain a specific order.
- `Unique Elements:` Duplicates are automatically removed.
- `Mutable:` Items can be added or removed easily.

### Set Methods in Python

| Method                                  | Description                                                            |
| --------------------------------------- | ---------------------------------------------------------------------- |
| `set.add(item)`                         | Adds an item to the set.                                               |
| `set.remove(item)`                      | Removes an item (raises an error if missing).                          |
| `set.discard(item)`                     | Removes an item (does not raise an error if missing).                  |
| `set.pop()`                             | Removes and returns a random item.                                     |
| `set.clear()`                           | Removes all elements from the set.                                     |
| `set.union(set2)`                       | Returns the union of two sets.                                         |
| `set.update(set2)`                      | Adds all elements from `set2` to the original set.                     |
| `set.intersection(set2)`                | Returns the intersection of two sets.                                  |
| `set.intersection_update(set2)`         | Keeps only the elements that are also present in `set2`.               |
| `set.difference(set2)`                  | Returns elements in the first set that are not in the second set.      |
| `set.difference_update(set2)`           | Removes elements from the set that are also in `set2`.                 |
| `set.symmetric_difference(set2)`        | Returns elements unique to each set (excluding common elements).       |
| `set.symmetric_difference_update(set2)` | Updates the set to contain only elements that are unique to each set.  |
| `set.issubset(set2)`                    | Checks if the set is a subset of another set.                          |
| `set.issuperset(set2)`                  | Checks if the set is a superset of another set.                        |
| `set.isdisjoint(set2)`                  | Returns `True` if the sets have no common elements, otherwise `False`. |

### Key Differences: `{}` vs `set()`

| Feature                       | `{}` (Curly Braces)          | `set()` Constructor |
| ----------------------------- | ---------------------------- | ------------------- |
| Creating a set with elements  | ✅ Yes                       | ✅ Yes              |
| Creating an empty set         | ❌ No (Creates a dictionary) | ✅ Yes              |
| Converting iterables to a set | ❌ No                        | ✅ Yes              |
| Performance                   | ⚡ Faster                    | 🐢 Slightly Slower  |
