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
            else:
                continue

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
        self.vertex_dots = None

    def _calc_dots(self, count):
        """
        :param count:  список точок, з класу Numeral,
        :return: розтавляє пропорційну кожну точку на колі, і повертає їх координати
        """
        step = len(count) / 2

        for i in count:
            difference = (pi / 2) - (i * pi / step)
            x = self.r * cos(difference) + self.face_center[0]
            y = self.r * sin(difference) + self.face_center[1]
            yield x, y

    def _draw_dots(self, arr):

        t.up()

        for i in range(len(arr)):
            x, y = arr[i]
            t.setpos(x, y)

            if i % 5 == 0:
                t.dot(2 * self.dot_size, "#8e0922")

            else:
                t.dot(self.dot_size, self.color)

    def draw(self):
        t.up()
        t.setpos(self.face_center[0], self.face_center[1] - self.r)
        t.width(self.width)
        t.down()
        t.circle(self.r)
        t.up()

        arr = self._calc_dots(self.minutes)
        arr = list(arr)

        self.vertex_dots = arr
        self._draw_dots(arr)
        self._draw_numerals(arr)


class Hand(ClockFace):

    def update_hands(self, k):
        h = t.Turtle()
        m = t.Turtle()
        s = t.Turtle()

        arr = self.vertex_dots
        for i in range(len(arr)):
            x1, y1 = arr[i]
            self.draw_hand(h, x1, y1, "#8e0922")

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
        obj.up()
        obj.setpos(*self.face_center)
        obj.color(color)
        obj.down()
        obj.goto(x, y)


if __name__ == '__main__':
    H = Hand(300, 5, 5)
    H.draw()
    H.update_hands(2)
    t.mainloop()
