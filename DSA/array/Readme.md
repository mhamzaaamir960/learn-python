# Array (Static Array)

An array is a collection of elements, all have same data type, stored in contiguous memory locations. It is static in size, meaning the size is fixed at the time of its declaration.

## Key Characteristics

1. **Fixed Size:** Cannot resize once declared.
2. **Same data type:** Homogeneous elements.
3. **Indexed:** Access elements using indices (starts at 0).
4. **Fast Access:** Accessing an element by index is O(1) time.

## Pros

- Fast access to elements.
- Easy to implement.

## Cons

- Fixed size wastes memory if not used fully.
- Cannot easily insert/delete elements in the middle.

# Dynamic Array

A dynamic array is a resizeable array that automatically resizes itself when elements are added beyond its current capicity. It still uses a contiguous block of memory, but internally handles resizing.

## Pros

- Flexible size
- Easier to work with compared to static arrays.

## Cons

- Resizing is costly (during resize operation)
- Still not ideal for frequent insertions/deletions in the middle.

# Array Module in Python

The array module provides a specific-efficient array for storing elements of the same data type. It's closer to arrays in languages like C.

- It supports typecodes

| Code | C Type         | Python Type  | Size                                |
| ---- | -------------- | ------------ | ----------------------------------- |
| 'b'  | signed char    | int          | 1 byte                              |
| 'B'  | unsigned char  | int          | 1 byte                              |
| 'u'  | Py_UNICODE     | Unicode char | 2 bytes (deprecated in Python 3.3+) |
| 'h'  | signed short   | int          | 2 bytes                             |
| 'H'  | unsigned short | int          | 2 bytes                             |
| 'i'  | signed int     | int          | 4 bytes                             |
| 'I'  | unsigned int   | int          | 4 bytes                             |
| 'l'  | signed long    | int          | 4 bytes                             |
| 'L'  | unsigned long  | int          | 4 bytes                             |
| 'f'  | float          | float        | 4 bytes                             |
| 'd'  | double         | float        | 8 bytes                             |

## 📊 Comparison: array.array vs list

| Feature           | array.array                      | list                             |
| ----------------- | -------------------------------- | -------------------------------- |
| Data Type         | Homogeneous (same type)          | Heterogeneous (any type)         |
| Type Enforcement  | Yes (via type code)              | No                               |
| Performance       | Faster for numeric data          | Slightly slower                  |
| Memory Efficiency | More memory-efficient            | Uses more memory                 |
| Functionality     | Limited (basic array operations) | Very rich (slicing, mixed types) |
| Use Case          | Numeric data processing          | General-purpose collections      |
| Element Size      | Fixed (e.g. 4 bytes for `i`)     | Dynamic                          |
| NumPy Alternative | No broadcasting, limited ops     | Use NumPy for more feature       |

# Python List

In python a `list` is a dynamic array that:

- Can store elements of any data type.
- Can grow or shrink in size.
- Allows random access by index.

## Internal Implementation: How does a list work?

- Python lists are arrays of pointers to objects.
- It stores references to objects, not actual values.
- Backed by a contiguous memory block like C arrays.
- Automatically resizes when capicity is exceeded.
