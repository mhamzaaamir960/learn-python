# Using parentheses
import sys
tuple1 = (1, 2, 3, "Hello")
print(f'Tuple 1: {tuple1}')

# Without parentheses
tuple2 = 10, 20, 30  # Automatically treated as a tuple
print(f'Tuple 2: {tuple2}')


# using tuple() constructor
tuple3 = tuple([2, 3, 4])
print(f'Tuple 3: {tuple3}')


# Creating a single-element tuple (comma required)
single_element_tuple = (5,)  # Correct
not_a_tuple = (5)  # Incorrect, treated as an integer


print(type(single_element_tuple))  # <class 'tuple'>
print(type(not_a_tuple))  # <class 'int'>


# Accessing Tuple Elements
# 1. Indexing
# 2. Negative Indexing
# 3. Slicing

# Indexing
fruits = ("apple", "banana", "cherry")
print(fruits[0])  # apple
print(fruits[2])  # cherry

# Negative Indexing
print(fruits[-1])  # cherry
print(fruits[-2])  # banana

# slicing
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])  # (20, 30, 40)
print(numbers[:3])   # (10, 20, 30)
print(numbers[::2])  # (10, 30, 50)


# Tuple Operations
# 1. Concatination
# 2. Repetition
# 3. Membership Test
# 4. Tuple Unpacking

# Concatination
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 10)
result = tuple1 + tuple2
print(type(result))
print(result)

# Repetition
tuple3 = ("Hello",) * 3
print(tuple3)

# Membership Test
print(3 in (1, 2, 3, 4, 5))
print("wo" in "Hello world!")

# Tuple Unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"x value: {x}, z value: {z}, y value: {y}")


# Tuple Methods
# .count()
# .index()

numbers = (4, 3, 8, 9, 6, 5, 7, 3, 2, 9, 3, 8, 3)
print(numbers.count(3))  # counts the no. of item in list
print(numbers.index(8))  # return value at index

# Inner Working & Memory Efficiency
#  How Tuples Store Data
#      Tuples store references (pointers) to objects, just like lists.
#      Since tuples are immutable, Python optimizes their storage to be more memory-efficient than lists.

list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print(sys.getsizeof(list_data))  # More memory
print(sys.getsizeof(tuple_data))  # Less memory


# When to Use Tuples?
# When data should remain constant – E.g., Days of the week:
# When you want to use tuples as dictionary keys

days_of_week = ("Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday")
print(days_of_week)

coordinates = {(10, 20): "Point A", (30, 40): "Point B"}
print(coordinates[(30, 40)])

# Copying Tuples
t1 = (1, 2, 3)
t2 = t1
print(t1 is t2)

# Loop values of tuple
dimensions = (300, 150)

print("Original Dimensions")
for dimension in dimensions:
    print(dimension)

dimensions = (500, 250)
print("\nModified Dimensions")
for dimension in dimensions:
    print(dimension)
