#Find the average length of words in a given sentence.

s1 = "Hello World was my first ever output...Many programmers, including me, started with this."
s2 = "I would like to be a data scientist! I am working on improving my python skills..."


def awl(s):
    for p in '.,!?;:':
        s=s.replace(p,' ')
    W=s.split()
    t=0
    a=round(sum(len(w) for w in W)/len(W),2)
    return a

print(awl(s1),awl(s2))
    