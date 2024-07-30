class Node:
    def __init__(self,data=None,pre=None,next=None):
        self.pre=pre
        self.data=data
        self.next=next
class Dequeue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.count=0

    def is_empty(self):
        return self.front==None

    def insert_front(self,data):
        n=Node(data,None,self.front)
        if self.is_empty():
            #self.front=n
            self.rear=n
        else:
            self.front.pre=n
        self.front=n
        self.count+=1

    def insret_rear(self,data):
        n=Node(data,self.rear)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.count+=1


    def delete_front(self):
        if self.is_empty():
            raise IndexError("Dequeue is empty")
        elif self.front==self.rear:
            self.front=None
            self.rear=None

        else:
            self.front=self.front.next
            self.front.pre=None
        self.count-=1

    def delete_rear(self):
        if seslf.is_empty():
            raise IndexError("dequeue is empty")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        
        else:
            self.rear=self.rear.pre
            self.rear.next=None
        self.count-=1

    def get_front(self):
        if not self.is_empty():
            return self.front.data
        else:
            raise IndexError("dequeue is empty")

    def get_rear(self):
        if not self.is_empty():
            return self.rear.data
        else:
            raise IndexError("dequeue is empty")

    def size(self):
        return sef.count









            
     








    






            






            







        
           




        
            
