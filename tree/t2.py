class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

class tree:
    def __init__(self):
        self.stk=[]
        self.root=Node(10)
        self.stk.append(self.root)

    def insert(self,data):
        item=self.stk[-1]
        n=Node(data)
        if item.data>data:
            item.left=n
            self.stk.append(n)
        else:
            item.right=n
            self.stk.append(n)

    def display(self):
        for i in self.stk:
            print(i.data,end=' ')

    def show(self):
        current=self.root
        s=[]
        while current or s:
            if current is not None:
                s.append(current)
                current=current.left
            else:
                current=s.pop()
                print(current.data,end=' ')
                current=current.right
        


t=tree()
t.insert(10)
t.insert(4)
t.insert(20)
t.insert(30)
t.insert(40)
t.insert(5)
t.display()
print()
t.show()






        
        
        
            
        
        
        
    
    
