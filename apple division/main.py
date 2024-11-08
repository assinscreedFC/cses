def moy(tab,n):
    somme=0
    for i in range(n):
        somme+=tab[i]
    for i in range (n):
        tab[i]/=somme
        tab[i]=round(tab[i],2)
    
    return tab
def somme_tab(tab,dep,fin):
    somme=0
    for i in range(dep,fin):
        somme+=tab[i]
    return somme
        



def main():
    n=int(input())
    nh=input()
    tab=[int(nombre) for nombre in nh.split()]
    

    tab=sorted(tab)
    sous_ensemble=[]
    dep=fin=0
    for i in range(n):
        for j in range(i,n): 
            sous_ensemble.append(somme_tab(tab,i,j))
    
    t=len(tab)
    somme=somme_tab(tab,0,t)
    res=somme-sous_ensemble[0]
    for i in range(len(sous_ensemble)):

        if(somme-sous_ensemble[i]<res and i!=8  ):
            res=somme-sous_ensemble[i]

    
    print(somme)
    print(sous_ensemble)
    
    print(res)

main()
