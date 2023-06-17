class People:
    __id = None
    __name = None
    __age = None

    def __init__(self, id, name, age):
        self.__id = id
        self.__name = name
        self.__age = age

    def __str__(self):
        return f"{self.__id} - {self.__name} - {self.__age}"

    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

