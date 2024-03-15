from ClockFace import ClockFace
import turtle as t


class Hand(ClockFace):

    def _update_hands(self, k):
        h = t.Turtle()
        m = t.Turtle()
        s = t.Turtle()

        for angle_h in range(0, 360, 30):
            self._draw_hand(h, angle_h, self.r // 3, "#220922")

            for angle_m in range(0, 360, 6):
                self._draw_hand(m, angle_m, self.r // 2, "#9e0922")

                for angle_s in range(0, 360, 6 * k):
                    self._draw_hand(s, angle_s, self.r, "#0a00ff")

                    s.undo()
                m.undo()
            h.undo()

    def _draw_hand(self, obj, angle, lenght, color="#000000"):

        obj.up()
        obj.color(color)
        obj.setpos(*self.face_center)
        obj.setheading(90 - angle)
        obj.down()
        obj.forward(lenght)

    def draw_clock(self, k):
        t.up()
        t.setpos(*self.face_center)
        t.dot(5)
        self.draw_face_clock()
        self._update_hands(k)
