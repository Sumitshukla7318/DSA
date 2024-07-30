class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class sll:
    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head==None

    def insert(self,data):
        n=Node(data)
        if self.is_empty():
            self.head=n
        else:
            n.next=self.head
            self.head=n

    def display(self):
        
        temp=self.head
        while temp.next is not None:
            print(temp.data)
            temp=temp.next
        print(temp.data)

    def reverse(self):
       pre = None
       current = self.head

       while current is not None:
           next_node = current.next
           current.next = pre
           pre = current
           current = next_node

       self.head = pre

def add(s1, s2, s3):
    temp1, temp2 = s1.head, s2.head
    carry = 0

    while temp1 is not None or temp2 is not None:
        t1 = temp1.data if temp1 else 0
        t2 = temp2.data if temp2 else 0

        total = carry + t1 + t2
        s3.insert(total % 10)
        carry = total // 10

        if temp1:
            temp1 = temp1.next
        if temp2:
            temp2 = temp2.next

    if carry > 0:
        s3.insert(carry)

    
s1=sll()
s2=sll()
s3=sll()
s1.insert(1)
s1.insert(2)
s1.insert(3)
s2.insert(4)
s2.insert(5)
s2.insert(6)
add(s1,s2,s3)

s3.display()
