class squre:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def D(self):
        return self.b ** 2 - 2 * self.a * self.b

    def solutions(self):
        D = self.D()
        try:
            if D < 0:
                return "No solutions"

            elif D == -1:
                return "Нескінченна кількість розв"

            elif D == 0:
                x = (-1 * self.b + D ** 0.5) * 1 / (2*self.a)
                return f"Solution: x = {x}"

            else:
                x1 = (-1 * self.b + D ** 0.5) * 1 / (2*self.a)
                x2 = (-1 * self.b - D ** 0.5) * 1 / (2*self.a)
                return f"Solution: x1 = {x1}\nx2 = {x2}"

        except ZeroDivisionError:
            if self.b == 0 and self.c == 0:
                return "Неск кільк розв"
            elif self.b == 0 and self.c != 0:
                return "No solutions"
            else:
                x = -1 * self.c / self.b
                return f"Solution: x = {x}"


obj = squre(1, 3, 2)

print(obj.solutions())