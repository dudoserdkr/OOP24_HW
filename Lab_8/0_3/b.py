def calc_series(x, epsilon):
    k = 0
    S = a = x
    difference = abs(a)
    while difference > epsilon:
        k += 1
        a *= -1 * x ** 2 / k
        S += a / (2 * k + 1)
    return S
