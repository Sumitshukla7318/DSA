class stack:
    def __init__(self):
        self.stk=[]

    def is_empty(self):
        return len(self.stk)==0


    def push(self,data):
        self.stk.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stk.pop()
        else:
            raise IndexError("stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stk[-1]
        else:
            raise IndexError("stack is empty")
    

    def size(self):
        return len(self.stk)
        

obj=stack()
obj.push(10)
obj.push(20)
obj.push(30)
print(obj.pop(),"poped out")
print(obj.pop(),"poped out")
#obj.pop()
#obj.pop()
print(obj.peek())
        
        
        
        
