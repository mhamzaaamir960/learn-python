
# if statement

age = 10
if age >= 18:
    print("Your age is {}. You can vote.".format(age))
else:
    print("You cann't vote because your age is {} less than 18".format(age))


name = "Hamza"
if name == "Hamza":
    print(f"Welcome {name}!")
else:
    print("Invalid Name!")

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


# if-elif-else

marks = 70

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >= 70 and marks < 80:
    print("Grade C")
elif marks >= 60 and marks < 70:
    print("Grade D")
elif marks >= 0 and marks < 60:
    print("Grade F")

print("Marks out range!")

# Nested if statements

number = 6

if number > 0:
    print("Positive Number")
    if number % 2 == 0:
        print("Even Number!")
    else:
        print("Odd Number!")


value = ""
if value:
    print("This is truthy value!")
else:
    print("This is Falsy value!")


# Ternary Operator in Python (Conditional Expression)

name = "Hamza"
correct_name = name if name != "Hamz" else "Wrong name"
print(correct_name)


username = "Hamza"
if username.lower() == "hamza":
    print("Valid username!")
    
age_1 = 15
age_2 = 21

if age_1 >= 18 or age_2 >= 18:
    print("Age is Correct for vote!")
else:
    print("Age is not correct for vote!")


banned_users = ["andrew","carolina", "david"]
user = "methew"


if user not in banned_users:
    print(f"{user.title()} you can post a response if you wish!")
