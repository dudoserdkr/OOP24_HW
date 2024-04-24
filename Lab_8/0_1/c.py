def calc_rec(n):
    factorial = 1
    a2 = 1
    S = factorial / a2
    if n == 1:
        return S
    k = 2

    a1 = 1
    factorial *= k
    c = 4

    S += factorial / a1
    k = 3
    while k <= n:
        factorial *= k
        c *= 2
        a = a1 + a2 / c
        a2 = a1
        a1 = a
        S += factorial / a
    return S
