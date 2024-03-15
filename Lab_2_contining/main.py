from Hand import Hand
import turtle as t

if __name__ == '__main__':
    H = Hand(250, 5, 5)
    t.speed(0)
    H.draw_clock(1)
    t.mainloop()
