from Numeral import Numeral
import turtle as t
from math import pi, sin, cos


class ClockFace(Numeral):
    color = "#000000"

    def __init__(self, r, x=0, y=0, dot_size=5, width=1):
        super().__init__()
        self.r = r
        self.color = ClockFace.color
        self.face_center = (x, y)
        self.width = width
        self.dot_size = dot_size
        self.vertex_dots = []

    @staticmethod
    def _calc_dots(count):
        """
        :param count:  список точок, з класу Numeral,
        :return: розтавляє пропорційну кожну точку на колі, і повертає їх координати
        """
        step = len(count) / 2

        for i in count:
            difference = (pi / 2) - (i * pi / step)
            x = cos(difference)
            y = sin(difference)
            yield x, y

    def _calculate_circle_positions(self, count, k=1):
        for x, y in count:
            x = x * self.r + self.face_center[0]
            y = y * self.r + self.face_center[1]
            self.vertex_dots += [(x, y)]
            yield x, y, x * k, y * k

    def _draw_time_points(self, count, k):

        circle_positions = self._calc_dots(count)

        dots = list(self._calculate_circle_positions(circle_positions, k))

        for i in range(len(dots)):
            x, y, x1, y1 = dots[i]
            t.up()

            if i % 5 == 0:
                t.color('#8e0922')
                t.width(2)
            else:
                t.color("#000000")
                t.width(1)

            t.setpos(x, y)
            t.down()
            t.goto(x1, y1)
            t.up()

    def _draw_circles(self, k):
        t.up()
        t.setpos(self.face_center[0], self.face_center[1] - self.r)
        t.down()
        t.circle(self.r)
        t.up()
        t.setpos(self.face_center[0], self.face_center[1] - self.r * k)
        t.down()
        t.circle(self.r * k)
        t.up()

    def draw_face_clock(self, k=1.05):
        self._draw_time_points(self.minutes, k)
        self._draw_circles(k)
        self._draw_numerals(self.vertex_dots)
