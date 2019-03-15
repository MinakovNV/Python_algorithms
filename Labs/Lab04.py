"""
 "  Minakov Nikita CSSE 1709R
 "  Lab 04 Python
"""
from random import *


# Task 1
print("Task_1\n\n")
i = 0
a = 1
arr_numb = []


while a == 1:
    z = int(input("Please enter a number:"))
    arr_numb.append(z)
    i = i+1
    print("Do ypu want to enter new number?\n 1. Yes\n 2. No")
    a = int(input())

print(arr_numb)
qua_even, qua_odd = 0, 0
j = 0
sum, mult = 0, 1
for j in range(len(arr_numb)):
    sum = arr_numb[j] + sum
    mult = arr_numb[j] * mult
    if (arr_numb[j]%2 == 0):
        qua_even = qua_even +1
    if (arr_numb[j]%2 != 0):
        qua_odd = qua_odd +1
    j = j+1
max = max(arr_numb)
print("Sum of all numbers:", sum, "\nMult of all numbers:", mult, "\nQuantity of even numbers:", qua_even, "\nQuantity of odd numbers:", qua_odd, "\nMax value:", max)

"""

# Первый вариант программы, выводит число только по индексу
# Task 2
print("\n\nTask_2\n\n")
try:
    def F(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return F(num-1)+F(num-2)

    print("Please enter index of number in Fibonacci sequence:")

    num = int(input())

    result = F(num)
    print("Fibonacci(", num, ")=", result)

except:
    print("fdsfsdfsdf")
    
"""


# Task 2
print("\n\nTask_2\n\n")
try:
    def F(num):
        if num <= 1:
            return num
        else:
            return F(num-1) + F(num-2)

    print("Please enter index of number in Fibonacci sequence:")

    num = int(input())

    for i in range(num):
        print(F(i))

except:
    print("Invalid Input")



# Task 3
print("\n\nTask_3\n\n")

i = 0
arr = []
for i in range(20, 50):
    if i % 3 == 0 and i %5 != 0:
        arr.append(i)
print(arr)


# Task 4
print("\n\nTask_4\n\n")

str = str(input("Input any word:"))
arr = []
i = 0
for i in range(len(str)):
    arr.append(str[i])
arr.reverse()
for i in range(len(str)):
    print(arr[i], sep="", end="")



# Task 5
print("\n\nTask_5\n\n")

counter = 0

def Hint1():
    print("Do you want a first hint?(yes/no)")
    answ = str(input())
    answ = answ.lower()
    if (answ == "no"):
        return 0
    elif (answ == "yes"):
        if (secret // 10 == 0):
            print("Number has only 1 digit")
            return 5
        elif (secret // 100 == 0):
            hint1 = secret // 10
            print("1 digit is equal to", hint1)
            return 5
        else:
            hint1 = secret//100
        print("1 digit is equal to", hint1)
        return 5
    else:
        print("Invalid input")
        return Hint1()

def Hint2():
    print("Do you want a second hint?(yes/no)")
    answ = str(input())
    answ = answ.lower()
    if (answ == "no"):
        return 5
    elif (answ == "yes"):
        if (secret // 10 == 0):
            print("Number has only 1 digit!!!! Think!!!")
            return 10
        elif (secret // 100 == 0):
            print("It is too easy to guese this number:) Think for a little!")
            return 10
        else:
            hint2 = secret // 10
        print("First 2 digits are equal to", hint2)
        return 10
    else:
        print("Invalid input")
        return Hint2()

secret = randint(0, 1001)

attempt = 0
i = 0
score = 0

while i == 0:
    try:
        attempt = int(input("Try to guese:[0, 1000]\n"))
        counter += 1
        score += 1
        if (attempt == secret):
            i = 1
            print("Congrats, You  are winner\n", "You score is", score)
        else:
            if (attempt < secret):
                print(">")
            elif (attempt > secret):
                print("<")
        if (counter==5):
            counter = Hint1()
        if (counter == 10):
            counter = Hint2()
        if (counter == 15):
            print("Are you seriously so stupid???\n",
                  "Game over! You lose!\n"
                  "You score is", score,
                  "\nYou number was:", secret)
            break
    except:
        print("Please enter any words")


"""
# Программа читтер(не доделана)
# Task 5
print("\n\nTask_5\n\n")

counter = 0

def Hint1():
    print("Do you want a first hint?(yes/no)")
    answ = str(input())
    answ = answ.lower()
    if (answ == "no"):
        return 0
    elif (answ == "yes"):
        if (secret // 10 == 0):
            print("Number has only 1 digit")
            return 5
        elif (secret // 100 == 0):
            hint1 = secret // 10
            print("1 digit is equal to", hint1)
            return 5
        else:
            hint1 = secret//100
        print("1 digit is equal to", hint1)
        return 5
    else:
        print("Invalid input")
        return Hint1()

def Hint2():
    print("Do you want a second hint?(yes/no)")
    answ = str(input())
    answ = answ.lower()
    if (answ == "no"):
        return 5
    elif (answ == "yes"):
        if (secret // 10 == 0):
            print("Number has only 1 digit!!!! Think!!!")
            return 10
        elif (secret // 100 == 0):
            print("It is too easy to guese this number:) Think for a little!")
            return 10
        else:
            hint2 = secret // 10
        print("First 2 digits are equal to", hint2)
        return 10
    else:
        print("Invalid input")
        return Hint2()

secret = randint(0, 1001)

#print(secret)
attempt = 0
i = 0
score = 0
a = secret
while i == 0:
    try:
        attempt = int(input("Try to guese:[0, 1000]\n"))
        counter += 1
        score += 1
        if (attempt == secret):
            i = 1
            print("Congrats, You  are winner\n", "You score is", score, "\nYou number was:", secret, a)
        else:


            if (attempt < secret):
                secret += + 3
                print(">")
            else:
                secret += - 3
                print("<")
        if (counter==5):
            counter = Hint1()
        if (counter == 10):
            counter = Hint2()
        if (counter == 15):
            print("Are you seriously so stupid???\n",
                  "Game over! You lose!\n"
                  "You score is", score,
                  "\nYou number was:", secret, a)
            break
        secret = a
    except:
        print("Please enter any words")

"""


# Task 6
print("\n\nTask_6\n\n")

def F_even(n):
    print("Shelpek", n, "Side 1;", "Shelpek", n+1, "Side 1")
    print("Shelpek", n, "Side 2;", "Shelpek", n + 1, "Side 2")

def F_odd(n):
    print("Shelpek", n, "Side 1;", "Shelpek", n + 1, "Side 1")
    print("Shelpek", n, "Side 2;", "Shelpek", n + 2, "Side 1")
    print("Shelpek", n+1, "Side 2;", "Shelpek", n + 2, "Side 2")


try:
    print("Input the number shelpeks:")
    num = int(input())
    min = num*10
    hour = 0
    min1 = 10

    if (num % 2 == 0):
        for n in range(1, num, 2):
            F_even(n)

    if (num % 2 != 0):
        for n in range(1, num, 3):
            F_odd(n)

    if (min >= 60):
        hour = min // 60
        min = min-60*hour

    print("\nNumber of shelpeks:", num)
    print("\nHours:", hour, "\nMinutes:", min)

except:
    print("Invalid number")


