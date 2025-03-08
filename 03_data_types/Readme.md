# Data Type in Python

### Primitive Data Types (Always immutable)

1. `String (str)`
2. `Integer (int)`
3. `Float (float)`
4. `Boolean (bool)`
5. `Complex (complex)`
6. `Byte (bytes)`

### Non-Primitive Data Types (Can be mutable or immutable)

1. `List (list)`
2. `Tuple (tuple)`
3. `Set (set)`
4. `Frozen Set (frozenset)`
5. `Dictionary (dict)`
6. `Byte Array (bytearray)`
7. `Memory View (memoryview)`

### **Mutable vs Immutable**

#### Mutable

- Mutable objects can be modified after creation.
- Changes happen in the same memory location.
- Can be modified after copying (shallow copy affects original).
- May have higher memory usage due to in-place modifications.
- Mutable objects can't be hashed.
- No safe for multi-threading without locks.
- Examples: `list`, `dict`, `set`, `bytearray`

#### Immutable

- Immutable objects can't be modified after creation.
- A new object is created on modification.
- Copying creates a completely independent object.
- More memory efficient due to object reuse.
- Immutable objects are hashable.
- Safe for multi-threading as they can't change.
- Examples: `int`, `float`, `str`, `tuple`, `bool`, `frozenset`
