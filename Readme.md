# What is Python?

Python is a **high-level, interpreted, dynamically typed** programming language known for its **simplicity, readability, and versatility**.  
It supports multiple programming paradigms, including **Object-Oriented, Procedural, and Functional programming**.

## Python Inner Workings

### Compilation to Bytecode
- Python source code is first **compiled** into **bytecode**, which is stored in the `__pycache__/` directory as `.pyc` files.
- This **bytecode is an intermediate representation**, not machine code.

### Bytecode Execution
- **Bytecode** is a set of low-level, **platform-independent** instructions for the **Python Virtual Machine (PVM)**.
- The **PVM (Python Interpreter)** reads and **executes the bytecode line by line**.

### Python Virtual Machine (PVM)
- The **PVM is platform-dependent**, meaning each operating system has its own version of the Python interpreter.
- The **PVM converts bytecode into machine code**, which is then executed by the system.
