#Given two sentences, return words that are common and words that are not.

s1 = 'We are really pleased to meet you in our city'
s2 = 'The city was hit by a really heavy storm'

def wordslist(s1,s2):
    C=[]
    M=[]
    S1=s1.split(' ')
    S2=s2.split(' ')
    for w in S1:
        if w in S2:
            C.append(w)
        else:
            M.append(w)
    for w in S2:
        if w not in S1:
            M.append(w)
    return C,M

c,m=wordslist(s1,s2)
print(c)
print(m)
    