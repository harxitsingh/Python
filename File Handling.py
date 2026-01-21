# ---------------------------------------------------------
# 1. Read Mode (r) – Read entire file
# ---------------------------------------------------------
with open(r"C:\Users\Harshit Singh\OneDrive\Desktop\students.txt", "r") as f1:
    content = f1.read()
    print(content)

# Output Example:
# Amit , 20 , Delhi
# Neha ,22 , Mumbai
# Rahul , 19 , Kolkata
# Priya ,21 , Chennai


# ---------------------------------------------------------
# 2. Read first line using readline()
# ---------------------------------------------------------
with open(r"C:\Users\Harshit Singh\OneDrive\Desktop\students.txt", "r") as f1:
    content = f1.readline()
    print(content)

# Output:
# Amit , 20 , Delhi


# ---------------------------------------------------------
# 3. Read all lines into a list using readlines()
# ---------------------------------------------------------
with open(r"C:\Users\Harshit Singh\OneDrive\Desktop\students.txt", "r") as f1:
    content = f1.readlines()
    print(content)

# Output:
# ['Amit , 20 , Delhi\n', 'Neha ,22 , Mumbai\n', 'Rahul , 19 , Kolkata\n', 'Priya ,21 , Chennai\n']


# ---------------------------------------------------------
# 4. Loop through the file and print each line separately
# ---------------------------------------------------------
with open(r"C:\Users\Harshit Singh\OneDrive\Desktop\students.txt", "r") as f1:
    for line in f1:
        print(line.strip())   # strip() removes \n

# Output:
# Amit , 20 , Delhi
# Neha ,22 , Mumbai
# Rahul , 19 , Kolkata
# Priya ,21 , Chennai


# ---------------------------------------------------------
# 5. Count number of students (lines) in the file
# ---------------------------------------------------------
with open(r"C:\Users\Harshit Singh\OneDrive\Desktop\students.txt", "r") as f1:
    lines = f1.readlines()
    print("Total students:", len(lines))

# Example Output:
# Total students: 4


# ---------------------------------------------------------
# 6. Write Mode (w) – Write 3 new student records
# ---------------------------------------------------------
with open("students.txt", "w") as f:
    f.write("Rahul - 19\n")
    f.write("Neha - 18\n")
    f.write("Amit - 22\n")

print("3 student records written successfully!")


# ---------------------------------------------------------
# 7. After writing, open the file again and print its content
# ---------------------------------------------------------
with open("students.txt", "r") as f:
    print(f.read())

# Output:
# Rahul - 19
# Neha - 18
# Amit - 22


# ---------------------------------------------------------
# 8. Append Mode (a) – Add one new student
# ---------------------------------------------------------
with open("students.txt", "a") as f:
    f.write("Karan - 23\n")

print("New student added!")


# ---------------------------------------------------------
# 9. Verify appended content
# ---------------------------------------------------------
with open("students.txt", "r") as f:
    print(f.read())

# Output:
# Rahul - 19
# Neha - 18
# Amit - 22
# Karan - 23
