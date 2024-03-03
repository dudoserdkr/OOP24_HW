from random import randint as rand
import turtle as t
import math


class Triangle:
    default_color = '#000000'

    def __init__(self, x1, y1, x2, y2):
        self._coord_1 = (x1, y1)
        self._coord_2 = (x2, y2)
        self._color = Triangle.default_color
        self.start = (0, 0)

    # region setters
    def set_coord1(self, x1, y1):
        self._coord_1 = x1, y1

    def set_coord1(self, x2, y2):
        self._coord_2 = x2, y2

    def set_color(self, color):
        # assert is_color_exist(color): -- тут повинна бути перевірка на манкі тест, але її ще нема :(
        self.color = color

    def set_start(self, x, y):
        self.start = (x, y)

    def set_random_color(self):
        R = rand(0, 255)
        G = rand(0, 255)
        B = rand(0, 255)

        self._color = f'#{R:02X}{G:02X}{B:02X}'

    def set_random_pos(self):
        x = rand(-500, 500)
        y = rand(-500, 500)

        self.start = (x, y)

    # endregion

    # region getters
    def get_coord_1(self):
        return self._coord_1

    def get_coord_2(self):
        return self._coord_2

    def get_color(self):
        return self.color

    def get_start(self):
        return self.start

    # endregion

    # region main functions

    def _random_angle(self):
        return rand(1, 360)

    def _radians(self, x):
        if x is None:
            x = self._random_angle()

        return math.radians(x)

    def _calculate_rotate(self, fi):
        x1 = self._coord_1[0] * math.cos(fi) - self._coord_1[1] * math.sin(fi)
        y1 = self._coord_1[0] * math.sin(fi) + self._coord_1[1] * math.cos(fi)
        x2 = self._coord_2[0] * math.cos(fi) - self._coord_2[1] * math.sin(fi)
        y2 = self._coord_2[0] * math.sin(fi) + self._coord_2[1] * math.cos(fi)

        return (x1, y1), (x2, y2)

    def rotate_coords(self, x=None):
        fi = self._radians(x)
        self._coord_1, self._coord_2 = self._calculate_rotate(fi)

    def _calc_start_pos(self):
        v1 = (self._coord_1[0] + self.start[0],
              self._coord_1[1] + self.start[1])

        v2 = (self._coord_2[0] + self.start[0],
              self._coord_2[1] + self.start[1])

        return v1, v2

    def draw(self):
        v1, v2 = self._calc_start_pos()
        t.color(self._color)
        t.up()
        t.setpos(*self.start)
        t.down()
        t.goto(*v1)
        t.goto(*v2)
        t.setpos(*self.start)
        t.up()
    # endregion
