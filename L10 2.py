class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Год выпуска: {self.year}")

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(f"Количество дверей: {self.doors}")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_type):
        super().__init__(brand, year)
        self.type = engine_type

    def display_info(self):
        super().display_info()
        print(f"Тип двигателя: {self.type}")

car = Car("Matiz", 2012, 4)
motorcycle = Motorcycle("Yamaha", 2022, "двухтактный")

car.display_info()
motorcycle.display_info()
