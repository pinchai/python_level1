from people import *


class Student(People):
    __subject = None
    __gpa = None

    def __init__(self, id, name, age, subject, gpa):
        super(Student, self).__init__(id, name, age)
        self.__subject = subject
        self.__gpa = gpa

    def __str__(self):
        return super().__str__() + f" - {self.__subject} - {self.__gpa}"

    def setSubject(self, subject):
        self.__subject = subject

    def getSubject(self):
        return self.__subject

    def setGpa(self, gpa):
        self.__gpa = gpa

    def getGpa(self):
        return self.__gpa
