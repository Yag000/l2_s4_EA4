#!/usr/bin/env python3


""" 
1. 
for i in range(9):
	print(i)

2.
list(range(9))
list(range(2,11))
list(range(2,11,2))
list(range(10,0,-2))

3.
l1 = [i*2 for i in range(7)]
l2 = [i for i in "abcdef"]
l1.reverse()
l3 = [i for i in zip(l2,l1)]

4.
l3[2:5]
l3[1::2]
l4 = l3.copy()
l5 = [0 if i%3 == 2 else (i+1)*7 for i in range(0,20)]
"""


def f(l):
    l[0] += 2022


def g(l):
    l[-1] += 2022


def exercice6():
    l = list(range(2, 37, 3))
    lg = l[: len(l) // 2]
    ld = l[len(l) // 2 :]
    print()
    print(l, lg, ld)
    ld[0] += 2022
    print(l, lg, ld)
    f(lg)
    print(l, lg, ld)
    g(l)
    print(l, lg, ld)
    g(l[: len(l) // 2])
    print(l, lg, ld)


#
# A REMPLIR
#
def crible_eratosthene(n):
    # calcule la table de booléens où la i-ème position est True
    # si et seulement si i est un nombre premier.
    res = [True] * (n + 1)
    res[0] = False
    res[1] = False

    for i in range(2, int(n**0.5) + 1):
        if res[i]:
            res[2 * i :: i] = [False] * ((n - 2 * i) // i + 1)

    return res


def test_crible(n):
    c = crible_eratosthene(n)
    for i in range(len(c)):
        if c[i]:
            print(i, end=" ")
    print()


#
# A REMPLIR
#
def somme_impairs(x):
    return sum(list(range(1, x + 1, 2)))


def test_somme(n):
    # teste que la somme des entiers impairs de 1 à x =
    #    (x/2)*(x/2) si x est pair
    #    (x+1)/2*(x+1)/2 sinon
    # pour tout 1 <= x <= n
    for x in range(n):
        if x % 2 == 0:
            if somme_impairs(x) != (x // 2) ** 2:
                return False
        else:
            if somme_impairs(x) != ((x + 1) // 2) ** 2:
                return False

    return True


# AJOUTER D'AUTRES TESTS
#  [valeur_x, resultat_attendu]
def testDataSomme():
    """retourne un jeu de tests"""
    return [[0, 0], [3, 4], [24, 144], [-3, 0]]


#
# NE PAS MODIFIER
#
def testOp(op, data):
    print("\n\n* Test function %s:" % op.__name__)
    score = 0
    ldata = len(data)
    for i, dt in enumerate(data):
        print("** test %d/%d : " % (i + 1, ldata), end="")
        x = dt[0]
        refr = dt[1]
        r = op(x)
        if r == refr:
            score += 1
            print("ok")
        else:
            print("ECHEC")
            print("    entree  : %s" % x)
            print("    calcule : %s" % r)
            print("    attendu : %s" % refr)
    print("** Score %d/%d" % (score, ldata))


if __name__ == "__main__":
    test_crible(50)
    exercice6()
    testOp(somme_impairs, testDataSomme())
