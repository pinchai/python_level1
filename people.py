class People:
    __id = None
    __name = None
    __year_of_birth = None

    def __init__(self, id, name, year_of_birth):
        self.__id = id
        self.__name = name
        self.__year_of_birth = year_of_birth

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setYearOfBirth(self, year_of_birth):
        self.__year_of_birth = year_of_birth

    def getYearOfBirth(self):
        return self.__year_of_birth

    def __cal(self):
        current_year = 2023
        return current_year - self.__year_of_birth

    def __str__(self):
        return f"{self.__id}\t{self.__name}\t{self.__cal()}"


