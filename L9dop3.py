class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.car_type = car_type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def setYear(self, year):
        self.year = year
        print(f"Год выпуска: {self.year}")

    def setType(self, car_type):
        self.car_type = car_type
        print(f"Тип: {self.car_type}")

    def setColor(self, color):
        self.color = color
        print(f"Цвет: {self.color}")