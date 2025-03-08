

first_name = "Muhammad Hamza"
last_name = "Aamir"
# Concatination (joining) of two strings
full_name = first_name + " " + last_name
# print(full_name)

# check the type of variable
# print(type(last_name))  # <class 'str'> means the variable type is stirng


# Single line string using single or double quotes
message = 'Hello, world!'
message = "Hello, World!"
# print(message)


# Multi-line string using triple single or double quotes
message2 = '''
Hi!
My name is Hamza.
I am from Pakistan.
This is multi-line string using single triple quotes.
'''
message2 = """
Hi!
My name is Hamza.
I am from Pakistan.
This is multi-line string using double triple quotes."""

# print(message2)


# Repitition of string
reps = "Hello, " * 5
# print(reps) # Hello, Hello, Hello, Hello, Hello,


# Indexing and Slicing

# Indexing
# print(full_name[0])  # M
# print(message[-2])  # d (-sign start indexing from end and last string exit on -1)


# Slicing  [start:end:step]
numbers = "3456587912"

# 34565 => it prints value from 0 index to 5 index  (5 is not included)
print(numbers[0:5])

# 7912 => it prints value form 6 index to 10 index (10 is not included)
print(numbers[6:10])

# 35571 => it print value from 0 index to 10 index with step of 2 e.g: (0, 2, 4, 6, 8)
print(numbers[0:10:2])

# -sign start indexing from end and last string exits on -1 in below it will print from start to second last but last two are not included.
print(numbers[:-2])

# due to -1 it will print reverse and from index 2 to 0
print(numbers[2::-1])

print(numbers[-5:])  # it start indexing from -5 to end
print(numbers[-5])  # it only print value which is at index -7

print(numbers[::])  # it print all the values
print(numbers[:])  # it print all the values

# it print values from index -5 to start with reverse order
print(numbers[-5::-1])

# it will print only one value
print(numbers[-5:-6:-1])

# Reverse the string
print(numbers[::-1])


# Case Conversion Methods
print(full_name.upper())
print(full_name.lower())
print(full_name.title())
print(full_name.capitalize())
print(full_name.swapcase())

s1 = "straße"   # German word for "street"
s2 = "STRASSE"

print(s1.lower() == s2.lower())    # False
print(s1.casefold() == s2.casefold())  # True (case-insensitive comparison)


# Searching & Replacing
# 1. User of .replace() method
# 2. Use of .find() method

name = "Muhammad Hamza Aamir"
print(name.replace("Hamza", "Omer"))  # Muhammad Omer Aamir
print(name.find("Hamza"))  # it returns the index of the finding string


# Splitting & Joining
# 1. use of .split() method
# 2. use of .join() method

fruits = "apple, banana, cherry"
print(fruits.split(", "))  # ['apple', 'banana', 'cherry']

fruits2 = ["apple", "banana", "cherry"]
print(", ".join(fruits2))  # apple banana cherry


# String formatting
# 1. using f-string (Python 3.6+)
# 2. using .format() method

# f-string using double quotes for single line string
name = "Muhammad Hamza Aamir"
age = 21
city = "Rawalpindi"
data = f"My name is {name}. I am {age} years old. I live in {city}."
print(data)

# f-string using triple double quotes for multi-line string
data = f"""My name is {name}. 
I am {age} years old.
I live in {city}."""
print(data)

# .format() method
data = """My name is {}. 
I am {} years old. 
I live in {}.""".format(name, age, city)
print(data)

