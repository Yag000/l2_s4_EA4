#!/usr/bin/env python3

"""
 A REMPLIR

 2. True if Z is None else False

 3. "sans valeur" if Z is None else "chaine vide" if Z == " " else "autre"

 4. True if x > 0 else False
 	3 -> True
	-5 -> False
	None -> Erreur
	non-défini -> Erreur
 
	None if x is None else True if x > 0 else False
	3 -> True
	-5 -> False
	None -> None
	non-défini -> Erreur

Expression conditionnelle
retourne True si x > 0, False si x <= 0 ou si x vaut None
"""


def expression_5(x):
    return x is not None and x > 0


#
# AJOUTER D'AUTRES TESTS
#  [valeur_x, resultat_attendu]
def testData():
    return [[5, True], [None, False], [-2, False], [-3.4, False], [0, False]]


#
# NE PAS MODIFIER
#
def testExpr(data):
    score = 0
    ldata = len(data)
    for i, dt in enumerate(data):
        print("  test %d/%d : " % (i + 1, ldata), end="")
        x = dt[0]
        refr = dt[1]
        r = expression_5(x)
        if r == refr:
            score += 1
            print("ok")
        else:
            print("ECHEC")
            print("    entree  : %s" % x)
            print("    calcule : %s" % r)
            print("    attendu : %s" % refr)

    print("Score %d/%d" % (score, ldata))


if __name__ == "__main__":
    testExpr(testData())
