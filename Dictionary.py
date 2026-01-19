# Question 1: Create a dictionary of 5 countries and capita-
countries = {
    "India": "New Delhi",
    "USA": "Washington D.C.",
    "Japan": "Tokyo",
    "France": "Paris",
    "Australia": "Canberra"
}

print(countries)
# Output:
# {'India': 'New Delhi', 'USA': 'Washington D.C.', 'Japan': 'Tokyo', 'France': 'Paris', 'Australia': 'Canberra'}


# ---------------------------------------------
# Question 2: Access the capital of "India"

print(countries["India"])
# Output:
# New Delhi


# ---------------------------------------------
# Question 3: Add a new key-value pair Japan:Tokyo

countries["Japan"] = "Tokyo"


# ---------------------------------------------
# Question 4: Update capital of USA to "New York"

countries["USA"] = "New York"


# ---------------------------------------------
# Question 5: Delete the key "France"

del countries["France"]


# ---------------------------------------------
# Question 6: Create a dictionary of students and marks
# Print all student names using keys()
students = {
    "aman": 45,
    "harshit": 76,
    "rudra": 45,
    "div": 67
}

print(students.keys())

# Output:
# dict_keys(['aman', 'harshit', 'rudra', 'div'])


# ---------------------------------------------
# Question 7: Print all marks using values()

print(students.values())

# Output:
# dict_values([45, 76, 45, 67])


# ---------------------------------------------
# Question 8: Print all key-value pairs using items()

print(students.items())

# Output:
# dict_items([('aman', 45), ('harshit', 76), ('rudra', 45), ('div', 67)])


# ---------------------------------------------
# Question 9: Use get() to access value of "Rahul"
# If not found, return "Not Found"

print(students.get("Rahul", "Not Found"))
# Output:
# Not Found
