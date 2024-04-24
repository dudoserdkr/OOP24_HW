def calc_log(x, epsilon):
    k = 1
    a = x
    S = a
    while abs(a / k) > epsilon:
        k += 1
        a *= -1 ** (k - 1) * x
        S += a / k
    return S
