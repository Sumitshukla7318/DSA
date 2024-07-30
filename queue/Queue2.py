class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0

    def is_empty(self):
        return self.count==0
        #return self.front==None

    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.count+=1


    def dequeue(self):
        if self.is_empty():
            raise IndexError("empty Queue")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
        self.count-=1

    def get_front(self):
        if self.is_empty():
            raise IndexError("no data in the queue")
        else:
            return self.front.data
            

    def get_rear(self):
        if self.is_empty():
            raise IndexError("No data in the queue")
        else:
            return self.rear.data


    def size(self):
        return self.count



q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
print(q1.size())

            



        
