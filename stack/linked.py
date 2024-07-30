from sll import *
class Stack:
    def __init__(self):
        self.s1=SLL()
        self.count=0

    def is_empty(self):
        return self.s1.is_empty

    def push(self,data):
        self.s1.insert_at_start(data)
        self.count+=1

    def pop(self):
        if not self.is_empty():
            self.s1.delete_first()
            self.count-=1

    def peek(self):
        #if not self.is_empty():
            return self.s1.start.data
        #print(self.s1.start.data)
        

    def size(self):
        return self.count
    

    
    

s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

print(s.peek())
print(s.size())

    
