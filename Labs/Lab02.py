"""
 "  Minakov Nikita CSSE 1709R
 "  Lab 02 Python
"""
import sys

# Task 1_a
print("Task_1a\n\n")
a = 100
b = "When will be zarplata?"
c = str(int(224.90)), (3 + 2j)
d = 123.32
e = 0b101
f = 1e4
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))

# Task 1_b
print("\n\nTask_1b\n\n")
f_name, l_name = "Nikita", "Minakov"
age, GPA = 19, 3.89
print(f_name, type(f_name))
print(l_name, type(l_name))
print(age, type(age))
print(GPA, type(GPA))

# Task 2_1
print("\n\nTask_2_1\n\n")
print('I\'m going to "Jerry\'s Bar"')

# Task 2_2
print("\n\nTask_2_2\n\n")
print("Please print any word:")

word = str(input())
Length = len(word)

if Length % 2 == 0:
    Length //= 2
    l1 = Length - 1

    print(word[l1] + word[Length])
else:
    Length //= 2
    print(word[Length])

# Task 2_3
print("\n\nTask_2_3\n\n")
print("Please print any sentence:(with white spaces)")

snt = str(input())
# left white spaces
snt = snt.lstrip()
print(snt + "(removing left white spaces)")
# right white spaces
snt = snt.rstrip()
print(snt + "(removing right white spaces)")
# all spaces
snt = snt.replace(" ", "")
print(snt + "(removing all white spaces)")

# Task 3_1
print("\n\nTask_3_1\n\n")

max = sys.maxsize

print("Max int value:", max)
print("In Python 3 int type is unbounded! As it is showed forward")
max = 100 ** 100
print(max)

# Task 3_2
print("\n\nTask_3_2\n\n")
print("Input integer number between 100 and 999")

num = int(input())

if (num >= 100 and num < 1000):
    a = num // 100
    c = num % 10
    b = num // 10 - (a * 10)
    sum = a + b + c
    print("Sum =", sum)
    if (0 != a * b * c):
        mult = a * b * c
        print("Mult =", mult)
    elif (b == c == 0):
        print("Mult =", a)
    elif (b == 0):
        mult = a * c
        print("Mult =", mult)
    elif (c == 0):
        mult = b * a
        print("Mult =", mult)
else:
    print("Invalid input")

# Task 3_3
print("\n\nTask_3_3\n\n")
a = int(input("Please choose:\n1.Celsius\n2.Fahrenheit\n"))
temp = int(input("Input temperature:\n"))

if (a == 1):
    cel = temp
    fahr = (9 / 5) * cel + 32
    print("Fahrenheit:", fahr)
elif (a == 2):
    fahr = temp
    cel = (fahr - 32) * 5 / 7
    print("Celsius:", cel)
else:
    print("Invalid input")

# Task 4_1
print("\n\nTask_4_1\n\n")
# numbers that can be divided only to 3? only to 3? only? there is no numbers that can be divided only to 3,
# even "3" can be divided to 1 and 3. As I understand i should create a list with numbers that CAN! be divided to 3.
list1 = list(range(0, 150, 3))
print("numbers that can be divided to 3:", list1, "\nLength:", len(list1))

list2 = list(range(1, 61, 2))
print("\nodd numbers:", list2, "\nLength:", len(list2))

# Task 4_2
print("\n\nTask_4_2\n\n")

list1 = ['Apple', 'Cherry', 'Melon', 'Watermelon', 'Banana', 'Pear', 'Grapes', 'Peach', 'Avocado']
list1.sort(reverse=True)
print("First way using \"sort\" method:", list1)

print("\nFirst way using \"sorted\" method:", sorted(list1, reverse=True))

# Task 4_3
print("\n\nTask_4_3\n\n")

list1 = list(range(50, 111, 2))
print("List of even numbers:", list1)
list1.reverse()
i = 9
print("Last 10 numbers:")
while (i > -1):
    print(list1[i], end=" ")
    i -= 1
list2 = list(range(-10, -101, -2))
print("\nList of negative even numbers:", list2)

# Task 4_4
print("\n\nTask_4_4\n\n")
# As we remember, there is no max int value in python 3. I will take the folowing int as a maximum.
max = sys.maxsize
m1 = list(range(0, 2))
m1.insert(1, max)
print("List with inserted \"max\" int value:\n", m1)

# Task 4_5
print("\n\nTask_4_5\n\n")
num_list = [1, 2, 3, 4, 5]
char_list = ['a', 'b', 'c', 'd']
multi_list = []

multi_list.append(num_list)
multi_list.append(char_list)

print("List of lists(int and char)", multi_list)
ch = int(input("Enter the number:\n"))
num_list.append(ch)
ch = str(input("Enter any char:\n"))
pos = int(input("Enter any index:\n"))
char_list.insert(pos, ch)

print("Adding new number and char to list", multi_list)
