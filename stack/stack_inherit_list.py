class stack(list):
    def is_empty(self):
        return len(self)==0

    def push(self,data):
        self.append(data)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("stack is empty")

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("stack is empty")

    def size(self):
        return len(self)

    def insert(self,index,data):
        raise AttributeError("No attribute insert in stack")
        


s1=stack()




