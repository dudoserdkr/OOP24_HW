from Triangle import Triangle
from turtle import *

if __name__ == '__main__':
    speed(0)
    t = Triangle(100, 100, 100, 0)
    t.draw()
    for i in range(0, 360, 10):
        t.rotate_triangle(100, 0, i)
        t.draw()
    mainloop()
