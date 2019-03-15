"""
 "  Minakov Nikita CSSE 1709R
 "  Lab 08 Python
"""

import sys
from datetime import *
from random import *
from collections import deque, Counter
import os
import json



# ______________
# Classes

class Person:

    def __init__(self, name):
        self.name = name

    def getInfoPerson(self):
        return self.name


class Courses_C:
    name = "C#"
    def __init__(self, mark):
        self.__mark = mark

    def getMark_C(self):
        return self.__mark

    def setMark_C(self, mark):
        self.__mark = mark


class Courses_Java:

    name = "Java"
    def __init__(self, mark):
        self.__mark = mark

    def getMark_Java(self):
        return self.__mark

    def setMark_Java(self, mark):
        self.__mark = mark

class Courses_Py:

    name = "Python"
    def __init__(self, mark):
        self.__mark = mark

    def getMark_Py(self):
        return self.__mark

    def setMark_Py(self, mark):
        self.__mark = mark


class Teacher(Person):

    def __init__(self, name, subject):
        Person.__init__(self, name)
        self.subject = subject

    def getInfoT(self):
        return self.getInfoPerson() + ": " + self.subject

    def getNameT(self):
        return self.name

    def getSubject(self):
        return self.subject


class Student(Person, Courses_C, Courses_Java, Courses_Py):

    def __init__(self, id, name, mark_c, mark_java, mark_py):
        self.id = id
        Person.__init__(self, name)
        Courses_C.__init__(self, mark_c)
        Courses_Java.__init__(self, mark_java)
        Courses_Py.__init__(self, mark_py)


    def getInfoS(self):
        return self.id + ": " + self.getInfoPerson() + "\n" + Courses_C.name + ": " + str(self.getMark_C()) + "\n" + Courses_Java.name + ": " + str(self.getMark_Java()) + "\n" + Courses_Py.name + ": " + str(self.getMark_Py()) + "\n"

    def getSpesInfoC(self):
        return self.id + ": " + self.getInfoPerson() + "\n" + Courses_C.name + ": " + str(self.getMark_C())

    def getSpesInfoJava(self):
        return self.id + ": " + self.getInfoPerson() + "\n" + Courses_Java.name + ": " + str(self.getMark_Java())

    def getSpesInfoPy(self):
        return self.id + ": " + self.getInfoPerson() + "\n" + Courses_Py.name + ": " + str(self.getMark_Py())

    def getNameS(self):
        return self.name

    def getMark(self):
        return Courses_C.name + ": " + str(self.getMark_C()) + "\n" + Courses_Java.name + ": " + str(self.getMark_Java()) + "\n" + Courses_Py.name + ": " + str(self.getMark_Py()) + "\n"

# ______________
# Working with Json functions 
# Dumping data file


def Json_create():
   
    teacher_names = ["Minakov Nikita", "Bogdanowitz Weronika", "Dasha Byshkova"]
    courses = ["c#", "java", "Python"]

    teacher_dict = dict(zip(teacher_names, courses))

    student_id = [101, 102, 103, 104, 105]
    student_names = ["Andrew Sazontov", "Anastasia Muratalieva", "Dilnaz Niyazova", "Ravil Brankov", "Jeniffer Russanova"]

    # Student ID info keeps
    student_id_dict = dict(zip(student_id, student_names))

    marks_c = [90, 20, 80, 43, 66]
    marks_java = [70, 100, 60, 78, 22]
    marks_py = [32, 33, 100, 23, 98]

    # marks info keeps
    c_dict = dict(zip(student_id, marks_c))
    java_dict = dict(zip(student_id, marks_java))
    py_dict = dict(zip(student_id, marks_py))


    with open('Teacher.json', "w") as maJsonT:
        json.dump(teacher_dict, maJsonT)

    with open('StudentInfo.json', "w") as maJsonS:
        json.dump(student_id_dict, maJsonS)

    with open('C#_marks.json', "w") as maJsonS:
        json.dump(c_dict, maJsonS)

    with open('Java_marks.json', "w") as maJsonS:
        json.dump(java_dict, maJsonS)

    with open('Py_marks.json', "w") as maJsonS:
        json.dump(py_dict, maJsonS)

# ______________
# Reading data from Json database 

def Json_Teacherinfo():

    with open('Teacher.json', "r") as maJson:
        myReadData = json.load(maJson)
        return myReadData

def Json_Studentinfo():
    with open('StudentInfo.json', "r") as maJson:
        myReadDataS = json.load(maJson)
        return myReadDataS

def Json_C_marks():
    with open('C#_marks.json', "r") as maJson:
        myReadDataC_marks = json.load(maJson)
        return myReadDataC_marks

def Json_Java_marks():
    with open('Java_marks.json', "r") as maJson:
        myReadDataJava_marks = json.load(maJson)
        return myReadDataJava_marks

def Json_Py_marks():
    with open('Py_marks.json', "r") as maJson:
        myReadDataPy_marks = json.load(maJson)
        return myReadDataPy_marks

# ______________
# Helping mini functions


def print_TeacherAndSubject():
    # func prints teachers and their subjects
    for i in range(0, 3):
        print(teacher[i].getInfoT())

def print_TeachersNames():
    for i in range(0, 3):
        print(i+1, ". ", teacher[i].getNameT(), sep="")

def print_StudentNames():
    for i in range(0, counterStudents):
        print(i+1, ". ", student[i].getNameS(), sep="")

def print_AllStdAndAllMarks():
    # func prints students and their Id
    for i in range(0, counterStudents):
        print(student[i].getInfoS())

def print_SpesCourse_AllStudMarks(iii):
    if iii == 1:
        for i in range(0, counterStudents):
            print(student[i].getSpesInfoC())
    elif iii == 2:
        for i in range(0, counterStudents):
            print(student[i].getSpesInfoJava())
    elif iii == 3:
        for i in range(0, counterStudents):
            print(student[i].getSpesInfoPy())

def print_StudentById(id):
    print(student[id-101].getInfoS())

def put_markFuck(iii):
    if iii == 1:
        for i in range(0, counterStudents):
            print(student[i].getSpesInfoC())
            temp_mark = int(input("Input new mark:\n"))
            student[i].setMark_C(temp_mark)

    elif iii == 2:
        for i in range(0, counterStudents):
            print(student[i].getSpesInfoJava())
            temp_mark = int(input("Input new mark:\n"))
            student[i].setMark_Java(temp_mark)
    elif iii == 3:
        for i in range(0, counterStudents):
            print(student[i].getSpesInfoPy())
            temp_mark = int(input("Input new mark:\n"))
            student[i].setMark_Py(temp_mark)

def addNewStudent(counterStudents, lastId):

    tempName = input("First and last name(with white space)\n")
    student_id.append(str(lastId))
    student_names.append(tempName)

    c_marks.append(100)
    java_marks.append(100)
    py_marks.append(100)
    RebuildClass()

def showMyMarks():
    print(student[iii-1].getMark())

def showNewCourses():

    for i in range(0, len(newCourses)):
        print(i+1, ": " ,newCourses[i], sep="")
    a = int(input())
    if a in temp_iiii:
        print("You have already enrolled")
    else:
        temp_iiii.append(a)
        print("Sucsesfuly enrolled")



def selActivity_func1():
    print("\nWhat you wanna do?\n"
          "1. Look for all students on your course\n"
          "2. Look for all students and all their marks\n"
          "3. Look for a student by ID\n"
          "4. Put a mark to students\n"
          "5. Add a student to your course\n"
          "6. Exit")

def selActivity_func2():
    print("\nWhat you wanna do?\n"
          "1. Look for my marks\n"
          "2. Look for my teachers\n"
          "3. Enrol new course\n"
          "4. Status\n"
          "5. Exit")

def RebuildClass():
    for i in range(0, counterStudents):
        student[i] = Student(student_id[i], student_names[i], c_marks[i], java_marks[i], py_marks[i])

try:

    # ______________
    # Json create
    Json_create()

    # ______________
    # Json read
    myReadDataTeacher = Json_Teacherinfo()
    myReadDataStudent = Json_Studentinfo()

    myReadDataC_marks = Json_C_marks()
    myReadDataJava_marks = Json_Java_marks()
    myReadDataPy_marks = Json_Py_marks()

    # ______________
    # Teacher's data prosessing & class filling
    teacher_names = list(myReadDataTeacher.keys())
    courses = list(myReadDataTeacher.values())

    teacher = [x for x in range(3)]
    for i in range(0, 3):
        teacher[i] = Teacher(teacher_names[i], courses[i])

    # ______________
    # Student's data prosessing & class filling
    student_id = list(myReadDataStudent.keys())
    student_names = list(myReadDataStudent.values())

    c_marks = list(myReadDataC_marks.values())
    java_marks = list(myReadDataJava_marks.values())
    py_marks = list(myReadDataPy_marks.values())

    student = [x for x in range(10)]
    for i in range(0, 5):
        student[i] = Student(student_id[i], student_names[i], c_marks[i], java_marks[i], py_marks[i])

    # ______________
    # Main body of program
    newCourses = ["Web", "Android", "IOS", "Big Data"]
    temp_iiii = []
    lastId = 105
    counterStudents = 5
    flag = True

    print("Hello to our little University!\n You are:\n "
      "1. Teacher\n "
      "2. Student")

    ii = int(input())                               # ii - Student or Teacher
    if ii == 1:
        print("Who are you?\n")
        print_TeachersNames()
        iii = int(input())                          # iii - Select a teacher you are
        if iii == 1 or iii == 2 or iii == 3:
            print("Hello!", teacher[iii-1].name, "\n")
            while flag:
                selActivity_func1()
                iiii = int(input())                     # iiii - Select an activity

                if iiii == 1:
                    print("\nList of students on your course\n")
                    print_SpesCourse_AllStudMarks(iii)
                    # Done

                elif iiii == 2:
                    print("\nList of all students\n")
                    print_AllStdAndAllMarks()
                    # Done

                elif iiii == 3:
                    input_id = int(input("Input an ID of student:(101-105)"))
                    print_StudentById(input_id)
                    # Done

                elif iiii == 4:
                    put_markFuck(iii)
                    # Done

                elif iiii == 5:
                    print("Adding a new student:")
                    lastId += 1
                    counterStudents += 1
                    addNewStudent(counterStudents, lastId)
                    # Done

                elif iiii == 6:
                    flag = False
                    # Done

                else:
                    flag = False
                    print("Invalid input")

        else:
            print("Invalid input")

    elif ii == 2:

        # Student activity
        print("Who are you?\n")
        print_StudentNames()
        iii = int(input())
        if iii == iii == 1 or iii == 2 or iii == 3 or iii == 4 or iii == 5 or iii == counterStudents:
            print("Hello!", student[iii - 1].name, "\n")
            while flag:
                selActivity_func2()
                iiii = int(input())                     # iiii - Select an activity

                if iiii == 1:
                    print("\nYour marks:\n")
                    showMyMarks()
                    # Done

                elif iiii == 2:
                    print("\nList of your teachers:\n")
                    print_TeacherAndSubject()
                    # Done

                elif iiii == 3:
                    print("\nSelect a course you want to learn:\n")
                    showNewCourses()
                    # Done

                elif iiii == 4:
                    print("\nYour status:\n")
                    showMyMarks()
                    # Done

                elif iiii == 5:
                    flag = False
                    # Done

                else:
                    flag = False
                    print("Invalid input")
        else:
            print("Invalid input")
    else:
        print("Invalid input")

except:
    print("Error")