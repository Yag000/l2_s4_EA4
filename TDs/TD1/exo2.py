def exponentiation_binaire_rec(m, n):
    if n == 0:
        return 1

    tmp = exponentiation_binaire_rec(m * m, n // 2)

    if n % 2 == 1:
        return tmp * m
    return tmp


def exponentiation_binaire_iter(m, n):
    res = 1
    while n > 0:
        if n % 2 == 1:
            res *= m
        m *= m
        n //= 2
    return res


assert exponentiation_binaire_rec(2, 4) == exponentiation_binaire_iter(2, 4)
assert exponentiation_binaire_rec(2, 5) == exponentiation_binaire_iter(2, 5)
assert exponentiation_binaire_rec(3, 3) == exponentiation_binaire_iter(3, 3)
assert exponentiation_binaire_rec(3, 4) == exponentiation_binaire_iter(3, 4)
assert exponentiation_binaire_rec(5, 3) == exponentiation_binaire_iter(5, 3)
assert exponentiation_binaire_rec(5, 4) == exponentiation_binaire_iter(5, 4)
