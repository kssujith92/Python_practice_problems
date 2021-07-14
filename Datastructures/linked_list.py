#single linked-list

class Node:
    def __init__(self,val):
        self.val=val 
        self.next=None
        
class link_list:
    def __init__(self):
        self.head=None
        self.size=0
        
    def push_left(self,newval):
        if self.head==None:
            self.head=Node(newval)
        else:
            h=self.head
            self.head=Node(newval)
            self.head.next=h    
        print('Pushed Left: ',newval)
        self.size+=1
        
    def push_right(self,newval):
        if self.head==None:
            self.head=Node(newval)
        else:
            n=self.head
            while n.next:
                n=n.next
            n.next=Node(newval)
        print('Pushed Right: ',newval)
        self.size+=1
            
    def pop_left(self):
        if self.head==None:
            print('The list is empty')
        else:
            val=self.head.val
            self.head=self.head.next
            print('Popped Left: ',val)
            self.size-=1
            return val
            
    def pop_right(self):
        if self.head==None:
            print('The list is empty')
        else:
            n=self.head
            while n.next:
                p=n
                n=n.next
            p.next=None
            val=n.val
            print('Popped Right: ',val)
            self.size-=1
            return val
        
    def reverse(self):
        if self.head==None:
            print('The list is empty')
        else:
            n=self.head
            p=None
            while n:
                nn=n.next
                n.next=p
                p=n
                n=nn
            self.head=p
        print('List reversed')
    
    def print_list(self):
        if self.head==None:
            print('List is empty')
        else:
            n=self.head
            while n:
                print(n.val)
                n=n.next
                
                

a=[1,2,3,5,4]
s=link_list()
[s.push_left(i) for i in a]
[s.push_right(i) for i in a]
print(s.size)
s.pop_left()
s.pop_left()
s.pop_right()
print(s.size)
s.reverse()
s.print_list()