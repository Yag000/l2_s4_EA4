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


print(exponentiation_binaire_rec(2, 4))
print(exponentiation_binaire_rec(2, 5))

print(exponentiation_binaire_rec(3, 3))
print(exponentiation_binaire_rec(3, 4))

print(exponentiation_binaire_rec(5, 3))
print(exponentiation_binaire_rec(5, 4))
