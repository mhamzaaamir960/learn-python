
str("Hamza")
repr("Hamza")

x = 100 # Positive Integer
y = -200 # Negative Integer
z= 0
print(x,y,z)


a = 100000
a = 300_000_000 # for better readability we use undersores
print(a)


#check the type of the variable
print(type(x))
# vefiry the type of the variable
isinstance(x, int)


# Integer Types: Binary, Octal, Hexadecimal
# 0b for binary
# 0o for octal
# ox for hexadeximal

# binary representation
x = 0b1011 
print(x)

# octal representation
y = 0o765
print(y)

# hexadecimal representation
z = 0xf29a
print(z)


# Converting integer to binary, octal and hexadecimal
# bin()
# oct()
# hex()

x = 100

print(bin(x))
print(oct(x))
print(hex(x))

big_num = 8**200
print(type(big_num))
print(big_num)

### Boolean Behavior of Integers
# `0` → False
# Any nonzero integer (Positive or Negative) → True

b = -100
if b:
    print("True")
else:
    print("False")
    
print(f"True + int:  {True + 5}")
print(f"True + float:  {True + 4.6}")
print(f"True + complex:  {True + (9+3j)}")

    
# Converting Other Types to Integer
# using `int()`

print(int(True))
print(int(False)) #convert bool to int
print(int(44.56)) # convert float (trunc) to int
print(int("100")) # convert string to int
print(int("0b1101", 2)) # convert string to int with base 2

# Built-in Functions for Integer (int)
# abs(x) → absolute value (it return non negative number)
# pow(base, exponent, modulus) 
# divmod(a,b) → return a tuple(quotient, remainder)
# round(number, ndigits)
# max(), min() → find max & min numbers in list of numbers
# sum(iterable, start=0)

print(abs(-200)) # 200
print(abs(200)) # 200
print(abs(-3.14)) # 3.14

print(pow(2,3)) # 2^3 = 8
print(pow(3,3,2)) # 3^3 % 2 =1

print(divmod(10,3)) # (3,1) 10//3 = 3, 10%3 = 1
print(divmod(20,3)) # (6,2) 20//3 = 6, 20%3 = 2

print(round(3.6)) 
print(round(5.5))
print(round(2.4))
print(round(2.045, 2))

l1 = [4,5,7,2,3]

print(max(l1))
print(min(l1))

print(sum(l1))

# for complex numbers abs return the magnitude 
# magnitude = sqrt(real^2 + imag^2)
z = 3 + 4j
print(int(abs(z)))

# Math Module Functions for Integers
# .factorial()
# .gcd()
# .isqrt()
# .floor()
# .ciel()
# .lcm()
# .log()
# .copysign()

# and many more...

import math
print(math.factorial(5))
print(math.isqrt(25))
print(math.gcd(12,15))
print(math.lcm(15,18))
print(math.floor(4.9))
print(math.ceil(4.1))
print(math.copysign(3,-2)) # it return the first argument with the sign of the second argument
print(math.fabs(-3.14))
print(math.log(10,10))

### Random Moudle (Generating random numbers)
# .random()
# .randint(x,y)  Random integer from x to y (inclusive)
# .uniform(x,y)  Random float between x and y
# .choice([list])
# .sample(list, pick no of uniqe elements form list) 
# .choices(list, k=3) pick 3 elements with replacement
# .shuffle(list)  shuffle the list
# and many more...

import random

numbers = [2,3,5,7,1,9]
# t = ("Hamza", "Omer", "Ali")

print(random.random())
print(random.randint(1,10))
print(random.uniform(1,10))
print(random.choice(numbers))

random.shuffle(numbers) # shuffle the numbers list
print(numbers) # shuffled numbers

print(random.choices(numbers, k=2)) # return list of 2 choices
