#Wires task in Among Us
#Two rows of N boxes each 
#N colors randomly assigned to each box. No two boxes in the same row has same colors.
#What's the probability that the colors in two rows match perfectly.

from random import sample
from math import factorial

N=8

C=[i for i in range(N)]

c=0
T=10**6
for i in range(T):
        C1=sample(population=C, k=N)
        C2=sample(population=C, k=N)
        if C1==C2:
            c+=1

print('1 in ',int(T/c),' chance')
print('Theoretical probability: 1/',factorial(N))