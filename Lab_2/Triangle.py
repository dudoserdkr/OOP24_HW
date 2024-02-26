from random import randint as rand
import turtle as t


class Triangle:

    color = '#000000'

    def __init__(self, x1, y1, x2, y2, color=None):
        self.coord_1 = (x1, y1)
        self.coord_2 = (x2, y2)
        if color is not None:
            self.color = color

        self.start = (0, 0)


    def random_col(self):

        R = rand(0, 255)
        G = rand(0, 255)
        B = rand(0, 255)

        self.color = f'#{R:02X}{G:02X}{B:02X}'


    def random_pos(self):
        x = rand(-500, 500)
        y = rand(-500, 500)

        self.start = (x, y)


    def start_pos(self, x=0, y=0):
        self.start = (x, y)


    def calc_start_pos(self):
        v1 = (self.coord_1[0] + self.start[0],
                        self.coord_1[1] + self.start[1])

        v2 = (self.coord_2[0] + self.start[0],
                        self.coord_2[1] + self.start[1])

        return v1, v2


    def draw(self):
        v1, v2 = self.calc_start_pos()
        t.color(self.color)
        t.up()
        t.setpos(*self.start)
        t.down()
        t.goto(*v1)
        t.goto(*v2)
        t.setpos(*self.start)
        t.up()


if __name__ == "__main__":
    triangle = Triangle(100, 100, 100, 0)
    triangle.draw()
    t.clear()


