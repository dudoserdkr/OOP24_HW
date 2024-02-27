from Triangle import Triangle
import turtle as t


triangle = Triangle(100, 100, 100, 0)
triangle.draw()

# поворот трикутника + 100 рандом трикутниківя

for i in range(100):
    triangle.random_pos()
    triangle.rotate_coords()
    triangle.random_col()
    triangle.draw()