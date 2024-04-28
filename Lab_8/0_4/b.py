def calc_limit(x, epsilon):
    n = int(1 / epsilon)

    a1 = x
    a = (16 + x) / (1 + abs(a1 ** 3))

    for _ in range(1, n + 1):
        a1 = a
        a = (16 + x) / (1 + abs(a1 ** 3))
    return a


if __name__ == '__main__':
    print(calc_limit(1, 0.00043024320))
