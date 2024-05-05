from Triangle import Triangle
import turtle as t

t.speed(0)
triangle = Triangle(100, 100, 100, 0)
triangle.draw()

# поворот трикутника

for i in range(0, 360, 3):
    triangle.rotate_coords(i)
    triangle.set_random_color()
    triangle.draw()

# 100 рандом трикутниківя

for i in range(100):
    triangle.set_random_pos()
    triangle.rotate_coords()
    triangle.set_random_color()
    triangle.draw()

t.mainloop()
