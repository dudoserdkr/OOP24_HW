# 1/(1+x)^2

def calc_function(x, epsilon):
    k = 1
    S = a = 1
    while abs(a * k) > epsilon:
        k += 1
        a *= x
        S += -1 ** (k - 1) * k * a
    return S
