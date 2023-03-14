from math import sqrt

def in_circle_check(i,j,r):
    if sqrt(i*i+j*j)<=r:
        return 1;
    else:
        return 0;

N=1000;
for r in range(1,N+1):
    A=0;
    for i in range(-r,r):
        for j in range(-r,r):
            if in_circle_check(i,j,r):
                A+=1;
    p=A/(r*r);
    print('N = ', r,'\t','pi = ',p)

