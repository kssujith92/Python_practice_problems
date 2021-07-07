def fn(i):
    i=i+1
    return

i=10
fn(i)
print(i)

A='Sujith'
print(A[1])
print(A[::-1])
print(A[::2])

for i in range(1,5): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(sum([i*10**m for m in range(i-1,-1,-1)]))