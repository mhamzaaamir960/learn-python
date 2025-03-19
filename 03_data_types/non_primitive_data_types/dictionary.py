student = {
    "name": "Hamza Aamir",
    "age": 21,
    "subject": "Computer Science",
}
print(type(student))
print(student)

removed_item = student.popitem()

# removes and return last inserted item in tuple type from dictionary
print(type(removed_item), removed_item)
print(student)


print(student["name"])
print(student.get("age"))
print(student.get("gender", "Value not Exits!"))


# Update/modify value in dictionay
student["age"] = 23
print(student["age"])

# Adding new value in dictionary
student["city"] = "Rawalpindi"
print(student["city"])
print(student.get("city"))

print(student)

# using .pop()
student.pop("age")
print(student)

# using del keyword
del student["name"]  # deletes name property in studnet dictionary
print(student.get("name"))
print(student)

# using .clear() removes all values from dictionary
# None and clear() method removes all key-value from student dictionary
print(student.clear())
print(student)  # {}


student = {
    "name": "Hamza Aamir",
    "age": 21,
    "subject": "Computer Science"
}

# iterate over keys()
for key in student:
    print(key)

print("\n")

for key in student.keys():
    print(key)

print("\n")

# iterate over values
for value in student.values():
    print(value)

print("\n")

# iterate over items
for key, value in student.items():
    print(f"Key: {key}, Value: {value}")

print("\n")

for key in student:
    print(f"Key: {key}, Value: {student[key]}")

# Merge other dictionary
# .update(other_dictionary)

data = {
    "name": "Hamza Aamir",
    "age": 21,
    "subject": "Computer Science"
}
update_data = {
    "age": 24,
    "city": "Rawalpindi"
}
print(data)
data.update(update_data)
print(update_data)
print(data)
