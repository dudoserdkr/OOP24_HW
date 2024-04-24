def calc_sum(n):
    S1 = 2
    S2 = 4
    if n == 1:
        return S1
    elif n == 2:
        return S2

    C = 4

    a1 = 0
    a2 = 1

    b = 1
    k = 3

    while k <= n:
        a = a2 / k + a1 * b
        b = b + a2
        a1 = a2
        a2 = a
        C *= 2
        S2 += C / (a + b)
        k += 1
    return S2


if __name__ == '__main__':
    print(calc_sum(234))
