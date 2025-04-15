class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age} лет'

people = [Person('Anya', 22),    Person('Fufel', 19),    Person('Sashko', 35)]

for person in people:
    print(person)
