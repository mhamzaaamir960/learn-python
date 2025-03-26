
# username = "Hamza Aamir"

# local scope
def greet():
    username = "Ali"  # local scope
    print(f"Hello, {username}")  # accessible inside function only


greet()
# print(username)  # Hamza Aamir


# Enclosing scope
def outer():
    x = 20  # Enclosing scope

    def inner():
        print(x)  # access y from enclosing scope

    inner()


outer()


# global scope
y = 30  # global scope variable


def sum(num):
    z = num + y  # access y from global scope
    print(z)


sum(10)

count = 0  # global variable


def counter():
    global count  # using global keyword to modify global variable in local scope
    count += 1
    print(count)


counter()
print(count)
counter()
print(count)
