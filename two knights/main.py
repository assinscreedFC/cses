import numpy as np
import asyncio
def knights(n,valeur):
    g=0
    matrice = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            # Placer un marqueur à la position actuelle
            matrice[i][j] = 1
            
            # Vérifier toutes les positions supérieures à (i, j)
            for k in range(i, n):
                for l in range((j+1) if k == i else 0, n):
                    if chek(matrice, valeur, k, l, n):
                        g += 1  # Compter les positions valides
            matrice[i][j] = 0
    print(g)         
            

def chek(matrice,valeur,i,j,n):
    for (a,b) in valeur:
        (a,b)=(a+i,b+j)
        if 0<=a<n and 0<=b<n:
            if matrice[a][b]==1 :
                return False
    return True
def main():
    
    valeur= ((2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2))
    
    n = int(input())
    for i in range(1, n+1):
        knights(i,valeur)
    # Créer une matrice remplie de zéros
   
main()
