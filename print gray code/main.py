
def main():
    n=input()
    n=int(n)
    

    
    for i in range(2**n): 
        dec=i
        dec=dec<<1
        dec=dec^i
        dec=dec>>1
        
        print(bin(dec)[2:].zfill(n))
        
        
       
    
    
    

        

main()
