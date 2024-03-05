from random import randint as rand
import turtle as t
import math


class Triangle:
    default_color = '#000000'

    def __init__(self, x1, y1=0, x2=0, y2=0):
        if isinstance(x1, Triangle):
            self._coord_1 = x1._coord_1
            self._coord_2 = x1._coord_2
            self._color = x1._color
            self._start = x1._start

        else:
            self._coord_1 = (x1, y1)
            self._coord_2 = (x2, y2)
            self._color = Triangle.default_color
            self._start = (0, 0)

    # region setters
    def set_coord1(self, x1, y1):
        self._coord_1 = x1, y1

    def set_coord2(self, x2, y2):
        self._coord_2 = x2, y2

    def set_color(self, color):
        assert self._is_color_exist(color)

        self._color = color

    def set_start(self, x, y):
        self._start = (x, y)
        self._coord_1, self._coord_2 = self._calc_start_pos()

    def set_random_color(self):
        R = rand(0, 255)
        G = rand(0, 255)
        B = rand(0, 255)

        self._color = f'#{R:02X}{G:02X}{B:02X}'

    def set_random_pos(self):
        x = rand(-500, 500)
        y = rand(-500, 500)

        self._start = (x, y)

    # endregion

    # region getters
    def get_coord_1(self):
        return self._coord_1

    def get_coord_2(self):
        return self._coord_2

    def get_color(self):
        return self._color

    def get_start(self):
        return self._start

    # endregion

    # region main functions

    def

    @staticmethod
    def _random_angle():
        return rand(1, 360)

    @staticmethod
    def _is_color_exist(color_code: str):
        """
        :param color_code: string
        :return: True, якщо такий код кольору існує. False - в іньшому випадку
        """

        if not (color_code.startswith('#') and len(color_code) == 7):
            return False

        for char in color_code[1:]:
            if not (char.isdigit() or char.lower() in 'abcdef'):
                return False

        return True

    def _radians(self, x):
        if x is None:
            x = self._random_angle()

        return math.radians(x)

    @staticmethod
    def _calculate_rotate(fi, coord: tuple) -> tuple:
        """
        :param fi: кут, на який будуть повертатися координати
        :param coord: кортеж (x, y)
        :return: повернуті координати, через матрицю повороту
        """

        x, y = coord
        x1 = x * math.cos(fi) - y * math.sin(fi)
        y1 = x * math.sin(fi) + y * math.cos(fi)

        return x1, y1

    def _calc_start_pos(self):
        """
        Допоміжна функція, що рахує координати двох інших вершин,
        якщо координати вершини start зміняться з (0, 0) на інші
        """
        v1 = (self._coord_1[0] + self._start[0],
              self._coord_1[1] + self._start[1])

        v2 = (self._coord_2[0] + self._start[0],
              self._coord_2[1] + self._start[1])

        return v1, v2

    def _calc_dot_rotate(self, x, y, fi):
        """
        :param x: координати точки, навколо якої трикутник будет повертатись
        :param y: координати точки, навколо якої трикутник будет повертатись
        :param fi: кут, на який трикутник буде повертатись
        :return: повертає 3 кортежа, які містять координати з поворотом
        """

        fi = self._radians(fi)
        for x1, y1 in (self._start, self._coord_1, self._coord_2):
            cur_x, cur_y = x1 - x, y1 - y
            new_x, new_y = self._calculate_rotate(fi, (cur_x, cur_y))

            yield new_x + x, new_y + y

    def rotate(self, x, y, fi):
        """Зміняє основні координати трикутника на повернуть"""
        self._start, self._coord_1, self._coord_2 = self._calc_dot_rotate(x, y, fi)

    def draw(self):
        t.color(self._color)
        t.up()
        t.setpos(*self._start)
        t.down()
        t.goto(*self._coord_1)
        t.goto(*self._coord_2)
        t.setpos(*self._start)
        t.up()
    # endregion
