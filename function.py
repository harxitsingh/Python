# Function 1: Simple greet function
def greet():
    print("Hello, WELCOME to Python")

greet()


# ----------------------------------------
# Function 2: Takes name as input and prints greeting

def greet_user(name):
    print("Hello, World", name)

greet_user(input("Enter your name: "))


# ----------------------------------------
# Function 3: Take two numbers and print their sum

def sum_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    total = a + b
    print("Sum:", total)

sum_numbers()


# ----------------------------------------
# Function 4: Count vowels in a string

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    print("Total vowels:", count)

count_vowels(input("Enter a string: "))


# ----------------------------------------
# EXTRA Function 5: Check EVEN or ODD

def even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

even_odd(int(input("Enter a number: ")))


# ----------------------------------------
# EXTRA Function 6: Find factorial

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial:", fact)

factorial(int(input("Enter a number for factorial: ")))


# ----------------------------------------
# EXTRA Function 7: Largest of three numbers
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        print(a, "is the largest")
    elif b >= a and b >= c:
        print(b, "is the largest")
    else:
        print(c, "is the largest")

largest_of_three(
    int(input("Enter number 1: ")),
    int(input("Enter number 2: ")),
    int(input("Enter number 3: "))
)
