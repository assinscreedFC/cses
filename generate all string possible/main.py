
def fact(n):
    somme=1
    for i in range(1,n):
        somme=i*somme
    return somme
def switch_case(mot,i,j):
    mot=list(mot)
    temp=mot[i]
    mot[i]=mot[j]
    mot[j]=temp
    mot=''.join(mot)
    return mot


def main():
    # n=input()
    # n=int(n)
    # n=fact(n)
    # print(n)
    x=20
    mot="aaabc"
    
    for k in range(x):

        print(mot)
        for i in range (3,0,-1):
            for j in range(i+1,3):
                mot=switch_case(mot,j+1,j)
                print(mot)
            
        mot=switch_case(mot,0,4)
           
        # if(j+1>4):
        #     i-=1
        #     j=i+1
        #     if(i!=0):
        #         mot=switch_case(mot,j+1,j)
        # else:
        #     if(i!=0):
        #         mot=switch_case(mot,j+1,j)
        #     j+=1
        # if (i<0): 
        #     i=4
        #     mot=switch_case(mot,i,j)
        




main()