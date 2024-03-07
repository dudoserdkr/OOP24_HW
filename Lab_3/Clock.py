from math import pi, sin, cos
import turtle as t


class Numeral:
    def __init__(self, font='Arial', size=5, type_font='normal'):
        self.minutes = [i for i in range(0, 60)]
        self.hours = [12] + [i for i in range(1, 12)]
        self.font = font
        self.font_size = size
        self.type_font = type_font

    def _draw_numerals(self, arr, k=0.9):
        """
        :param k: коефіцієнт, що зменшує координати з масиву arr, щоб цифри були в середині циферблата
        :param arr: передає список координат точок
        :return: None, малює цифри на точках, які вже нанесені на круг
        """

        hour = 0
        t.up()

        for i in range(len(arr)):
            x, y = arr[i]

            x, y = x * k, y * k

            t.setpos(x, y)

            if i % 5 == 0:
                t.write(f"{self.hours[hour]}", font=(self.font, 3 * self.font_size, self.type_font))
                hour += 1

            t.up()


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


class Hand(ClockFace):

    def update_hands(self, k):
        h = t.Turtle()
        m = t.Turtle()
        s = t.Turtle()

        arr = self.vertex_dots
        for i in range(0, len(arr), 5):
            x1, y1 = arr[i]
            self.draw_hand(h, x1, y1, "#220922")

            for d in range(len(arr)):
                x2, y2 = arr[d]
                self.draw_hand(m, x2, y2, "#9e0922")

                for v in range(0, len(arr), k):
                    x3, y3 = arr[v]
                    self.draw_hand(s, x3, y3, "#99ff99")
                    s.undo()
                m.undo()
            h.undo()

    def draw_hand(self, obj, x, y, color="#000000"):
        """

        :param obj: передається об'єкт класу Turtle
        :param x: координата точки
        :param y: координата точки
        :param color: колір стрілки
        :return: малює стрілку
        """

        obj.up()
        obj.setpos(*self.face_center)
        obj.color(color)
        obj.down()
        obj.goto(x, y)

    def draw_clock(self, k):
        t.up()
        t.setpos(*self.face_center)
        t.dot(5)
        self.draw_face_clock()
        self.update_hands(k)


if __name__ == '__main__':
    H = Hand(300, 5, 5, )
    t.speed(0)
    H.draw_clock(30)
    t.mainloop()
