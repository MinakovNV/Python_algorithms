from .Person import*

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
