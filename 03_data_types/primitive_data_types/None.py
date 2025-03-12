
print(type(None))  # NoneType

a = None
b = None
print(a == b)
print(a is b)


# Common use case

def greet(name=None):
    if name is None:
        return "Hello Guest!"
    return f"Hello, {name}"

print(greet())
print(greet("Hamza"))


student  = {"name": "Hamza", "age": None}
print(student["age"] is None)
