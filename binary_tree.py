from random import randint

def treesum(T):
    print(T)
    T1=[T[0]]
    i=1;k=1;j=0;
    while i<len(T):
        T1.append(T[i])
        i=i+1
        j=j+1
        if j==k:
            j=0
            i=i+k
            k=k*2
    print(T1)
    T2=[T[0]]
    i=2;k=1;j=0;
    while i<len(T):
        T2.append(T[i])
        j=j+1
        i=i+1
        if j==k:
            j=0
            k=k*2
            i=i+k
    print(T2)
    s1=0
    s2=0
    for i in range(0,len(T1)):
        s1=s1+T1[i]*pow(10,len(T1)-i-1)
    for i in range(0,len(T2)):
        s2=s2+T2[i]*pow(10,len(T2)-i-1)
    print([s1,s2])
    return s1+s2



tree=[randint(0,9) for i in range(0,15)]
print(treesum(tree))