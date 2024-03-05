from Triangle import Triangle
from turtle import *

speed(0)
t = Triangle(100, 100, 100, 0)
t.set_start(1, 1)
t.draw()
t.scale(2)
t.draw()
t.rotate(90)
t.draw()
mainloop()
