import turtle as t
from math import pi, sin, cos


class Numeral:
    def __init__(self, font='Arial', size=5, type='normal'):
        self.minutes = [i for i in range(1, 61)]
        self.hours = [i for i in range(1, 13)]
        self.font = font
        self.size = size
        self.type = type


class Clock_face(Numeral):
    color = "#000000"

    def __init__(self, r=100, x=0, y=0):
        super().__init__()
        self.r = r
        self.real_centre = (x, y)
        self.centre = (x, y - self.r)
        self.color = Clock_face.color
        self.circle_dots = None

    def _dots(self, count):
        start_pos = pi / 2
        step = len(count) / 2

        for i in count:
            difference = i * pi / step
            x = self.r * cos(start_pos - difference)
            y = self.r * sin(start_pos - difference)
            yield x, y

    def _face_draw(self, count, color="#000000", size=5):
        t.up()

        i = 0
        hour = 1
        self.circle_dots = self._dots(count)
        for x, y in self.circle_dots:

            i += 1
            t.setpos(x, y)

            if i % 5 == 0:
                t.write(f'{hour}', font=("Arial", int(size * 2 * 1.6), "normal"))
                t.dot(2 * size, color)
                hour += 1
            else:
                t.dot(size, self.color)

            t.up()

    def draw_face(self):
        self._face_draw(self.minutes, "#8e0922", 5)

    def draw(self):
        x, y = self.centre
        t.up()
        t.setpos(x, y)
        t.down()
        t.circle(self.r)
        t.up()
        self.draw_face()


class Hand(Clock_face):
    def __init__(self):
        super().__init__()

    def draw_hand(self, k):
        t.up()
        t.speed(3)
        arr = list(self.circle_dots)
        for i in range(0, len(arr), k):
            x, y = arr[i]
            t.setpos(*self.real_centre)
            t.down()
            t.width(5)
            t.goto(x, y)
            t.up()
            t.clear()


if __name__ == '__main__':
    t.speed(0)
    c = Clock_face(300)
    c.draw()

    t.setpos(0, 0)
    t.down()
    t.dot(10, )
    t.up()
    h = Hand()
    h.draw_hand(5)
    t.mainloop()
