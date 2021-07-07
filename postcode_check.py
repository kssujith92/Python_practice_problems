#postcode validation
#must be an integer in the range 100000 to 999999
#must not contain more than one alternating digit pair - eg:101 (1 is an alternating digit)

def postcode(p):
    if p<100000 or p>999999:
        return False
    ps=str(p)
    c=0
    for i in range(0,4):
        if ps[i]==ps[i+2]:
            c+=1
    if c<=1:
        return True
    else:
        return False
    
print(postcode(102515))

    