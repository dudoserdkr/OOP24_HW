# sqrt(1 + x)

def calc_sqrt(x, epsilon):
    # k = 1
    a = x / 2
    S = a
    k = 2
    while abs(a) > epsilon:
        a *= -1 ** (k + 1) * (2 * k - 1) / (2 * k) * x
        S += a
        k += 1
    return 1 + S
