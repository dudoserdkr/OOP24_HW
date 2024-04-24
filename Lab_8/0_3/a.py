def calc_sum(epsilon, x):
    # S += x ** 2 / (2*k)

    S = 1

    a = 1
    k = 1

    while abs(a) > epsilon:
        a *= x ** 2 / (2 * k)
        S = S + a
        k += 1

    return S


print(calc_sum(10 ** (-12), 15))
