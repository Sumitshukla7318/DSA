class Node:
    def __init__(self,data,pre=None,next=None):
        self.pre=pre
        self.item=data
        self.next=next

class dll:
    def __init__(self):
        self.start=None
        self.last=None

    def insert(self,data):
        if self.start is None:
            n=Node(self.start,data,self.start)
            self.start=n
            self.pre=n
        else:
            
            n=Node(self.start,data,self.start)
            self.start=n

    def display(self):
        temp=self.start
        while temp.next is not None:
            print(temp.item)
            temp=temp.next


    def disp(self):
        temp=self.last
        while temp.pre is not None:
            print(temp.item)
            temp=temp.pre
        
obj=dll()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.insert(40)
obj.display()
obj.disp()

            
