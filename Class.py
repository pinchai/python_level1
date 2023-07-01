class Class:
    __name = None
    __no = None
    __year = None
    __student = None

    def __init__(self, name, no, year, student):
        self.__name = name
        self.__no = no
        self.__year = year
        self.__student = student

    def getNo(self):
        return self.__no

    def getStudent(self):
        return self.__student

    def __str__(self):
        return f"Group: {self.__name}{self.__no}\n" \
               f"Year: {self.__year}\n" \
               f"Student: {self.__student}"

    def __add__(self, other):
        name = self.__name
        no = f"{self.__no}{other.getNo()}"
        year = self.__year
        student = self.__student + other.getStudent()
        return f"New Group: {name}{no}\n" \
               f"New Year: {year}\n" \
               f"New Student: {student}"
