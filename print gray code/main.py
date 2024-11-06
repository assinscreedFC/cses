
def main():
    n=input("entrer la puissance de 2^n a evaluer")
    n=int(n)
    while(n<1 or n>16):
        print("la puissance doit etre comprise entre 1 et 16")
        n=input("entrer la puissance de 2^n a evaluer")
        n=int(n)
    

    
    for i in range(2**n): 
        dec=i
        dec=dec<<1
        dec=dec^i
        dec=dec>>1
        
        print(bin(dec))
        
        
       
    
    
    

        

main()
