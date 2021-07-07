#check whether a given array is monotonic.

A = [6, 5, 4, 4] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

def check_mon(A):
    f=3  
    for i in range(0,len(A)-1):
        if f==3:
            if A[i]<A[i+1]:
                f=1
            elif A[i]>A[i+1]:
                f=2
        elif f==1 and A[i]>A[i+1]:
            f=0
        elif f==2 and A[i]<A[i+1]:
            f=0
    if f==0:
        return 'Non monotonic'
    else:
        return 'Monotonic'


print(check_mon(B))