class upright:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def upright_square(self):
        if self.a > 0 and self.b > 0:
            return self.a * self.b

        else:
            return "Прямокутника не існує"