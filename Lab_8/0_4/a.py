def calc_limit(x, epsilon):
    a1 = x
    a = (abs(4 * a1 ** 2 - 2 * x)) ** 0.5
    diffrence = abs(a - a1)
    while diffrence > epsilon:
        a1 = a
        a = (abs(4 * a1 ** 2 - 2 * x)) ** 0.5
        diffrence = abs(a - a1)
    return a


if __name__ == '__main__':
    print(calc_limit(1, 10 ** (-1)))
