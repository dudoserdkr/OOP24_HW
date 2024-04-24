# log((1+x)/(1-x))

def calc_function(x, epsilon):
    k = 1
    a = x
    S = a / k
    while abs(a / k) > epsilon:
        k += 2
        a *= x ** 2
        S += a / k
    return S
