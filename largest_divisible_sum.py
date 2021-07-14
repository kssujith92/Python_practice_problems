#Given an array of integers and a number k, find the maximum sum which is divisible by k from the given array.

import numpy as np

def max_sum(A,k):
    sum=0
    S=np.array([0])
    if len(A)==0:
        return sum
    else:
        for a in A:
            if a%k==0:
                sum=sum+a
                St=S+a
                S=np.append(S,St)
            else:
                St=S+a
                T=St[St%k==0]
                print(a,S,St,T)
                if len(T)!=0:
                    tmax=max(T)
                    sum=max(sum,tmax)
                S=np.array(list(set(np.append(S,St))))
            print(a,sum)
        return sum

#A,k= [43, 1, 17, 26, 15],16
#A,k = [3, 6, 5, 1, 8],3
A,k = [1,2,3,4,4],3
print(max_sum(A,k))