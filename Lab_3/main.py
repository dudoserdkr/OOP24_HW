from Triangle import Triangle
from turtle import *

speed(0)
t = Triangle(100, 100, 100, 0)
print(t._is_color_exist("#188431"))
print(t.get_color())
t.draw()
t.set_random_color()
t.rotate(0, 0, 30)
t.draw()
t.set_random_color()
t.rotate(0, 0, 750)
t.draw()
mainloop()
