
from random import *

# Task 1

i = 0
counter1 = 1
arr = []

while counter1 == 1:
    z = int(input("Please enter a number:"))
    arr.append(z)
    i = i + 1
    print("Do ypu want to enter new number?(1. Yes 2. No)")
    counter1 = int(input())
even, odd = 0, 0
j = 0
s, m = 0, 1
for j in range(len(arr)):

    s = arr[j] + s

    m = arr[j] * m
    if (arr[j] % 2 == 0):
        even = even + 1
    if (arr[j] % 2 != 0):
        odd = odd + 1
    j = j + 1
max = max(arr)
print("Sum:", s, "\nMult:", m, "\nEven numbers:", even,
      "\nOdd numbers:", odd, "\nMax:", max)


# Task 2

def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)

print("Please enter number")

n = int(input())

for i in range(n):
    print(F(i))


# Task 3

i = 0
a = []
for i in range(20, 50):
    if i % 3 == 0 and i % 5 != 0:
        a.append(i)
print("Elements of sequence", a)

# Task 4


s = input("Any word:")
a = []

for i in range(0, len(s)):
    a.append(s[i])
a.reverse()
for i in range(0, len(s)):
    print(a[i])

# Task 5

s = randint(0, 1001)

a = 0
j = 0
score = 0

while j == 0:

    a = int(input("Try to guese a number:\n"))
    if (a == s):
        i = 1
        print("You  are winner\n")
        break
    else:
        if (a < s):
            print(">")
        elif (a > s):
            print("<")


# Task 6

print("Input the number shelpeks:")
n = int(input())
min = n * 10
hour = 0

if (min >= 60):
    hour = min // 60
    min = min - 60 * hour

print("\nNumber of shelpeks:", n)
print("\nHours:", hour, "\nMinutes:", min)


