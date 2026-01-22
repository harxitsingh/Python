# ---[ Q1: Read entire file ]-----------------------------------------
with open("products.txt", "r") as f:
    data = f.read()
    print(data)

# OUTPUT (example):
# P201, Headphones, 2000, Electronics
# P202, Sofa, 28000, Furniture
# P203, Printer, 12000, Electronics


# ---[ Q2: Read only first line ]--------------------------------------
with open("products.txt", "r") as f:
    print(f.readline())

# OUTPUT:
# P201, Headphones, 2000, Electronics


# ---[ Q3: Read all lines into a list ]--------------------------------
with open("products.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# OUTPUT:
# ['P201, Headphones, 2000, Electronics\n',
#  'P202, Sofa, 28000, Furniture\n',
#  'P203, Printer, 12000, Electronics\n']


# ---[ Q4: Print file line by line ]-----------------------------------
with open("products.txt", "r") as f:
    for line in f:
        print(line.strip())

# OUTPUT:
# P201, Headphones, 2000, Electronics
# P202, Sofa, 28000, Furniture
# P203, Printer, 12000, Electronics


# ---[ Q5: Count total number of products ]-----------------------------
with open("products.txt", "r") as f:
    count = len(f.readlines())
    print("Total products:", count)

# OUTPUT:
# Total products: 3


# ---[ Q6: Display only product names ]--------------------------------
with open("products.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        print(parts[1].strip())

# OUTPUT:
# Headphones
# Sofa
# Printer


# ---[ Q7: Products whose price > 10,000 ]------------------------------
with open("products.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        if int(parts[2]) > 10000:
            print(line.strip())

# OUTPUT:
# P202, Sofa, 28000, Furniture
# P203, Printer, 12000, Electronics


# ===========================================================
# PART B — WRITE MODE (w)
# ===========================================================

# ---[ Q8: Write 3 new product records ]-------------------------------
with open("products.txt", "w") as f:
    f.write("P201, Headphones, 2000, Electronics\n")
    f.write("P202, Sofa, 28000, Furniture\n")
    f.write("P203, Printer, 12000, Electronics\n")

print("Data written.")

# OUTPUT:
# Data written.


# ---[ Q9: Reopen and print file ]-------------------------------------
with open("products.txt", "r") as f:
    print(f.read())

# OUTPUT:
# P201, Headphones, 2000, Electronics
# P202, Sofa, 28000, Furniture
# P203, Printer, 12000, Electronics


# ===========================================================
# PART C — APPEND MODE (a)
# ===========================================================

# ---[ Q10: Append product ]-------------------------------------------
with open("products.txt", "a") as f:
    f.write("P204, Fan, 3500, Electronics\n")

print("Product added.")

# OUTPUT:
# Product added.


# ---[ Q11: Verify appended product ]----------------------------------
with open("products.txt", "r") as f:
    print(f.read())

# OUTPUT:
# P201, Headphones, 2000, Electronics
# P202, Sofa, 28000, Furniture
# P203, Printer, 12000, Electronics
# P204, Fan, 3500, Electronics


# ===========================================================
# PART D — READ & WRITE MODE (r+)
# ===========================================================

# ---[ Q12: Update product name Mouse → Wireless Mouse ]---------------
with open("products.txt", "r+") as f:
    data = f.readlines()
    f.seek(0)
    for line in data:
        line = line.replace("Mouse", "Wireless Mouse")
        f.write(line)
    f.truncate()

# OUTPUT:
# (If Mouse existed, it becomes Wireless Mouse)


# ---[ Q13: Move cursor to end and add new product ]-------------------
with open("products.txt", "r+") as f:
    f.seek(0, 2)
    f.write("P205, Bed, 45000, Furniture\n")

# OUTPUT:
# New product P205 added.


# ===========================================================
# PART E — LOGICAL THINKING
# ===========================================================

# ---[ Q14: Count Electronics category products ]----------------------
count = 0
with open("products.txt", "r") as f:
    for line in f:
        if "Electronics" in line:
            count += 1
print("Electronics products:", count)

# OUTPUT:
# Electronics products: 3   (example)


# ---[ Q15: Create new file with products > 20,000 ]-------------------
with open("products.txt", "r") as f, open("expensive_products.txt", "w") as out:
    for line in f:
        price = int(line.strip().split(",")[2])
        if price > 20000:
            out.write(line)

print("expensive_products.txt created.")

# OUTPUT:
# expensive_products.txt created.
