# How generator functions work?
# Instead of using return, generator functions use yield keyword to produce values on demand.

def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()
try:
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
except StopIteration:
    print("Generator is finished")


# Key Differences from regular functions
# A normal function returns all values at once and terminates.
# A generator function returns one value at a time, and remembers where it left off.

# countdown generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1


# for i in countdown(5):
#     print(i)

# Generating infinite sequences
# You cannot create infinite lists, but you can make an infinite generator.


def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1

# infinite loop
# for num in infinite_numbers():
#     print(num)


# for num in infinite_numbers():
#     print(num)
#     if num == 20:
#         break

# or

nums = infinite_numbers()
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print infinite numbers


def square_numbers(n):
    for i in range(n):
        yield i * i


squares = square_numbers(5)
print(next(squares))
print(next(squares))
print(list(squares))


# key Takeways
# 1. Use regular funcitons when you need all results at once.
# 2. Use generator functions when handling large data efficiently.
# 3. Generators are best for infinite sequences or streams of data.

# Generators = less memory usage + better performance
