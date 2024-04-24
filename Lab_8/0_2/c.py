# 1/(1+x)
def calc_function(x, epsilon):
    k = 0
    a = 1
    S = a
    while abs(a) > epsilon:
        k += 1
        a *= -1 ** k * x
        S += a
    return S
