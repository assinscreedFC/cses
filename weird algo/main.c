#include<stdlib.h>
#include<stdio.h>

int main (){
    unsigned long int n;
    scanf("%ld",&n);
    while (n!=1)
    {   
        printf("%ld ",n);
        if(n%2==0)
        {
            n=n/2;
        }
        else
        {
            n=3*n+1;
        }

    }
    printf("%ld ",n);
}