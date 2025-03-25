
from functools import reduce
def square(x): return x * x
# print(square(5))


greeting = lambda name = "Hassan": print("Welcome, " + name)
# greeting("Omer")


def sum_of_two_number(x, y): return x + y
# print(sum_of_two_number(5,6))


sum_of_numbers = lambda *x: sum(x)
# print(sum_of_numbers(1,2,3,4,5))

student_data = lambda **kwargs: kwargs
data = student_data(name="Hamza", age=21, city="Rawalpindi")
# print(data)


cube = (lambda x: x*x*x)(3)
print(f"Cube: {cube}")


# using map() function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x*x, numbers))
# print(f"Squared Numbers: {squared_numbers}")
# map(function, iterablep)

# using filter() function
# filter(function, iterable)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(f"Even Numbers: {even_numbers}")

# using reduce() function
# reduce(function, iterable)
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
product_of_numbers = reduce(lambda x, y: x * y, numbers)
# print(f"Sum of Numbers: {sum_of_numbers}")
# print(f"Product of Numbers: {product_of_numbers}")

# default arguments in lambda function
data = lambda name = "Hamza Aamir", age = 21: f"Name: {name}, Age: {age}"
print(data())
print(data("Omer"))
print(data("Wahab", 24))
print(data(age=26, name="Ali"))
