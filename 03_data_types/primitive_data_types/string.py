

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

print(numbers[-5::-1])

# Reverse the string
print(numbers[::-1])
