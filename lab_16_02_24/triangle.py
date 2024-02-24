class triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            P = self.a + self.b + self.c
            p = P / 2
            S = ((p-a)*(p-b)*(p-c)) ** 0.5
            return S
        else:
            return "Трикутника не існує"