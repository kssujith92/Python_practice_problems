#Binary search
import math

A=[16,1,12,32,1,45,54,6,17,11,4,16,12,7,19,3,13,2,14,0,15,5,-1,18,20]
A.sort()
x=54
In=0
f=0
A1=A.copy()
print(A)

l=len(A)
while (l>=0):
    m=(l//2)
    am=A[m]
    if am==x:
        f=1
        while A[m]==x and m>0:
            m=m-1
        In=In+m+1
        l=-1
    elif am>x:
        A=A[:m]
        l=m
    elif am<x:
        A=A[m:]
        In+=m
        l=m
    print(am,m,In)

if f!=-0:
    print(In)
else:
    print('Not found')
print(A1.index(x))
