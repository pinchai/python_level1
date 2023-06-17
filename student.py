from people import *


class Student(People):
    __subject = None
    __gpa = None

    def __init__(self, id, name, year_of_birth, subject, gpa):
        super(Student, self).__init__(id, name, year_of_birth)
        self.__subject = subject
        self.__gpa = gpa

    def __str__(self):
        return super().__str__() + f"\t{self.__subject}\t{self.__gpa}"
