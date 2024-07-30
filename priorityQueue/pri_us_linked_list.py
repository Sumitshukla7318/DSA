class Node:
    def __init__(self,data=None,priority=None,next=None):
        self.data=data
        self.priority=priority
        self.next=next


class pQueue:
    def __init__(self):
        self.start=None
        self.count=0


    def push(self,data,priority):
        n=Node(data,priority)
        if not self.start or priority<self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next and temp.next.priority<=priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.count+=1



    def is_empty(self):
        return self.start==None

    def pop(self):
        if self.is_empty():
            raise IndexError('empty')
        else:
            data=self.start.data
            self.start=self.start.next
        self.count-=1
        
        return data
        #self.count-=1
                
    def size(self):
        return self.count


p=pQueue()
p.push("sumit",3)
p.push("Amit",4)
p.push("Ankit",1)
p.push("Arpit",5)
p.push("aun",7)
#print(p.size())
while not p.is_empty():
    print(p.pop())






                






