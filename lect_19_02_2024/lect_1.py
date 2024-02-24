import copy



class Triangle:
    triangle_id = 0 # статичне поле класу
    def __init__(self, a=None, b=None, c=None):
        global triangle_id

        if isinstance(a, Triangle):
            self.a = a.a
            self.b = a.b
            self.c = a.c

        else:
            self.a = a
            self.b = b
            self.c = c

        self.id = Triangle.triangle_id
        triangle_id += 1

    # def __init__(self, otherTriangle):
    #     global triangle_id
    #     self.a = otherTriangle.a
    #     self.b = otherTriangle.b
    #     self.c = otherTriangle.c
    #     self.id = triangle_id
    #     triangle_id += 1

    def perimetr(self):
        return (self.a + self.b + self.c)

    def area(self):
        p = self.perimetr()
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5

    def show(self):
        print("Triangle id =", self.id, "edges: ", self.a, self.b, self.c)


if __name__ == '__main__':
    # t = Triangle(3, 4 ,5)
    # t.show()
    # t2 = Triangle(9, 12, 15)
    # t2.show()
    # t3 = Triangle(t)
    # t3.show()

    print(Triangle.triangle_id)

# Конструктор копіювання = конструктор, список формальних параметрів якого складаєтсья з єдиного аргументу - посилання на інший екземпляр цього ж класу
# Перевантаження - один із засобів реалізації поліморфізму, що полягає у можилвості створення кількох реалізацій функції(методі) ...
