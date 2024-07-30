class Node:
    def __init__(self,item=None,pre=None,next=None):
        self.item=item
        self.pre=pre
        self.next=next
class cdll:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None

    def Insert_at_First(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.pre=n
        else:
            n.next=self.start
            n.pre=self.start.pre
            self.start.pre=n

    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
             n.next=n
             n.pre=n
             self.start=n
        else:
              n.next=self.start
              n.pre=self.start.pre
              n.pre.next=n
              self.start.pre=n
                          

    def search(self,data):
        temp=self.start
        if temp==None:
            return None
        if temp.item==data:
            return temp
        else:
            temp=temp.next
        while temp!=self.start:
            if temp.item==data:
                return temp
            temp=temp.next
        return None


    
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data)
            n.next=temp.next
            n.pre=temp
            temp.next.pre=n
            temp.next=n

    def print_list(self):
        temp=self.start
        print(temp.item)
        temp=temp.next
        while temp!=self.start:
            print(temp.item)
            temp=temp.next

    def delete_first(self):
        if self.start is not None:
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.pre.next=self.start.next
                self.start.next.pre=self.start.pre
                self.start=self.start.next


    def delete_last(self):
        if self.start is not None:
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.pre.pre.next=self.start
                self.start.pre=self.start.pre.pre



    def delete_item(self,data):
        if self.start is not None:
            #if self.start.next==self.start:
            #   if self.start.item==data:
             #       self.start=None

            #else:
                temp=self.start
                if temp.item==data:
                    self.delete_first()
                else:
                    temp=temp.next
                    while temp is not self.start:
                        if temp.item==data:
                            temp.next.pre=temp.pre
                            temp.pre.next=temp.next



obj=cdll()
obj.Insert_at_First(10)
obj.print_list()
                
                






    

                
        


              
            


             
            
