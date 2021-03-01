#roman numeral to integer

A='CXi'
A=A.upper()

D={'I':1,'V':5,'X':10,'L':50,'C':100}

N=0
i=0
while i<len(A):
    f=0
    if i<len(A)-1:
        if A[i] == 'I' and A[i+1] in ['V','X']:
            N+=D[A[i+1]]-1
            i=i+2
            f=1
        elif A[i] == 'X' and A[i+1] in ['L','C']:
            N+=D[A[i+1]]-10
            i=i+2
            f=1
    if f!=1:
        N+=D[A[i]]
        i=i+1

print(A,'=',N)