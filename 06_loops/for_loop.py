

from itertools import count
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)


print("\n")


# using range()
# range(start, end, step)

for num in range(1, 6):
    print(num)


# Iterating Over a String
word = "Python"
for letter in word:
    print(letter)

# Control Statements with for loops
# 1. break
# 2. continue
# 3. pass


# break => stops the loop immediately

numbers = [2, 65, 77, 23, 54, 93, 87, 45]
for num in numbers:
    print(num)
    if num == 93:
        break

print("\n")

# Using an Infinite Generator
for num in count(1):  # starts from 1 and never stops
    print(num)
    if num == 10:
        break  # Break the loop to avoid infinite exctuion


# continue => Skips the current iteration and moves to the next.

for num in range(1, 11):
    if num == 6:
        continue  # skips printing 3
    print(num)

cars = ["suzuki", "toyota", "audi", "mercedes", "bmw"]
for car in cars:
    if car == "audi":
        continue  # skips printing audi
    print(car)


# pass => does nothing but it prevents syntax error
for i in range(1, 6):
    pass  # Does nothing, prevents syntax error


# Nested Loops

for i in range(1, 6):
    for j in range(1, 6):
        print(f"({i}, {j})", end=" ")
    print(end="\n")


# Inner Working of Loops
numbers = [1, 2, 3, 4, 5]
iter_obj = iter(numbers)

print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

