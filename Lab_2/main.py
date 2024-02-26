from Triangle import Triangle
import turtle as t


triangle = Triangle(100, 100, 100, 0)
t.speed(0)


for i in range(100):
    triangle.random_col()
    triangle.random_pos()
    triangle.draw()

t.mainloop()