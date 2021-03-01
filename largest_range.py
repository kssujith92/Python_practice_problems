#find largest range of consecutive integers in an array

A=[16,1,12,32,45,54,6,17,11,4,12,7,19,3,13,2,14,0,15,5,-1,18,20]

amin=min(A)
amax=max(A)

r=0
R=0
E=amin
for i in range(amin,amax):
    if i in A:
        r=r+1
    else:
        r=0
    if r>R:
        R=r
        E=i

print([E+1-R,E])