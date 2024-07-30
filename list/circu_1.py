class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class cll:
    def __init__(self,last=None):
        self.last=last

    def insert_at_first(self,data):
        #temp=last
        if self.last is None:
            n=Node(data,None)
            self.last=n
            self.last.next=self.last
        else:
            temp=self.last
            n=Node(data,temp.next)
            temp.next=n
            last=temp.next

    def display(self):
         temp=self.last
         print(temp.data)
         temp=temp.next
         while temp!=self.last:
             print(temp.data)
             temp=temp.next


obj=cll()
obj.insert_at_first(12)
obj.insert_at_first(13)
obj.insert_at_first(13)
#obj.insert_at_first(13)
#obj.insert_at_first(13)
#obj.insert_at_first(13)
obj.display()


