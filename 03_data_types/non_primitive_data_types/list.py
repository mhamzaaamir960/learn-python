

my_list = ["Hello world", 21, 3.14, [20, 30, 40]]
print(my_list)
print(type(my_list))


numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

# created an empty list using list() constructor
empty_list = list()
print(empty_list)

str_list = list("Python")
print(str_list)


# Accessing List Elements
# - You can access elements using indexing, slicing, and negative indexing.

# indexing
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[2])

# Negative Indexing
print(fruits[-1])
print(fruits[-2])

# slicing
print(fruits[1:2])
print(fruits[:3])
print(fruits[::2])


# Modifying a List
# - Since lists are mutable, we can change elements, add, and remove items.

# Changing Elements
fruits = ["Apple", "Banana", "Grapes", "Cherry"]
fruits[2] = "Orange"
print(fruits)

# Adding Elements
fruits.append("manogo".title())  # add element at end of list
fruits.insert(2, "Strawberry")  # insert element at defined index
print(fruits)

# Removing Elements
fruits.remove("Banana")  # find and remove element in list
fruits.pop()  # by default removes last element
print(fruits)

fruits.pop(1)  # removes element which exists on index 1
print(fruits)

del fruits[2]  # Deletes an element by index
print(fruits)

# clear a list
fruits = ["Apple", "Banana", "Grapes", "Cherry"]
print(fruits)  # ['Apple', 'Banana', 'Grapes', 'Cherry']
fruits.clear()
print(fruits)  # ['Apple', 'Banana', 'Grapes', 'Cherry']

# count the items in list
fruits = ["Apple", "Banana", "Apple", "Grapes", "Cherry", "Apple"]
print(fruits.count("Apple"))


# Iterating Through a List
# - You can iterate through a list using a for loop.

fruits = ["Apple", "Banana", "Grapes", "Cherry"]

for fruit in fruits:
    print(fruit)

# Using enumerate() to get index & value:
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Value: {fruit}")

# Sorting a List Permanently with the sort() Method

cars = ["bmw", "audi", "toyota", "mercedes"]
print(cars)
cars.sort()
print(cars)

# Reverse sort
cars = ["bmw", "audi", "toyota", "suzuki", "mercedes", "tesla"]
print(cars)
cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function

cars = ["bmw", "toyota", "suzuki", "audi", "mercedes"]
print(sorted(cars))

# Reverse Temporarily sort
print(sorted(cars, reverse=True))

# Printing a List in Reverse Order
cars = ["bmw", "toyota", "suzuki", "audi", "mercedes"]
cars.reverse()
print(cars)

# back tooriginal
cars.reverse()
print(cars)


# Find the length of list
cars = ["bmw", "toyota", "suzuki", "audi", "mercedes"]
print(len(cars))

# Looping Through an Entire List
names = ["Hamza", "Omer", "Ali", "Fazeel", "Wasif", "Ibrahim"]
for name in names:
    print(f"Welcome {name}! Hope you are doing well!")


# Using the range() Function
for value in range(0, 11):
    print(value)

# Add steps using range function
for value in range(0, 11, 2):
    print(value)

# Using range() to make list of numbers
numbers = list(range(1, 6))
print(numbers)

# Add steps using range() in list of numbers
numbers = list(range(1, 11, 2))
print(numbers)


squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
else:
    print(squares)

# Using:
#  - min()
#  - max()
#  - sum()

# using numerical numbers
digits = [2, 5, 7, 3, 9, 1, 8]
print(min(digits))
print(max(digits))
print(sum(digits))

# using string (min() and max())
names = ["Hamza", "Omer", "Ali", "Fazeel", "Wasif", "Ibrahim"]
print(min(names))  # prints name alphabatically in asseceding order
print(max(names))  # prints name alphabatically in decending order


# List Comprehensions
squares = [value ** 2 for value in range(1, 11)]
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # print players name 0 index to 3. 3 is not included
print(players[:4])  # print players from 0 index to 4.
print(players[0::2])
print(players[::-1])  # reverse the list

# Looping Through a Slice
for player in players[:3]:
    print(player.upper())


# copy a list through slicing
players2 = players[:]
print(players2)
players2[1] = "Smith"
print(players2)
