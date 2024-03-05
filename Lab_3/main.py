from Triangle import Triangle
from turtle import *

speed(0)
t = Triangle(100, 100, 100, 0)
t.set_random_color()
t.draw()

t.set_pivot(*t.get_bisec_centre())

for i in range(1, 360, 10):
    t.set_random_color()
    t.rotate(i)
    t.draw()
reset()

t.set_pivot(*t.get_median_centre())
i = 1
while i < 3:
    i += 0.05
    t.set_random_color()
    t.scale(i)
    t.draw()

mainloop()
