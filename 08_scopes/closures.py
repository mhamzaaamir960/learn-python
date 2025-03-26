
def outer(num):

    def inner(x):
        return num ** x

    return inner


square = outer(4)
print(square(2))


def counter():
    count = 0  # Enclosing scope variable

    def increment():
        nonlocal count  # nonlocal keyword is used to modify the variable in enclosing scope
        count += 1
        return count
    return increment


c = counter()
print(c())
print(c())



def secret_data():
    secret = "This is a secret message"
    
    def get_secret():
        return secret
    return get_secret

get_secret_data = secret_data()
print(get_secret_data())
