
from itertools import permutations
def main():
    mot=input()
    # Obtenir seulement les permutations uniques
    permutations_uniques = sorted(set(permutations(mot)))
    print(len(permutations_uniques))
    # Convertir chaque tuple en chaîne
    for perm in permutations_uniques:
        print(''.join(perm))
main()