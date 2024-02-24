class Trap:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def trap_square(self):
        middle = (self.a + self.b) / 2

        q = (((self.a - self.b) ** 2 + self.c ** 2 - self.d ** 2) * 1/(2*(self.a - self.b))) ** 2

        if q >= self.c**2:
            return "Трапеція не існує"

        height = (self.c ** 2 - q) ** 0.5

        S = middle * height

        return S

d = Trap(11, 6, 3, 4)

print(d.trap_square())