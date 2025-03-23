
def greet():
    print("Welcome, User")


# greet()

# function with parameter


def greet_user(name):
    print(f"Welcome, {name}")


# greet_user("Hamza")

# with multiple parameters


def student_data(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")


# student_data("Hamza", 21, "Rawalpindi")

# function default parameter

def get_name(name="Hassan"):
    print(name)


get_name()
get_name("Hamza Aamir")

# multiple default parameters


def get_data(name="Hassan", age=18, city="Lahore"):
    print(f"Name: {name}, Age: {age}, City: {city}")


get_data()
get_data("Hamza")
get_data("Wasif", 17)
get_data("Ibrahim", 21, "Rawalpindi")


# function keyword arguments

get_data(city="Multan", name="Wahab", age=24)


