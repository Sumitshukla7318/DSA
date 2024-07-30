class PriorityQueue:
    def __init__(self):
        self.items=[]


    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))


    def is_empty(self):
        return len(self.items)==0


    def pop(self):
        if self.is_empty():
            raise IndexError("priority queue is empty")
        else:
            return self.items.pop(0)[0]

    def size(self):
        return len(self.items)





p1=PriorityQueue()
p1.push("sumit",9)
p1.push("tanu",8)
p1.push("priya",7)
p1.push("shivangi",6)
p1.push("vandana",3)
p1.push("divya",4)
p1.push("shalu",8)
#print(p1.size())
while not p1.is_empty():
    print(p1.pop())










    
