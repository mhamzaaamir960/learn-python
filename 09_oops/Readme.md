# Object-Oriented Programming (OOPs) in Python

Object-Oriented Programming (OOP) in Python is a paradigm that allows structuring code using objects and classes. Python follows OOP principles such as **Encapsulation**, **Inheritance**, **Polymorphism** and **Abstraction** to create reusable and organized code.

## Key OOP concepts in Python

- `Class`: A blueprint for creating objects.
- `Object`: An instance of a class with its own attributes. (In python both variables and methods are called attributes.)
- `Encapsulation`: Restricting direct access to object data using private and protected attributes.
  - Encapsulation uses access modifiers to control data access.
  - **Public** (`name`) - Accessible anywhere
  - **Protected** (`_name`) - Accessible within the class and subclass
  - **Private** (`__name`) - Accessible only within the class.
- `Inheritance`: Creating new classes based on existing ones to promote code reuse.
  - Inheritance enables reusability by deriving classes from a base class.
- `Ploymorphism`: Allowing objects of different classes to be treated as objects of a common superclass.
  - Polymorphism allows the same method (`make_sound()`) to behave differently in different classes.
- `Abstraction`: Hiding implementation details and exposing only neccessary parts.
  - Abstraction can be implemented using abstract classes (`ABC` module) to enforce method definitions.

### Attributes

- Attributes are member variables and member functions.

### Objects

- Object is an instance of a class.
- Objects are of two types: (One class has exactly one class object but can have any number of instance objects.)
  - class object
  - instance object

### variables

- Class object variables (Static variables)
- Instance object variables

### Methods

- Class Method
- Static Method
- Instance Method
