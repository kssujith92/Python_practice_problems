#10 balls randomly put in 12 boxes
#what is the probability that exactly 10 boxes are empty
#monte carlo

import random as rd
import numpy as np

Nballs=10
Nbox=12
Nsim=10000000
C=0

for i in range(Nsim):
    Bx=np.zeros(Nbox)
    for i in range(Nballs):
        Bx[rd.randint(0,Nbox-1)]+=1
    if np.count_nonzero(Bx)==2:
        C=C+1
        
print('Probability = ',C/Nsim)

#while (i<N):
#    Nb=10
#    c=0
#    while (Nb>0):
#        n=rd.randint(0,Nb)
#        Nb=Nb-n
#        c=c+1
#    if c>12:
#        i=i-1
#    elif c==2:
#        C=C+1
#    i=i+1
    
