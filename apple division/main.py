from itertools import combinations
#utilistation de combination pour genere tout les sous-ensemble possible d'un tableau
#utilsiation de la formule  somme_totale - 2 * somme_sous_ensemble pour trouver la difference minimale entre deux sous-ensemble
# s1-s2 -> s1-(somme-s1) -> 2s1-somme ou somme-2s1
#s2=somme-s1
def main():
    n = int(input())
    nh = input()
    tab = [int(nombre) for nombre in nh.split()]
    
    tab = sorted(tab)
    
    somme_totale = sum(tab)
    
    difference_minimale = somme_totale

    for r in range(1, n):  
        for sous_ensemble in combinations(tab, r):
            somme_sous_ensemble = sum(sous_ensemble)
            difference = abs(somme_totale - 2 * somme_sous_ensemble)
            difference_minimale = min(difference_minimale, difference)

    print( difference_minimale)

main()
