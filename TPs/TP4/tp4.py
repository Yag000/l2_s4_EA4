#!/usr/bin/env python3

import sys

version = sys.version_info
if version.major < 3:
    sys.exit(
        "Python2 n'est PLUS supporté depuis le 1er Janvier 2020, merci d'installer Python3"
    )

import random
from time import perf_counter as clock

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    sys.exit("Le module matplolib est nécessaire pour ce TP.")

############################################################
# Exercice 1.1
#
# Tri rapide avec mémoire auxiliaire et en place
#
def partition(
    T, pivot_updater=lambda T, x, y: ()
):  # les éléments sont supposés distincts
    pivot_updater(T, 0, len(T))
    pivot = T[0]
    number_of_pivots = 0
    gauche = []
    for elt in T:
        if elt == pivot:
            number_of_pivots += 1
        if elt < pivot:
            gauche.append(elt)
    droite = [elt for elt in T if elt > pivot]
    return pivot, gauche, droite, number_of_pivots


def tri_rapide(T):
    if len(T) < 2:
        return T
    pivot, gauche, droite, number_of_pivots = partition(T)
    return tri_rapide(gauche) + [pivot] * number_of_pivots + tri_rapide(droite)


def partition_en_place(T, deb, fin, pivot_updater=lambda T, x, y: ()):
    pivot_updater(T, deb, fin)
    pivot = T[deb]
    gauche, droite = deb + 1, fin - 1

    while gauche <= droite:
        if T[gauche] <= pivot:
            gauche += 1
        elif T[droite] > pivot:
            droite -= 1
        else:
            T[gauche], T[droite] = T[droite], T[gauche]

    T[deb], T[droite] = T[droite], pivot

    return droite


def tri_rapide_en_place(T, deb=0, fin=None):
    if fin is None:
        fin = len(T)
    if deb < fin:
        pivot = partition_en_place(T, deb, fin)
        tri_rapide_en_place(T, deb, pivot)
        tri_rapide_en_place(T, pivot + 1, fin)

    return T


############################################################
# Exercice 1.2
#
# Tri rapide avec mémoire auxiliaire et en place avec pivot
# aléatoire
#


def pivot_aleatoire(T, deb, fin):
    index = random.randint(deb, fin - 1)
    T[deb], T[index] = T[index], T[deb]


def tri_rapide_aleatoire(T):
    if len(T) < 2:
        return T
    pivot, gauche, droite, number_of_pivots = partition(T, pivot_aleatoire)
    return tri_rapide(gauche) + [pivot] * number_of_pivots + tri_rapide(droite)


def tri_rapide_en_place_aleatoire(T, deb=0, fin=None):
    if fin is None:
        fin = len(T)
    if deb < fin:
        pivot = partition_en_place(T, deb, fin, pivot_aleatoire)
        tri_rapide_en_place_aleatoire(T, deb, pivot)
        tri_rapide_en_place_aleatoire(T, pivot + 1, fin)

    return T


############################################################
""" Exercice 1.3: Interprétation des courbes

# A COMPLETER

"""

############################################################
# Exercice 2.1
#
# Tri par insertion (voir TP3)
#


def tri_insertion(T):
    if T == None:
        return T
    for i in range(1, len(T)):
        for j in range(i, 0, -1):
            if T[j - 1] > T[j]:
                T[j - 1], T[j] = T[j], T[j - 1]
            else:
                break
    return T


############################################################
# Exercice 2.2
#
# les tableaux de taille < 15 sont triés par insertion, le
# reste avec l'algo de tri rapide usuel.
#


def tri_rapide_ameliore(T, deb=0, fin=None):
    if fin is None:
        fin = len(T)
    if fin - deb < 15:
        return tri_insertion(T)
    if deb < fin:
        pivot = partition_en_place(T, deb, fin)
        tri_rapide_ameliore(T, deb, pivot)
        tri_rapide_ameliore(T, pivot + 1, fin)

    return T


############################################################
# Exercice 2.3
#
# Tri rapide seulement pour les tableaux de taille >= 15 et
# ne fait rien pour les tableaux de taille < 15
#


def tri_rapide_partiel(T, deb=0, fin=None):
    if fin is None:
        fin = len(T)
    if fin - deb < 15:
        return

    if deb < fin:
        pivot = partition_en_place(T, deb, fin)
        tri_rapide_partiel(T, deb, pivot)
        tri_rapide_partiel(T, pivot + 1, fin)

    return T


############################################################
# Exercice 2.4
#
# Trie par insertion le résultat de tri_rapide_partiel(T).
#
def tri_sedgewick(T):
    T = tri_rapide_partiel(T)
    return tri_insertion(T)


############################################################
""" Exercice 2.5: Interprétation des courbes

# A COMPLETER

"""


############################################################
# Exercice 3.1
#
# Tris drapeau. Attention, les éléments du tableau ne peuvent pas
# avoir d'autres valeurs que 1, 2 ou 3.
#

BLEU, BLANC, ROUGE = 1, 2, 3


def tri_drapeau(T):
    bleu = []
    blanc = []
    rouge = []

    for i in T:
        if i == BLEU:
            bleu.append(i)
        elif i == BLANC:
            blanc.append(i)
        else:
            rouge.append(i)

    return bleu + blanc + rouge


def tri_drapeau_en_place(T):
    bleu = 0
    blanc = 0
    rouge = len(T) - 1

    while blanc <= rouge:
        if T[blanc] == BLEU:
            T[bleu], T[blanc] = T[blanc], T[bleu]
            bleu += 1
            blanc += 1
        elif T[blanc] == BLANC:
            blanc += 1
        else:
            T[blanc], T[rouge] = T[rouge], T[blanc]
            rouge -= 1

    return T


############################################################
# Exercice 3.2
#
# Effectue un tri drapeau par rapport au pivot.
# Les éléments strictements inférieur au pivot ont couleur 1,
# les éléments égaux au pivot ont couleur 2,
# et les éléments supérieur au pivot ont couleur 3.
# Retourne trois tableaux, contenant respectivement les éléments de couleurs 1, 2 et 3.
#


def partition_drapeau(T, pivot):
    # A compléter
    return T, [], []


############################################################
# Exercice 3.2
#
# Tris rapide, pivot drapeau pour amélioration si le tableau en entrée
# est très répété.
#


def tri_rapide_drapeau(T):
    # A compléter
    return T


############################################################
""" Exercice 3.3: Interprétation des courbes

# A COMPLETER

"""

############################################################
# Exercice 3.4
#
# Effectue un tri drapeau EN PLACE par rapport au pivot.
# Les éléments strictements inférieur au pivot ont couleur 1,
# les éléments égaux au pivot ont couleur 2,
# et les éléments supérieur au pivot ont couleur 3.
# Retourne l'indice du premier élement blanc et du premier element rouge dans le tableau.
# (le premier élément bleu étant à la position 0 si il existe, pas besoin de le préciser.)
#


def partition_drapeau_en_place(T, pivot):
    # A compléter
    return 0, 0


############################################################
# Exercice 3.4
#
# Tri rapide en place utilisant un partitionnement drapeau
#


def tri_rapide_drapeau_en_place(T, debut=0, fin=None):
    # A compléter
    return T


##############################################################
#
# Tri Fusion, pour comparaison
#


def fusion(T1, T2):
    i = 0
    j = 0
    res = []
    while i < len(T1) and j < len(T2):
        if T1[i] < T2[j]:
            res.append(T1[i])
            i += 1
        else:
            res.append(T2[j])
            j += 1
    res += T1[i:]
    res += T2[j:]
    return res


def tri_fusion(T, deb=0, fin=None):
    if fin is None:
        fin = len(T)
    if fin - deb <= 1:
        return T[deb:fin]
    m = (fin - deb) // 2
    T1 = tri_fusion(T, deb, deb + m)
    T2 = tri_fusion(T, deb + m, fin)
    return fusion(T1, T2)


##############################################################
#
# Mesure du temps
#


def mesure(algo, T):
    debut = clock()
    algo(T)
    return clock() - debut


def mesure_moyenne(algo, tableaux):
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
        y = [mesure_moyenne(algo, t[1]) for t in tableaux]
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
    plt.ylabel("temps d'execution (sec)")
    plt.legend(loc="upper left")
    plt.title(titre)


def random_perm(n):
    T = list(range(n))
    random.shuffle(T)
    return T


def test_tri(f):
    for i in range(2, 101):
        T = random_perm(i)
        T_sorted = sorted(T)
        T_output = f(T)
        if T_output != T_sorted:
            print("Échec sur :")
            print(T)
            return False
    return True


def random_tab(n, a, b):
    return [random.randint(a, b) for _ in range(n)]


def derange_un_peu(n, k, rev):
    T = [n - i for i in range(n)] if rev else [i + 1 for i in range(n)]
    for i in range(k):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        T[a], T[b] = T[b], T[a]
    return T


def compare_algos(algos):
    for tri in algos:
        if test_tri(tri):
            print(tri.__name__ + ": OK")
        else:
            print(tri.__name__ + ": échoue")
    taille = 1000  # taille maximale des tableaux à trier
    pas = 100  # pas entre les tailles des tableaux à trier
    ech = 5  # taille de l'échantillon pris pour faire la moyenne

    plt.subplot(221)
    print()
    print("Comparaison à l'aide de random_perm")
    tableaux = [
        [i, [random_perm(i) for j in range(ech)]] for i in range(2, taille, pas)
    ]
    courbes(algos, tableaux, styleLigne="-")
    affiche("Comparaison à l'aide de random_perm")

    plt.subplot(222)
    print()
    print("Comparaison à l'aide de random_tab")
    tableaux = [
        [i, [random_tab(i, 0, 1000000) for j in range(ech)]]
        for i in range(2, taille, pas)
    ]
    courbes(algos, tableaux, styleLigne="-")
    affiche("Comparaison à l'aide de random_tab")

    plt.subplot(223)
    print()
    print("Comparaison à l'aide de derange_un_peu (rev = False)")
    tableaux = [
        [i, [derange_un_peu(i, 20, False) for j in range(ech)]]
        for i in range(2, taille, pas)
    ]
    courbes(algos, tableaux, styleLigne="-")
    affiche("Comparaison à l'aide de derange_un_peu (rev = False)")

    plt.subplot(224)
    print()
    print("Comparaison à l'aide de derange_un_peu (rev = True)")
    tableaux = [
        [i, [derange_un_peu(i, 20, True) for j in range(ech)]]
        for i in range(2, taille, pas)
    ]
    courbes(algos, tableaux, styleLigne="-")
    affiche("Comparaison à l'aide de derange_un_peu (rev = True)")

    plt.show()


def test_tri_non_perm(tri, maxVal=3):
    for size in range(2, 101):
        T = random_tab(size, 1, maxVal)
        T2 = tri(T)
        for i in range(1, len(T2)):
            if T2[i - 1] > T2[i]:
                return False
    return True


def compare_tableaux_repetes(algos, taille=20000, pas=1000, ech=15, maxVal=3):
    for tri in algos:
        if test_tri_non_perm(tri):
            print(tri.__name__ + ": OK")
        else:
            print(tri.__name__ + ": échoue")

    print("Comparaison à l'aide de random_tab")
    tableaux = [
        [i, [random_tab(i, 1, 3) for j in range(ech)]] for i in range(2, taille, pas)
    ]
    courbes(algos, tableaux, styleLigne="-")
    affiche("Comparaison à l'aide de random_tab")
    plt.show()


##############################################################
#
# Main
#

if __name__ == "__main__":

    T = [
        324,
        654,
        23,
        412,
        31243,
        345456,
        23313123,
        5445645,
        34,
        112,
        34,
        5,
        5,
        6,
        6,
        6,
        7,
        7,
        5,
        4523,
    ]
    print(T)
    print(tri_rapide(T))
    print(tri_rapide_en_place(T))
    print(tri_rapide_aleatoire(T))
    print(tri_rapide_en_place_aleatoire(T))
    # trisRapides = [
    #     tri_insertion,
    #     tri_fusion,
    #     tri_rapide,
    #     tri_rapide_en_place,
    #     tri_rapide_aleatoire,
    #     tri_rapide_en_place_aleatoire,
    # ]
    # trisHybrides = [tri_rapide_ameliore, tri_sedgewick]
    # trisDrapeaux = [tri_drapeau, tri_drapeau_en_place]
    # trisRapidesDrapeaux = [tri_fusion, tri_rapide_drapeau, tri_rapide_drapeau_en_place]

    # exercice 1

    # print("Exercice 1")
    # algos = trisRapides
    # compare_algos(algos)

    # exercice 2

    # print("Exercice 2")
    # algos = trisHybrides
    # compare_algos(algos)
    # algos = trisRapides + trisHybrides
    # compare_algos(algos)

    # exercice 3

    T = [BLANC, BLEU, ROUGE, BLEU, ROUGE, ROUGE, BLANC, ROUGE, BLEU, BLEU, ROUGE, BLANC]
    print(T)
    print(tri_drapeau(T))
    print(tri_drapeau_en_place(T))

    # print("Exercice 3")
    # # comparaison des tris drapeaux
    # print("Comparaisons sur tableaux très répétés")
    # algos = trisDrapeaux
    # compare_tableaux_repetes(algos, maxVal=3)

    # # comparaison des tris rapide drapeaux
    # print("Comparaisons sur tableaux très répétés")
    # algos = [tri_rapide, tri_rapide_en_place] + trisRapidesDrapeaux
    # compare_tableaux_repetes(algos, taille=1000, pas=100, ech=5, maxVal=5)
