
# Lab 01 Minakov Nikita Csse1709R
# Task 1_A

print("Minakov")
print("Nikita")
# Task 1_B
print("This", "year", "is", "mine", sep="+", end="...")
print("I promise")
# Task 2_A

a = 100;
b = 200;
c = a + b

print(c)  # Sum using third variable

print("%i * %i= " % (a, b), a*b)  # Multiplication in print() function

print(a**(1/2))  # squre root
c = b**(1/2)  # squre root using new variable
print(c)

print(a**3)  # a and b in power of 3
c = b**3
print(c)

# Task 2_B
print("Write your First and Last Names")
a2 = input()
b2 = input()
print("Your First Name {} and Last Name {}" .format(a2, b2))  # output user's First and Last Names using format

# Task 3
# Этот код был написан до того как вы сказали как именно должна решаться эта задача(Не хватает только правильной формулы расчета GPA)
sub = [100, 100, 100, 100, 100, 100, 100, 100]
cred = [2, 2, 2, 2, 3, 3, 3, 3]

sum1 = 0
sum2 = 0

for i in range(8):  # inputing marks and subjects
     print("Your", i+1, "subject's mark")
     sub[i] = int(input())
     print("Your", i+1, "subject's credit")
     cred[i] = int(input())


for i in range(8):
    if(sub[i] > 49) and (sub[i] < 101):
        sum1 = (sum1+sub[i])
        sum2 = sum2 + cred[i]
gpa = (sum1 + sum2)/ sum2/10
if (gpa > 2.24 and gpa < 4.01):
    print(gpa)

# Task 3(правильный)
mark = int(input())
if (mark>=95 and mark<=100):
    print("Your GPA = 4! Welcome to the 3rd course")
elif(mark>=90 and mark<=94):
    print("Your GPA = 3.67! Welcome to the 3rd course")
elif(mark>=85 and mark<=89):
    print("Your GPA = 3.33! Welcome to the 3rd course")
elif(mark>=80 and mark<=84):
    print("Your GPA = 3! Welcome to the 3rd course")
elif(mark>=75 and mark<=79):
    print("Your GPA = 2.66! Welcome to the 3rd course")
elif (mark >= 70 and mark <= 74):
    print("Your GPA = 2.33! Welcome to the 3rd course")
elif(mark>=65 and mark<=69):
    print("Your GPA = 2! Sorry, you are going to study on the 2nd course again")
elif(mark>=60 and mark<=64):
    print("Your GPA = 1.67! Sorry, you are going to study on the 2nd course again")
elif(mark>=55 and mark<=59):
    print("Your GPA = 1.32! Sorry, you are going to study on the 2nd course again")
elif(mark>=50 and mark<=54):
    print("Your GPA = 1! Sorry, you are going to study on the 2nd course again")

# Task 4

num = int(input())
if(num > 100 and num < 1000):
    a = num//100
    c = num % 10
    b = num //10 - (a*10)
if (a == b == c):
    print(a, b, c, sep="")
elif (a==b):
    print(b, c, a, sep="")
    print(c, b, a, sep="")
elif (b==c):
    print(b, a, c, sep="")
    print(b, c, a, sep="")
elif (a==c):
    print(a, c, b, sep="")
    print(b, a, c, sep="")
else:
    print(a, b, c, sep="")
    print(a, c, b, sep="")
    print(b, a, c, sep="")
    print(b, c, a, sep="")
    print(c, a, b, sep="")
    print(c, b, a, sep="")



# Task 5
import math
print("Chose one of 3 figures:\n1. Triangle\n2. Circle\n3. Tetragon")
a = int(input())
if(a == 1):
    print("Write 3 sides of triangle:")
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c)/2
    area = (p*(p-a)*(p-b)*(p-c))**(1/2)
elif(a == 2):
    print("Write radius of circle")
    r = int(input())
    area = math.pi*r**2
elif(a == 3):
    print("Write 4 sides of tetragon:")
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    p = (a + b + c + d) / 2
    area = ((p-a)*(p-b)*(p-c)*(p-d))
print(area)