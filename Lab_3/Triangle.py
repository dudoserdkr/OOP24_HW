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

    def set_coord2(self, x2, y2):
        self._coord_2 = x2, y2

    def set_color(self, color):
        # assert is_color_exist(color): -- тут повинна бути перевірка на манкі тест, але її ще нема :(
        self._color = color

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
        return self._color

    def get_start(self):
        return self.start

    # endregion

    # region main functions

    @staticmethod
    def _random_angle():
        return rand(1, 360)

    def _radians(self, x):
        if x is None:
            x = self._random_angle()

        return math.radians(x)

    @staticmethod
    def _calculate_rotate(fi, coord: tuple) -> tuple:
        x, y = coord
        x1 = x * math.cos(fi) - y * math.sin(fi)
        y1 = x * math.sin(fi) + y * math.cos(fi)

        return x1, y1

    def rotate_coords(self, x=None):
        fi = self._radians(x)

        self.start = self._calculate_rotate(fi, self.start)
        self._coord_1 = self._calculate_rotate(fi, self._coord_1)
        self._coord_2 = self._calculate_rotate(fi, self._coord_2)

    def _calc_start_pos(self):
        v1 = (self._coord_1[0] + self.start[0],
              self._coord_1[1] + self.start[1])

        v2 = (self._coord_2[0] + self.start[0],
              self._coord_2[1] + self.start[1])

        return v1, v2

    def __calc_dot_rotate(self, x, y, fi):
        for x1, y1 in (self.start, self._coord_1, self._coord_2):
            cur_x, cur_y = x1 - x, y1 - y

            new_x, new_y = self._calculate_rotate(fi, (cur_x, cur_y))

            yield new_x + x, new_y + y

    def rotate_triangle(self, x, y, fi):
        self.start, self._coord_1, self._coord_2 = self.__calc_dot_rotate(x, y, fi)

    def draw(self):
        v1, v2 = self._coord_1, self._coord_2
        t.color(self._color)
        t.up()
        t.setpos(*self.start)
        t.down()
        t.goto(*v1)
        t.goto(*v2)
        t.setpos(*self.start)
        t.up()
    # endregion
