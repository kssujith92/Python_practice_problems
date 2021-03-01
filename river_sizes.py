#count the lenght of river (continous ones)
import numpy as np

def ip_travel(A,i,j,c,Rin):
    f=0
    l,b=A.shape
    print('Starting ip_travel')
    if i*l+j not in Rin:
        Rin.append(i*l+j)
        c=c+1
    while f==0 and i<l-1:
                i=i+1
                if A[i,j]==1:
                    Rin.append(i*l+j)
                    c=c+1
                else:
                    f=1
                    i=i-1
    if j>0:
        if A[i,j-1]==1:
            c,Rin=jm_travel(A,i,j-1,c,Rin)
    if j<b-1:
        if A[i,j+1]==1:
            c,Rin=jp_travel(A,i,j+1,c,Rin)
    print('ip_travel done: c=',c)
    return (c,Rin)

def im_travel(A,i,j,c,Rin):
    f=0
    l,b=A.shape
    print('Starting im_travel')
    if i*l+j not in Rin:
        print(i*l+j,Rin)
        Rin.append(i*l+j)
        c=c+1
    while f==0 and i>0:
                i=i-1
                if A[i,j]==1:
                    Rin.append(i*l+j)
                    c=c+1
                else:
                    f=1
                    i=i+1
    if j>0:
        if A[i,j-1]==1:
            c,Rin=jm_travel(A,i,j-1,c,Rin)
    if j<b-1:
        if A[i,j+1]==1:
            c,Rin=jp_travel(A,i,j+1,c,Rin)
    print('im_travel done: c=',c)
    return (c,Rin)

def jm_travel(A,i,j,c,Rin):
    f=0
    l,b=A.shape
    print('Starting jm_travel')
    if i*l+j not in Rin:
        Rin.append(i*l+j)
        c=c+1
    while f==0 and j>0:
                j=j-1
                if A[i,j]==1:
                    Rin.append(i*l+j)
                    c=c+1
                else:
                    f=1
                    j=j+1
    if i>0:
        if A[i-1,j]==1:
            c,Rin=im_travel(A,i-1,j,c,Rin)
    if i<l-1:
        if A[i+1,j]==1:
            c,Rin=ip_travel(A,i+1,j,c,Rin)
    print('jm_travel done: c=',c)
    return (c,Rin)

def jp_travel(A,i,j,c,Rin):
    f=0
    l,b=A.shape
    print('Starting jp_travel')
    if i*l+j not in Rin:
        Rin.append(i*l+j)
        c=c+1
    while f==0 and j<b-1:
                j=j+1
                if A[i,j]==1:
                    Rin.append(i*l+j)
                    c=c+1
                else:
                    f=1
                    j=j-1
    if i>0:
        if A[i-1,j]==1:
            c,Rin=im_travel(A,i-1,j,c,Rin)
    if i<l-1:
        if A[i+1,j]==1:
            c,Rin=ip_travel(A,i+1,j,c,Rin)
    print('jp_travel done: c=',c)
    return (c,Rin)


A=np.random.randint(2,size=(6,5))
#A=np.array([[1,1,0,0,1],[1,0,1,0,1],[1,0,1,0,1],[0,1,1,0,0],[1,0,0,1,1]])
print(A)
l,b=A.shape
Rin=[]
C=[]

for i in range(0,l):
    for j in range(0,b):
        if A[i,j]==1 and i*l+j not in Rin:
            c=0
            print('\nNew river discovered at',[i,j])
            c,Rin=ip_travel(A, i, j, c, Rin)
            c,Rin=im_travel(A, i, j, c, Rin)
            C.append(c)
            print('Length counted to be',c)
print(Rin)           
print(C)
                    