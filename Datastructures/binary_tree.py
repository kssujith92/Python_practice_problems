#Binary tree

class Node:
    def __init__(self,val):
        self.val=val 
        self.left=None 
        self.right=None 
        
class Tree:
    def __init__(self):
        self.root=None
        self.depth=0
    
    def insert(self,newval):
        if not self.root:
            self.root=Node(newval)
        else:
            l,j,f=self.depth,0,0
            while f==0:
                f=self.add_element(newval,l,j)
                j+=1
                if j>=2**l:
                    l=l+1
                    j=0
                    self.depth+=1
        
    def add_element(self,newval,l,j):
        n=self.root
        while l>1:
            if j<2**l//2:
                n=n.left
            else:
                n=n.right
            j=l%2
            l-=1
        if not n.left:
            n.left=Node(newval)
            f=1
        elif not n.right:
            n.right=Node(newval)
            f=1
        else:
            f=0
        return f
    
    def print_tree(self):
        if self.root==None:
            print('The tree is empty')
        else:
            print(self.root.val)
            print('Level 0')
            l,j,f=0,0,0
            while f==0:
                f=self.print_elements(l,j)
                j+=1
                if j>=2**l:
                    print('Level ',l+1)
                    l=l+1
                    j=0
                    self.depth+=1
                    
    def print_elements(self,l,j):
        n=self.root
        f=0
        while l>0:
            if j<2**l//2:
                n=n.left
            else:
                n=n.right
            j=l%2
            l-=1
        if n.left:
            print(n.left.val)
        else: 
            f=1
        if n.right:
            print(n.right.val)
        else: 
            f=1
        return f
    

a=[1,2,3,5,4,7,5,4,7,8,5,6,2]
t=Tree()
[t.insert(i) for i in a]
t.print_tree()
        
        