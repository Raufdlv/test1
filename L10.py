class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Гав-гав!")

class Cat(Animal):
    def make_sound(self):
        print("Мяу!")

class Cow(Animal):
    def make_sound(self):
        print("Муу!")

dog = Dog()
cat = Cat()
cow = Cow()

dog.make_sound()
cat.make_sound()
cow.make_sound()
