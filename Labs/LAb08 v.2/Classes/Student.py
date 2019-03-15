from .Person import *
from .Courses_C import *
from .Courses_Py import *
from .Courses_Java import *

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
