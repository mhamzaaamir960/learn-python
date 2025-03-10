
name = "Hamza Aamir"
print(name)

# change the value of name variable
name = "Muhammad Omer Aamir"
print(name)

# error print is a reserved keyword
# print = "Hamza Aamir"
# print(print)


message = "Hello World"
# print(mesage) # error due to typo in variable name
print(message)


# use of underscore in variable names
full_name = "Muhammad Hamza Aamir"
print(full_name)


# Assign multiple variables

x, y, x = 50, 30, 50
print(type(x))


name, age, city = "Muhammad Hamza Aamir", 21, "Rawalpindi"
print(f"My name is {name}, I am {age} years old and I live in {city}")


# Assgin same value to multiple variables

a = b = c = 10
print(a, b, c)


# swaping variables (without using temp)
a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)


data = ("Hamza", 21, "Rawalpindi")
print(type(data))

name, age, city = data
print(name, age, city)
# print(data[0])
