# Q1
#  write program to print numbers from 1 to 10 using for loop 
for i in range (1 , 101):
 print(i)

 #Q2
 #sum of first 10 natural numbers using a while loop 
i=1
total= 0
while i <= 10:
    total += i
    i+= 1
print('sum = ',total)

#Q3
# take a number as input and print its multiplication table upto 10
num = int(input("Enter a number :"))
i=1
while i <= 10:
    print(num,"x",i,"=",num*i)
    i+= 1

#q4
# find the factorial of a number using while loop    
num = int(input("Enter a number: "))
fact = 1
i = 1

# while i <= num:
fact *= i
i += 1

print("Factorial =", fact)

#q5
#take an integer as input and reverse its digits
num = int(input("Enter a number: "))
rev = 0

# while num > 0:
digit = num % 10
rev = rev * 10 + digit
num //= 10
print("Reversed number =", rev)

#q6
#print all even numbers b/w 1 and 50
for i in range (2,51 ,2):
    print(i)

#Q7
#Take a number as input and find the sum of its digits.
num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10      # last digit
    total += digit        # add digit
    num //= 10            # remove last digit

print("Sum of digits =", total)

#Q8
#print the first 10 terms of the fibonacci sequence using for loop
a = 0
b = 1

for i in range(10):
    print(a)
    c = a + b
    a = b
    b = c
