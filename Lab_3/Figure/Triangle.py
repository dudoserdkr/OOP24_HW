from Figure import Figure
import turtle as t


class Triangle(Figure):
    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        self.vertex1 = (x1, y1)
        self.vertex2 = (x2, y2)
        self._dimention = 2

    def get_dimention(self):
        return self._dimention

    @staticmethod
    def get_side_len(v1, v2: tuple) -> float:
        abs_len = ((v2[0] - v1[0]) ** 2 + (v2[1] - v1[1]) ** 2) ** 0.5
        return abs_len

    def _get_sides(self) -> tuple:
        """
        AB, AC, CB - lengts of Triangle sides
        :return: AB, AC, CB - lengts of Triangle sides
        """
        assert self._dimention != 3
        AB = self.get_side_len(self.start, self.vertex1)
        AC = self.get_side_len(self.start, self.vertex2)
        CB = self.get_side_len(self.vertex1, self.vertex2)
        return AB, AC, CB

    def get_perimetr(self):
        assert self._dimention != 3
        sides = self._get_sides()
        P = sum(sides)
        return P

    def get_square(self):
        assert self._dimention != 3
        AB, AC, CB = self._get_sides()
        p = (AB + AC + CB) / 2
        S = (p * (p - AB) * (p - AC) * (p - CB)) ** 0.5
        return S

    def get_squareSurface(self):
        assert self._dimention == 2

    def get_squareBase(self):
        assert self._dimention == 2

    def get_height(self):
        assert self._dimention == 2

    def figure_vol(self):
        pass

    def get_volume(self):
        if self._dimention == 2:
            return self.get_square()
        else:
            return self.figure_vol()

    def _draw_vertex(self, *args):
        t.up()
        t.setpos(*self.start)
        t.down()
        for vertex in args:
            vertex = self.calc_vertex(*vertex)
            vertex = self.scale_vertex(*vertex)
            vertex = self.rotation_calc(*vertex)
            t.goto(*vertex)

        t.goto(*self.start)
        t.up()

    def draw(self):
        v1 = self.start
        v2 = self.vertex1
        v3 = self.vertex2
        self._draw_vertex(v1, v2, v3)


if __name__ == '__main__':
    t1 = Triangle(100, 100, 100, 0)
    t1.draw()
    t1.rotation_angel = 30
    t1.draw()
    t1.scale_coords = (2, 5)
    t1.draw()
    print(t1.get_perimetr())
    t.mainloop()
