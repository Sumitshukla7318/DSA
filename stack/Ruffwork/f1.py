class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class cll:
    def __init__(self):
        self.start=None

    def insert(self,data):
        n=Node(data)
        if self.start is None:
            self.start=n
        else:
            n=Node(data,self.start)
            self.start=n

    def back(self,data):
        n=Node(data,None)
        temp=self.start
        if self.start is None:
            self.start=n
        else:
            while temp.next is not None:
                temp=temp.next
            else:
                temp.next=n

    def search(self,data):
        temp=self.start
        while temp.next is not None:
            if temp.item==data:
                 return True
            temp=temp.next
        if temp.item==data:
            return True
        return False
            

    def display(self):
        temp=self.start
        while temp is not None:
            print(temp.item)
            temp=temp.next


s1=cll()
s1.insert(10)
s1.insert(20)
s1.insert(30)
s1.insert(40)
s1.back(50)
print(s1.search(50))
s1.display()






            
