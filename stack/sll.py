class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None

    def insert_at_start(self,data):
        n=node(data,self.start)
        self.start=n


    def insert_at_last(self,data):
        n=node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n

    def search(self,data):
         temp=self.start
         while temp is not None:
             if temp.item==data:
                 return temp
             temp=temp.next
         return None

    def insert_after(self,temp,data):
        if temp is not None:
            n=node(data,temp.next)
            temp.next=n

    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.data,end=' ')
            temp=temp.next

    def delete_first(self):
       if self.start is not None:
           self.start=self.start.next

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next==None
    def del_position(self,data):
         if self.start is None:
             pass
         elif self.start.next is None:
            if self.start.data==data:
                self.start=None
         else:
            temp=self.start
            if temp.data==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.data==data:
                        temp.next=temp.next.next
                        break
                temp=temp.next
        





