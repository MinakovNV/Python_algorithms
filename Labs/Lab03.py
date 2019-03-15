"""
 "  Minakov Nikita CSSE 1709R
 "  Lab 03 Python
"""

from collections import deque, Counter

# Task 1_a
print("Task_1a\n\n")

queue = deque(list(range(1, 14)))
print(queue)
queue.append(10)  # repeating "10" value
list1 = queue

list1.insert(7, "How are you?")

print("#Repeating \"10\" value, inserting \"How are you?\" on 7th position")

print(list1)
# Task 1_b
print("\n\nTask_1b\n\n")

print("#Element with index 6 was copied on first (0) position")
a = list1[6]
list1[0] = a
print(list1)

# Task 1_c
print("\n\nTask_1c\n\n")
list1.remove('How are you?')
list1.append(3)  # adding another new element

count = 0
len1 = len(list1)

for i in range(0, len1):
    for j in range(0, len1):
        if (list1[i] == list1[j]):
            count += 1

list1 = sorted(list1)
queue = deque(list1)

print(queue)
print("Number of repeated values:", (count - len1) // 2, "\nLength:", len1)
C = Counter(queue)
print(C)

# Task 2_a
print("\n\nTask_2a\n\n")

subj_name = ['Math', 'English', 'Python', 'C#', 'C++']
marks_list = [45, 90, 67, 100, 99]
stud_name = ['Minakov Nikita', 'Bogdanowitcz Weronika', 'Dilnaz Niyazova', 'Byckova Dariya', 'Sanshar Abilmazinov']
stud_name_que = deque(stud_name)
tup = subj_name, marks_list, stud_name_que
i = 0
print("Subject | Grade | Student")
for j in range(len(tup)+2):
    #for j in range(3):
    print(tup[i][j], "|", tup[i+1][j], "|", tup[i+2][j])

#print(tup)
#print(subj_name, stud_name, marks_que)

# Task 2_b
print("\n\nTask_2b\n\n")
#Minakov Nikita rewrites a Math exam and takes 100% mark
print("Minakov Nikita rewrites a Math exam and takes 100% mark\n\n")
marks_list[0] = 100

print("Subject | Grade | Student")
for j in range(len(tup)+2):
    #for j in range(3):
    print(tup[i][j], "|", tup[i+1][j], "|", tup[i+2][j])

# Task 2_c
print("\n\nTask_2c\n\n")
try:

    print("Select a row you want to delete: ")
    row_num = int(input())

    del subj_name[row_num-1]
    del marks_list[row_num-1]
    del stud_name[row_num-1]
    stud_name_que = deque(stud_name)
    tup = subj_name, marks_list, stud_name_que

    print("Subject | Grade | Student")
    for j in range(len(tup)+2):
        #for j in range(3):
        print(tup[i][j], "|", tup[i+1][j], "|", tup[i+2][j])
except:
    print("")
finally:
    print("Successfully deleted")


# Task 3_a
print("\n\nTask_3a\n\n")

different = ['one', 'two', 'one', '1', 1, '5', 1, '1', 123, 321, 123, 321, 90, 'Python', 'python', 'Python', 'lecture 4']

print("List of different elements:")
print(different)

C = Counter(different)
print("Result using Counter function:\n", C)

list_ele = list(C.elements())                             # dividing counter into to lists(list of elements)
new_list_ele = sorted(set(list_ele), key=list_ele.index)  # deleting repeated elements of array

list_num = list(C.values())                               # dividing counter into to lists(list of values)

tup_counter = new_list_ele, list_num                      # tuple of this 2 lists

i = 0

print("\nRepeated elements:")
for j in range(len(list_num)):
        if(list_num[j] != 1):                              # if number of repeatings is not equal to 1 => print this element
            print(tup_counter[i][j], "\"repeates:\"", tup_counter[i+1][j])

print("\nUnique elements:")
for j in range(len(list_num)):
        if(list_num[j] == 1):                              # if number of repeatings is equal to 1 => print this element
            print(tup_counter[i][j])


# Task 3_b
print("\n\nTask_3b\n\n")

fnames_set = {"Nikita", "Weronika", "Dasha", "Dilnaz", "Sanshar"}
lname_set = {"Minakov", "Bogdanowitz", "Bychkova", "Niyazova", "Abilmazinov"}

print("Two different sets:\n", fnames_set, "\n", lname_set)

FIO_set = {"Nikita"}                                       # sets delete repeated values
FIO_set.update(fnames_set)                                 # or it is possible to use union method
FIO_set.update(lname_set)
print("\n\nOne set created by adding 2 previous sets\n", FIO_set)


# Task 3_c
print("\n\nTask_3c\n\n")
# Subsets??????????????????????????????????????????????
print("First name set as a subset of FIO set:\n", FIO_set.intersection(fnames_set))
print("Last name set as a subset of FIO set:\n", FIO_set.intersection(lname_set))


# Task 3_d
print("\n\nTask_3d\n\n")

num1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
num2 = {12, 23, 4, 45, 3, 2, 7, 44, -12, 0}
print("Two sets of int numbers:\n", num1, "\n", num2)

# finding max elements

max1 = max(num1)
max2 = max(num2)
print("\nMax number in 1st set:", max1)
print("Max number in 2st set:", max2)
if max1 >= max2:
    print("Max between 2 sets:", max1)
else:
    print("Max between 2 sets:", max2)

# finding min elements

min1 = min(num1)
min2 = min(num2)
print("\nMin number in 1st set:", min1)
print("Min number in 2st set:", min2)
if min1 <= min2:
    print("Min between 2 sets:", min1)
else:
    print("Min between 2 sets:", min2)



# Task 4_a
print("\n\nTask_4a\n\n")

list_apple = ('1. the tree, cultivated in most temperate regions',
              '2. the fruit of any of certain other species of tree of the same genus')
list_words = ('glossary', 'apple', 'phone', 'table', 'teacher')
list_dif = ('a list of terms in a special subject, field, or area of usage, with accompanying definitions',
            list_apple,
            'a portable electronic telephone device, as a cell phone, mobile phone, or smartphone',
            'such a piece of furniture specifically used for serving food to those seated at it',
            'a person who teaches or instructs, especially as a profession; instructor')

glossary = dict(zip(list_words, list_dif))


num = int(input("Welcome to our Glossary!\nEnter number:\n1. Glossary\n2. Apple\n3. Phone\n4. Table\n5. Teacher\n"))
if (num == 1):
    word = 'glossary'
elif (num == 2):
    word = 'apple'
elif (num == 3):
    word = 'phone'
elif (num == 4):
    word = 'table'
elif (num == 5):
    word = 'teacher'
else:
    print("Invalid number")
#word = str(input())
#word.lower();

print(glossary.get(word))


# Task 4_b
print("\n\nTask_4b\n\n")

id_list = (101, 102, 103, 104, 105)
name_list = ('Minakov Nikita, 19.06.1999, 77777580802',
             'Dariya Bychkova, 29.10.1996, 77057768918',
             'Weronika Bogdanowitcz, 04.09.1999, 48731148987',
             'Gorinski Stephan, 04.08.1999, 77771786351',
             'Dlnaz Niyazova, 02.03.2000, 77018765009')

d_base = dict(zip(id_list, name_list))

print("Hello to our student DB")
id_input = int(input("Enter ID:\n(You can choose from 101-105)\n"))

print(d_base.get(id_input))


# Task 4_c
print("\n\nTask_4c\n\n")

currency_name = str(input("Please enter your currency:\n(Examples: dollar, euro, zloti, rubles, pounds)\n"))

currency_name_list = ('dollar', 'euro', 'zloti', 'rubles', 'pounds')
currency_rate_list = (360.5, 414.1, 98.74, 5.54, 501.8)
exch_dict = dict(zip(currency_name_list, currency_rate_list))

print(currency_name.lower(), "=", exch_dict.get(currency_name.lower()), "tenge")