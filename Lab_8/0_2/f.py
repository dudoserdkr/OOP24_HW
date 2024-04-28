# 1/(1 + x^2)

def calc_function(x, epsilon):
    k = 0
    a = 1
    S = a
    while abs(a) > epsilon:
        k += 1
        a *= x ** 2
        S += -1 ** k * a
    return S
