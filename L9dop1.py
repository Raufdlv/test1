class Student:
    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

student1 = Student("Pavel", 34, "12C")
student2 = Student("Anna", 20, "12B")
student3 = Student("Oleg", 19, "11A")
student4 = Student("Maria", 21, "13C")
student5 = Student("Nikolay", 22, "14D")