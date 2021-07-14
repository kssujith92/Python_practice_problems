#Huffman encoding

s='Mary had a little lamb'
d={}
for c in s:
    if c in d:
        d[c]+=1
    else:
        d[c]=1

print(d)
ds=sorted(d.items(),key=lambda x:x[1],reverse=True)
