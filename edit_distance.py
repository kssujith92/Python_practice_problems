#Edit distance between two words
#Operations: Delete, Insert, Replace

def edit_dist(s1,s2,d=0):
    l1,l2=len(s1),len(s2)
    if l2>l1:
        s1,s2=s2,s1
        l1,l2=l2,l1
    if l2==0:
        d+=l1
    elif s1[0]==s2[0]:
        d+=edit_dist(s1[1:],s2[1:],d)
    else:
        d+=min(edit_dist(s1,s2[1:],d),edit_dist(s1[1:],s2,d),edit_dist(s1[1:],s2[1:],d))
        d+=1
    return d
    
    
#str1,str2='Sunday','Saturday'
str1,str2='Kitten','Sitting'
#str1,str2 = 'geek','gesek'
print(edit_dist(str1,str2))

