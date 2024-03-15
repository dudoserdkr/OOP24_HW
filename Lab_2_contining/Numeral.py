import turtle as t


class Numeral:
    def __init__(self, font='Arial', size=5, type_font='normal'):
        self.minutes = [i for i in range(0, 60)]
        self.hours = [12] + [i for i in range(1, 12)]
        self.font = font
        self.font_size = size
        self.type_font = type_font

    def _draw_numerals(self, arr, k=0.9):
        """
        :param k: коефіцієнт, що зменшує координати з масиву arr, щоб цифри були в середині циферблата
        :param arr: передає список координат точок
        :return: None, малює цифри на точках, які вже нанесені на круг
        """

        hour = 0
        t.up()

        for i in range(len(arr)):
            x, y = arr[i]

            x, y = x * k, y * k

            t.setpos(x, y)

            if i % 5 == 0:
                t.write(f"{self.hours[hour]}", font=(self.font, 3 * self.font_size, self.type_font))
                hour += 1

            t.up()
