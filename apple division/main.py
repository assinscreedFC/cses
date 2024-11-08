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
    dep=fin=0
    for i in range (5):
        somme=somme_tab(tab,dep,fin)
        if(somme<=0.50):
            fin+=1
        else: 
            dep+=1
    
    res=somme_tab(tab,dep,fin)
    res1=somme-res
    res=round(res)
    res1=round(res1)
    print(res1)

main()
