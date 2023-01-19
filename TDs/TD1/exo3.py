def eval_poly_naif(poly, x):
    res = 0
    for i in range(len(poly)):
        res += poly[i] * x**i
    return res


assert eval_poly_naif([1, 1, 1, 1, 1], 3) == 121
