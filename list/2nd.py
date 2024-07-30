'''
class A:
    a=12
    b=23
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(a)
        print(b)
    
obj=A(12,13)
print(obj.a)
print(A.a)
'''

class node:
    def __init__(self,a,b):
        self.item=a
        self.next=b

class sll:
    def __init__(self,start=None):
        self.start=start

    def insert(self,data):
        n=node(data,self.start)
        self.start=n 

    def prin(self):
        temp=self.start
        while temp is not None:
            print(temp.item)
            temp=temp.next

    def  insert_at(self):
        temp=self.start
        while temp is not None:
            temp=temp.next
        temp.next=n
obj=sll()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.insert(40)
obj.prin()
        
        
        
