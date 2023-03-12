#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

version = sys.version_info
if version.major < 3:
    sys.exit(
        "Python2 n'est PLUS supporté depuis le 1er Janvier 2020, merci d'installer Python3"
    )

import random
from time import process_time as clock

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    sys.exit("Le module matplolib est nécessaire pour ce TP.")


############################################################
# Exercice 1.1
#
# Tri selection
#


def find_minimum_index(T, index):
    min_value, minimum_index = T[index], index

    for i in range(index, len(T)):
        if min_value <= T[i]:
            continue
        min_value = T[i]
        minimum_index = i

    return minimum_index


def triSelection(T):
    for i in range(len(T) - 1):
        minimum_index = find_minimum_index(T, i)
        T[i], T[minimum_index] = T[minimum_index], T[i]

    return T


############################################################
# Exercice 1.2
#
# randomPerm prend en paramètre un entier n et renvoie une
# permutation aléatoire de longueur n dont l'algorithme s'appuie
# sur le tri sélection
#


def randomPerm(n):
    T = [i + 1 for i in range(n)]
    for i in range(n - 1):
        index = random.randint(i + 1, len(T) - 1)
        T[i], T[index] = T[index], T[i]

    return T


############################################################
# Exercice 1.3
#
# testeQueLaFonctionTrie prend en paramètre une fonction de
# tri f et l’applique sur des permutations aléatoires de
# taille i variant de 2 à 100 et vérifie que le résultat est
# un tableau trié
#


def testeQueLaFonctionTrie(f):
    for i in range(2, 101):
        tab = randomPerm(i)
        sorted_tab = f(tab.copy())
        if sorted_tab != [j + 1 for j in range(i)]:
            print("The array was not properly sorted : ", tab)
            print("The function returned : ", sorted_tab)
            return False

    return True


############################################################
# Exercice 1.4
#
# randomTab prend des entiers n, a et b et renvoie un tableau
# aléatoire de taille n contenant des entiers compris entre
# les bornes a et b.
#


def randomTab(n, a, b):
    T = [0] * n
    for i in range(n):
        T[i] = random.randint(a, b)
    return T


############################################################
# Exercice 1.5
#
# derangeUnPeu prend des entiers n, k et un booléen rev et
# effectue k échanges entre des positions aléatoires sur la
# liste des entiers de 1 à n si rev vaut False ou sur la
# liste des entiers n à 1 si rev vaut True.
#


def derangeUnPeu(n, k, rev):
    T = [n - i for i in range(n)] if rev else [i + 1 for i in range(n)]

    for _ in range(k):
        a, b = random.randint(0, n - 1), random.randint(0, n - 1)
        T[a], T[b] = T[b], T[a]

    return T


############################################################
# Exercice 2.1
#
# Trois variantes du tri par insertion L échanges successifs,
# insertion directe à la bonne position, et avec recherche
# dichotomique de la position
#


def triInsertionEchange(T):
    for i in range(1, len(T)):
        for j in range(i, 0, -1):
            if T[j - 1] > T[j]:
                T[j - 1], T[j] = T[j], T[j - 1]
            else:
                break
    return T


def shiftByOne(T, new_index, old_index):
    """
    Déplace un element d'un tableau vers la gauche de
    la liste dans la position old_index vers la position
    new_index en faisant des échanges successifs.
    """

    tmp = T[old_index]
    for i in range(old_index, new_index, -1):
        T[i] = T[i - 1]
    T[new_index] = tmp


def triInsertionRotation(T):
    for i in range(1, len(T)):
        for j in range(i - 1, -1, -1):
            if T[j] < T[i]:
                break
            if j == 0 or T[j] >= T[i] and T[j - 1] <= T[i]:
                shiftByOne(T, j, i)
                break
    return T


def findCorrectIndexDichotomy(T, value, start, end):
    """
    Recherche dichotomique de la position d'un element dans un tableau trié.
    """
    if start == end:
        return start
    middle = (start + end) // 2
    if T[middle] < value:
        return findCorrectIndexDichotomy(T, value, middle + 1, end)
    return findCorrectIndexDichotomy(T, value, start, middle)


def triInsertionRapide(T):
    for i in range(1, len(T)):
        index = findCorrectIndexDichotomy(T, T[i], 0, i)
        shiftByOne(T, index, i)

    return T


############################################################
# Exercice 2.2
#
# Tri fusion
#


def fusion(T1, T2):
    """
    Fusionne deux tableaux en un seul tableau de manière itérative.
    """
    n1 = len(T1)
    n2 = len(T2)
    T12 = [0] * (n1 + n2)

    # index des tableaux T1 et T2
    i1 = 0
    i2 = 0
    # index du tableau final
    i = 0

    # On fusionne les deux tableaux en un seul.
    # On parcourt les deux tableaux en même temps
    # et on ajoute l'élément le plus petit dans
    # le tableau final
    while i1 < n1 and i2 < n2:
        if T1[i1] < T2[i2]:
            T12[i] = T1[i1]
            i1 += 1
        else:
            T12[i] = T2[i2]
            i2 += 1
        i += 1

    # On ajoute les éléments restants dans le tableau final
    while i1 < n1:
        T12[i] = T1[i1]
        i1 += 1
        i += 1
    while i2 < n2:
        T12[i] = T2[i2]
        i2 += 1
        i += 1

    return T12


def triFusion(T, deb=0, fin=None):
    if fin is None:
        fin = len(T)
    if fin - deb < 2:
        return T[deb:fin]
    milieu = (deb + fin) // 2
    gauche = triFusion(T, deb, milieu)
    droite = triFusion(T, milieu, fin)
    return fusion(gauche, droite)


############################################################
# Exercice 2.3
#
# Tri à bulles
#


def triBulles(T):
    for i in range(len(T), 0, -1):
        for j in range(0, i - 1):
            if T[j + 1] < T[j]:
                T[j + 1], T[j] = T[j], T[j + 1]

    return T


############################################################
# Exercice 3.1
#
# Trie par insertion le sous-tableau T[debut::gap] de T
#


def triInsertionPartiel(T, gap, debut):
    for i in range(debut, len(T), gap):
        for j in range(i, debut, -gap):
            if T[j - gap] > T[j]:
                T[j - gap], T[j] = T[j], T[j - gap]
            else:
                break
    return T


############################################################
# Exercice 3.2
#
# Tri Shell
#


def triShell(T):
    for gap in [57, 23, 10, 4, 1]:
        for i in range(gap):
            triInsertionPartiel(T, gap, i)
    return T


##############################################################
#
# Mesure du temps
#


def mesure(algo, T):
    debut = clock()
    algo(T)
    return clock() - debut


def mesureMoyenne(algo, tableaux):
    return sum([mesure(algo, t[:]) for t in tableaux]) / len(tableaux)


couleurs = [
    "b",
    "g",
    "r",
    "m",
    "c",
    "k",
    "y",
    "#ff7f00",
    ".5",
    "#00ff7f",
    "#7f00ff",
    "#ff007f",
    "#7fff00",
    "#007fff",
]

marqueurs = [
    "o",
    "^",
    "s",
    "*",
    "+",
    "d",
    "x",
    "<",
    "h",
    ">",
    "1",
    "p",
    "2",
    "H",
    "3",
    "D",
    "4",
    "v",
]


def courbes(algos, tableaux, styleLigne="-"):
    x = [t[0] for t in tableaux]
    for i, algo in enumerate(algos):
        print("Mesures en cours pour %s..." % algo.__name__)
        y = [mesureMoyenne(algo, t[1]) for t in tableaux]
        plt.plot(
            x,
            y,
            color=couleurs[i % len(couleurs)],
            marker=marqueurs[i % len(marqueurs)],
            linestyle=styleLigne,
            label=algo.__name__,
        )


def affiche(titre):
    plt.xlabel("taille du tableau")
    plt.ylabel("temps d'execution")
    plt.legend(loc="upper left")
    plt.title(titre)
    plt.show()


def compareAlgos(algos, taille=1000, pas=100, ech=5):
    # taille = 1000 : taille maximale des tableaux à trier
    # pas = 100 : pas entre les tailles des tableaux à trier
    # ech = 5 : taille de l'échantillon pris pour faire la moyenne
    for tri in algos:
        if testeQueLaFonctionTrie(tri):
            print(tri.__name__ + ": OK")
        else:
            print(tri.__name__ + ": échoue")
    print()
    print("Comparaison à l'aide de randomPerm")
    tableaux = [[i, [randomPerm(i) for j in range(ech)]] for i in range(2, taille, pas)]
    courbes(algos, tableaux, styleLigne="-")
    affiche("Comparaison à l'aide de randomPerm")
    print()

    print("Comparaison à l'aide de randomTab")
    tableaux = [
        [i, [randomTab(i, 0, 1000000) for j in range(ech)]]
        for i in range(2, taille, pas)
    ]
    courbes(algos, tableaux, styleLigne="-")
    affiche("Comparaison à l'aide de randomTab")
    print()

    print("Comparaison à l'aide de derangeUnPeu (rev = True)")
    tableaux = [
        [i, [derangeUnPeu(i, 10, True) for j in range(ech)]]
        for i in range(2, taille, pas)
    ]
    courbes(algos, tableaux, styleLigne="-")
    affiche("Comparaison à l'aide de derangeUnPeu (rev = True)")
    print()

    print("Comparaison à l'aide de derangeUnPeu (rev = False)")
    tableaux = [
        [i, [derangeUnPeu(i, 10, False) for j in range(ech)]]
        for i in range(2, taille, pas)
    ]
    courbes(algos, tableaux, styleLigne="-")
    affiche("Comparaison à l'aide de derangeUnPeu (rev = False)")
    print()


def compareAlgosSurTableauxTries(algos, taille=20000, pas=1000, ech=10):
    print("Comparaison à l'aide de derangeUnPeu (rev = False)")
    tableaux = [
        [i, [derangeUnPeu(i, 10, False) for j in range(ech)]]
        for i in range(2, taille, pas)
    ]
    courbes(algos, tableaux, styleLigne="-")
    affiche("Comparaison à l'aide de derangeUnPeu (rev = False)")


##############################################################
#
# Main
#

if __name__ == "__main__":
    trisInsertion = [triInsertionEchange, triInsertionRotation, triInsertionRapide]
    trisLents = [triSelection, triBulles]

    sys.setrecursionlimit(4000)

    # Question 1.6

    print("Exercice 1")
    algos = [triSelection]
    # compareAlgos(algos)

    # Question 2.4

    print("Exercice 2")
    algos += trisInsertion + [triFusion, triBulles]
    # compareAlgos(algos)

    ###################################################################
    ##### Commentez ici les résultats obtenus pour les différents #####
    ##### algorithmes sur les différents types de tableaux ############
    ###################################################################
    # Dans un premier moment on observe que parmi les tris par insertion
    # le tri par insertion rapide est le plus rapide. POar contre la
    # différence entre le tri par insertion rapide et le tri par selection
    # devient évidente quand on a  un tableau presque trié (derange un peu).
    # Dans ce cas, le tri par insertion performe de la meme manière que quand
    # le tableau n'est pas trié. Par contre le tri par selection est beaucoup
    # plus rapide. On en déduit que le tri par insertion est plus rapide que
    # le tri par selection en moyenne.
    #
    # Une fois introduits le tri a bulles et le tri par fusion, on observe
    # qu'ils font la différence. Le tri a bulles est clairement le pire, il
    # performe de la même manière dans toutes les situations et d'un manière
    # beaucoup plus lente que les autres. Le tri par fusion est le plus rapide
    # et il est constant aussi dans toutes les situations.
    ###################################################################

    # Question 3.3

    print("Exercice 3")
    algos = [triShell]
    # compareAlgos(algos)

    # Question 3.4

    print("Comparaisons de tous les algos")
    algos = trisInsertion + trisLents + [triFusion, triShell]
    # compareAlgos(algos, taille=2000, pas=200)

    ###################################################################
    ##### Commentez ici les résultats obtenus pour les différents #####
    ##### algorithmes sur les différents types de tableaux ############
    ###################################################################
    # On observe que le tri Shell est une amélioration importante du tri
    # par insertion. Il bat tous les autres tris par insertion et il est
    # très proche du tri par fusion (au moins a cette échelle).
    ###################################################################

    # compare les tris fusions et Shell

    print("Comparaisons des tris fusion et Shell")
    algos = [triFusion, triShell]
    # compareAlgos(algos, taille=10000, pas=500)

    ###################################################################
    ##### Commentez ici les résultats obtenus pour les différents #####
    ##### algorithmes sur les différents types de tableaux ############
    ###################################################################
    # On observe que le tri par fusion est plus rapide que le tri Shell
    # dans tous les cas, sauf dans les tableaux presque tries. Dans cette
    # situation ils sont plus ou moins égaux.
    ###################################################################

    # comparaison sur tableaux presque triés

    print("\nComparaisons sur tableaux presque triés")
    algos = trisInsertion + [triFusion, triShell]
    compareAlgosSurTableauxTries(algos)

    ###################################################################
    ##### Commentez ici les résultats obtenus pour les différents #####
    ##### algorithmes sur les différents types de tableaux ############
    ###################################################################
    # On observe que dans le cas des tableaux presque triés, le tri par
    # insertion domine. Le tri par fusion est le plus rapide dans toutes
    # les situations sauf quand le tableau est presque trié. Dans ce
    # cas, le tri shell est plus rapide.
    ###################################################################
