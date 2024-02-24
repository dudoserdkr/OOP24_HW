import turtle

class Triangle:
    default_color = "#FF0000"

    def __init__(self, x1, y1, x2, y2):
        self.vertrex1 = (x1, y1)
        self.vertrex2 = (x2, y2)
        self.position = (0, 0)
        self.color = "#FF0000"

    def set_position(self, x, y):
        self.position = (x, y)

    def set_color(self, color):
        self.color = color


    def calc_abs_pos(self):
        v1 = (self.position[0] + self.vertrex1[0],
              self.position[1] + self.vertrex1[1])

        v2 = (self.position[0] + self.vertrex2[0],
              self.position[1] + self.vertrex2[1])

        return v1, v2
    def draw(self):
        v1, v2 = self.calc_abs_pos()
        turtle.color(self.color)
        turtle.up()
        turtle.down()
        turtle.goto(*v1)
        turtle.goto(*v2)
        turtle.setpos(*self.position)
        turtle.up()
        turtle.color(Triangle.default_color)


if __name__ == '__main__':
    turtle.speed(1)
    triangle = Triangle(100, 100, 100, 0)
    triangle.draw()
    turtle.clear()

    triangle.set_color("#38915F")
    triangle.set_position(-100, -100)
    triangle.draw()
