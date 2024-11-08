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
    
    tabvalence=moy(tab,len(tab))
    sous_ensemble=[]
    dep=fin=0
    for i in range(n):
        for j in range(i,n):
            sous_ensemble.append(somme_tab(tab,i,j))
    somme=somme_tab(tab,0,n)
    res=somme-sous_ensemble[0]
    for i in range(len(sous_ensemble)):
        if(somme-sous_ensemble[i]<res):
            res=somme-sous_ensemble[i]


    
    
    res=round(res)
    print(res)

main()
