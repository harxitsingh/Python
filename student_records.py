# Q1: Create list of 3 dictionaries
students = [
    {"name": "Rahul", "age": 19},
    {"name": "Neha", "age": 18},
    {"name": "Amit", "age": 22}
]
print(students)


# Q2: Print name of first student
print(students[0]["name"])


# Q3: Loop and print all student names
for s in students:
    print(s["name"])


# Q4: Add new dictionary Priya:21
students.append({"name": "Priya", "age": 21})
print(students)


# Q5: Update Rahul's age to 20
for s in students:
    if s["name"] == "Rahul":
        s["age"] = 20
print(students)


# Q6: Remove Neha from list
for s in students:
    if s["name"] == "Neha":
        students.remove(s)
        break
print(students)


# Q7: Find oldest student
oldest = students[0]
for s in students:
    if s["age"] > oldest["age"]:
        oldest = s
print(oldest)


# Q8: Print all students age > 20
for s in students:
    if s["age"] > 20:
        print(s)


# Q9: Convert list of dicts to list of names
names = []
for s in students:
    names.append(s["name"])
print(names)


# Q10: Sort list by age 
for i in range(len(students)):
    for j in range(i+1, len(students)):
        if students[i]["age"] > students[j]["age"]:
            students[i], students[j] = students[j], students[i]

print(students)
