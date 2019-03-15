"""
 "  Minakov Nikita CSSE 1709R
 "  Lab 08 Python
"""

class Person:

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def getInfoPerson(self):
        return self.f_name + " " + self.l_name


class Teacher(Person):

    def __init__(self, f_name, l_name, subject):
        Person.__init__(self, f_name, l_name)
        self.subject = subject

    def getInfoT(self):
        print(self.getInfoPerson(), self.subject)

    def getNameT(self):
        return self.f_name + " " + self.l_name

class Student(Person):

    def __init__(self, f_name, l_name, subject_list):
        Person.__init__(self, f_name, l_name)
        self.subject_list = subject_list

    def printSubj(self):
        return subject_list

    def getInfoS_Names(self):
        print(self.getInfoPerson())

    def getInfoS(self):
        print(self.getInfoPerson(), self.subject_list)

    def getNameS(self):
        return self.f_name + " " + self.l_name

def printTeacher():
    j = 1
    print("\nStaff:")
    for i in range(0, 3):
        print(j, ". ", sep="", end="")
        teacher_list[i].getInfoT()
        j += 1


def printStudent(i):
    student_list[i].getInfoS_Names()
    i += 1

subject_list = ["c#", "Java", "Python"]
f_name_list = ["Nikta", "Dasha", "Andrew", "Weronika", "Vlad", "Ravil"]
l_name_list = ["Minakov", "Bychkova", "Sazontov", "Bogdanowitcz", "Golm", "Brankov"]

course_name = subject_list
course_mark = []

result_list = [course_name, course_mark]

teacher_list = [i for i in range(0, 3)]
student_list = [i for i in range(0, 3)]

teacher_list[0] = Teacher(f_name_list[0], l_name_list[0], subject_list[0])
teacher_list[1] = Teacher(f_name_list[1], l_name_list[1], subject_list[1])
teacher_list[2] = Teacher(f_name_list[2], l_name_list[2], subject_list[2])

student_list[0] = Student(f_name_list[3], l_name_list[3], subject_list)
student_list[1] = Student(f_name_list[4], l_name_list[4], subject_list)
student_list[2] = Student(f_name_list[5], l_name_list[5], subject_list)



print("Hello to our little University!\n You are:\n "
      "1. Teacher\n "
      "2. Student")

ii = int(input())
if ii == 1:
    print("Who are you?")
    printTeacher()
    iii = int(input())
    if iii == 1:
        print("Hello", teacher_list[iii - 1].getNameT(), "\n")
        print("What you wanna do?\n"
              "1. Look for all students\n"
              "2. Look for student\n"
              "3. Put a mark to students\n"
              "4. Add a student to your course\n")
        iiii = int(input())
        if iiii == 1:
            print("All students of a class:")
            for jj in range(0,3):
                print(student_list[jj].getNameS())
        elif iiii == 2:
            print("Select a student:(1-3)")
            for jj in range(0, 3):
                print(jj+1, ". ", sep="", end="")
                print(student_list[jj].getNameS())
            jj = int(input())
            print(printStudent(jj-1))

    elif iii == 2:
        print("Hello", teacher_list[iii - 1].getNameT(), "\n")
    elif iii == 3:
        print("Hello", teacher_list[iii - 1].getNameT(), "\n")
    else:
        print("Invalid input")
elif ii == 2:
    print("fsdfs")

else:
    print("Invalid input")
