#include<stdlib.h>
#include<stdio.h>
typedef enum bool{FALSE,TRUE}bool;
int main (){
    bool trouve=TRUE;
    unsigned long int n;
    unsigned long int *tab;
    unsigned long int count=0;
    scanf("%ld",&n);
    tab = (unsigned long int*)malloc(n*sizeof(unsigned long int));
     for(unsigned long int i=0;i<n;i++)
        {
            scanf("%ld",&tab[i]);
        }
    
    while (trouve==TRUE && n>1)
    {   
        
        trouve=FALSE;
        for(unsigned long int i=0;i<(n-1);i++)
        {
            if(tab[i]>tab[i+1])
            {   
                trouve=TRUE;
                count+=tab[i]-tab[i+1];
                tab[i+1]+=tab[i]-tab[i+1];
                
                
            }
        }
    }
    printf("%ld",count);
    

    
}