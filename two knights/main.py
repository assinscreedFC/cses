def knights(n, valeur):
    g = 0
    b=1
    for i in range(n):
        for j in range(n):
            cases_menacees = chek(valeur, i, j, n) #nombre de cases menacées par un cavalier à la position (i, j)
            g -= cases_menacees #on enlève le nombre de cases menacées par un cavalier à la position (i, j)
            g+=n*n-b #on addition le nombre totale de case moin celle deja visiter
            b+=1
            

    print(g)


def chek(valeur, i, j, n):
    """
    Vérifie combien de cases sont menacées par un cavalier à la position (i, j).
    """
    val = 0
    for dx, dy in valeur:
        x, y = dx + i, dy + j
        
        if 0 <= x < n and 0 <= y < n: #si la position est dans le tableau
            if x==i and y>j: #on verifie que la case n'est pas deja visiter
                val+=1
            elif x>i:
                val+=1
    return val


def main():
    valeur = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))

    n = int(input())
    for i in range(1, n + 1):
        knights(i, valeur)


main()
