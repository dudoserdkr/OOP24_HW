def calc_rec(n):
    a2 = a1 = 1
    b = 3
    S = b / a2
    if n == 1:
        return S

    b *= 3
    S += b / a1
    k = 3
    while k <= n:
        a = a1 / k + a2
        a2 = a1
        a1 = a
        b *= 3
        S += b / a
        k += 1
    return S


if __name__ == '__main__':
    print(calc_rec(23))
