#There are N train stations.
#Find the number of ways in which a train can be made to stop at s of these stations.
#Condition: No two stopping stations are consecutive.

def trainstops(N,s,a,n,c):
    while a<=N-(s-n)*2:
        a=a+2
        n=n+1
        if n<s:
            while a<=N-(s-n)*2:
                c=trainstops(N,s,a,n,c)
                a=a+1
        elif n==s:
            c=c+(N-a)
            break
    return c
            


N=16
s=5

a=-2
n=0
c=0
c=trainstops(N,s,a,n,c)
print('Num of possibilities = ',c)

        