class Math:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def addition(self):
        print(f"{self.a} + {self.b} = {self.a + self.b}")

    def subtraction(self):
        print(f"{self.a} - {self.b} = {self.a - self.b}")

    def multiplication(self):
        print(f"{self.a} * {self.b} = {self.a * self.b}")

    def division(self):
        if self.b != 0:
            print(f"{self.a} / {self.b} = {self.a / self.b}")
        else:
            print("Ошибка")