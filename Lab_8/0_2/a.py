def calc_shx(x, epsilon):
    # k = 1
    a = x
    S = a
    factorial = 1
    k = 2
    while abs(a / factorial) > epsilon:
        a *= x ** 2
        factorial *= k * (k + 1)
        S += a / factorial
    return S
