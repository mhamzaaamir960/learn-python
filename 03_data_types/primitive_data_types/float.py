from decimal import Decimal
x = 3.14  # Positive float
y = -2.6  # Negative float
z = 25e2  # 25 * 10^2 = 2500.0
print(x, y, z)


# Converting float variables

a = 5.6
b = float(10)
c = float("3.14")
print(type(a))
print(type(b))
print(type(c))
print(a, b, c)


# Precision and Rounding Errors
x = 0.1
y = 0.2
z = 0.3
print(x+y-z)

# To avoid precision errors, use Python's decimal module:

a = Decimal('0.1')
b = Decimal('0.2')
c = Decimal('0.5')
print(a+b-c)


# Special Float Values
# inf (positive infinity)
# -inf (Negative infinity)
# nan (Not a nummber (NaN))

print(float('inf'))
print(float('-inf') > 100)
print(float('nan'))


# use of inf

numbers = [8.5, 7.6, 6.5, 9.2]
min_value = float('inf')
for num in numbers:
    if num < min_value:
        min_value = num

print(min_value)


# When to Avoid Using nan?
# 1. Do not use `nan` for normal missing values in databases. Instead, use `None` (Python’s null equivalent).
# 2. Avoid comparisons with nan since it never equals anything, even itself. Always use `math.isnan()`.


# use of nan
import math

data = [4.5, 3.2, float('nan'), 1.4, 9.6]
filtered_data = [x for x in data if not math.isnan(x)]
print(filtered_data)

print(float("nan") == float("nan")) # False
print(float('nan') != float('nan')) # True
print(float('nan') is float("nan")) # False

print(id(float("nan")))
print(id(float("nan")))

import math

x = float("nan")
y = float("nan")

print(math.isnan(x)) # True
print(math.isnan(y)) # True
print(x == y) # False


### Type Checking
x = 3.14
print(isinstance(x , float))
print(isinstance(x , int))
