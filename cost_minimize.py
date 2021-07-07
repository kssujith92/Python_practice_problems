#minimize cost of climbing a ladder.

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

#method 2

def calc_cost(C,m):
    top=len(C)-1
    if m==top-1 or m==top-2:
        c=C[m]
    else:
        c1,c2=calc_cost(C,m+1),calc_cost(C,m+2)
        if c1<c2:
            c=C[m]+c1
        else:
            c=C[m]+c2
    return c

def costmin2(C):
    c1,c2=calc_cost(C,0),calc_cost(C,1)
    if c1>=c2:
        return c2
    else:
        return c1
        
        

cost=[randint(1,10) for i in range(0,10)]
print(costmincalc(cost))
print(costmin2(cost))

