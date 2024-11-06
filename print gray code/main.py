
def main():
    n=input("entrer la puissance de 2^n a evaluer")
    n=int(n)
    
    for i in range(2**n): 
        dec=i
        dec=dec<<1
        dec=dec^i
        dec=dec>>1
        
        print(bin(dec))
        
        
       
    
    
    

        

main()
