from random import randint

def costmincalc(cost):
    C=cost
    print(C)
    S=[]
    c=0
    i=0
    while i<len(C)-1:
        if C[i]<C[i+1]:
            c=c+C[i]
            S.append(C[i])
            i=i+1    
        else:
            c=c+C[i+1]
            S.append(C[i+1])
            i=i+2
    print(S)
    return c


cost=[randint(1,10) for i in range(0,10)]
print(costmincalc(cost))

