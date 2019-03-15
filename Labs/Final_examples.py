import sys
from datetime import *
from random import *
from collections import deque, Counter
import os
import json
import sqlite3
 
# json
teacher_dict = {}

with open('Teacher.json', "w") as maJsonT:
   json.dump(teacher_dict, maJsonT)
		
with open('Teacher.json', "r") as maJson:
    myReadData = json.load(maJson)

# Classes
class Person:

    def __init__(self, name):
        self.name = name

    def getInfoPerson(self):
        return self.name

class Teacher(Person):

    def __init__(self, name, subject):
        Person.__init__(self, name)
        self.subject = subject

    def getInfoT(self):
        return self.getInfoPerson() + ": " + self.subject
# Datetime
date_time = datetime.now()

# Database

con = sqlite3.connect("Endterm.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Client(fname text,  balance integer)")
cur.execute("INSERT INTO Manager VALUES\
            ('Minakova', 'Weronika', 'DartVaider')")
s = cur.execute("SELECT acc_name, validity, owner, manager FROM Account")
con.commit()
con.close()

# Random
def Random_my():
    for i in range(0, elememts_num):
        a[i] = randint(-10, 10)
"""

from datetime import *
import sqlite3
class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

class Student(Person):

    def __init__(self, name, age, grade):
        Person.__init__(self, name, age)
        self.__garde = grade

St1 = Student('Nikita', 19, 11)

print(St1.getName())

#con = sqlite3.connect("SSS.db")
#cur = con.cursor()

#cur.execute = ("CREATE TABLE IF NOT EXIST Student(Name text, age, integer, grade integer)")

#con.commit()
#con.close()
"""
def D_poss():
    x1 = (-1*b+D**(1/2))/2*a
    x2 = (-1 * b - D ** (1 / 2)) / 2 * a
    print(x1, x2)

a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

D = b**2 - 4*a*c
try:
    if D>0:
        D_poss()
    elif D == 0:
        D_zero()
    else:
        D_neg()
except:
    print("Error")
"""
date = datetime.now()
import json
print(date)

with open("Exp.json", "w") as myJson:
    json.dump(str(date), myJson)

with open("Exp.json", "a+")as myJson:
    json.dump(str(date), myJson)

from random import *

list = []

for i in range(0,10):
    list.append(randint(0, 20))

print(list)
print(max(list))
print(min(list))
list = sorted(list)
print(list)

for i in range(0, len(list)):
    list[i] = list[i]**2
print(list)

list_key = ["001", "002", "003"]
list_val = ["Minakov", "Bychkova", "Bogdanowitcz"]

dict1 = dict(zip(list_key, list_val))

print(dict1)

print(max(dict1.keys()))
print(max(dict1.values()))


def F(i):
    if i <= 1:
        return 1
    else:
        return F(i-1)+F(i-2)


num = int(input())

for i in range(0, num):
    print(F(i))
