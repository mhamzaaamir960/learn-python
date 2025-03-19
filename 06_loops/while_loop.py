
# print value from 1 to 5
count = 1
while count <= 5:
    print(count)
    # count++ # not works in python
    count += 1


# Infinite loop in python using while loop

while True:
    print("This is infinite loop!")
    break  # Stops the loop after print once

# Nested while loop

count1 = 0
count2 = 0
while count1 < 5:
    print("This is outer loop")
    count2 = 0
    while count2 < 5:
        print("This is inner loop", end=", ")
        count2 += 1
    print(end="\n")
    count1 += 1


while True:
    pass  # nothing return or print
