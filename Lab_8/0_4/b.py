def calc_limit(x, epsilon):
    a1 = x
    a = (16 + x) / (1 + abs(a1 ** 3))
    diffrence = abs(a - a1)
    while diffrence > epsilon:
        a1 = a
        a = (16 + x) / (1 + abs(a1 ** 3))
        diffrence = abs(a - a1)
    return a


if __name__ == '__main__':
    print(calc_limit(0.001, 10 ** (-1)))
