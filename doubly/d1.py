class node:
    def __init__(self,pre=None,item=None,next=None):
        self.pre=pre
        self.item=item
        self.next=next

class dll:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None

    
    def insert(self,item):
        n=node(None,item,self.start)
        if not self.is_empty():
           self.start.pre=n
        self.start=n
 
    def insert_at_last(self,data):
        temp=self.start
        if self.start!=None:
            while temp.next!=None:
                temp=temp.next
        n=Node(temp,data,None)
        if temp==None:
            self.start=n
        else:
            temp.next=n

    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None 


    def insert_after(self,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.pre=n
            temp.next=n


    def display(self):
        temp=self.start
        while temp is not None:
            print(temp.item)
            temp=temp.next


    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.pre=None


    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.pre.next=None

    def delete_item(self,data):
        if self.start is None:
            pass
            '''elif self.start.next is None:
            if self.start.item==data:
                self.start=None'''
        else:
            temp=self.start
            '''if temp.item==data:
                self.start=temp.next
                temp.next.pre=None'''
            #else:
            while temp is not None:
                    if temp.item==data:
                        if temp.next is not None:
                            temp.next.pre=temp.pre
                        if temp.pre is not None:
                            temp.pre.next=temp.next
                        else:
                            self.start=temp.next
                    temp=temp.next
                        


            
print("               1.insert_at_First")
print("               2.insert_at_last")
print("               3.insert_at_position")
print("               4.search..")
print("               5.delete_at_First")
print("               6.delete_at_last")
print("               7.delete_at_position")
print("               8.display...")
print("               9.Exit.........")
ln=dll()
while True:
    print("  _______________________________________")
    ch=int(input("enter your choice :  "))
    print("__________________________________________")

    if ch==1:
        data=int(input("enter element to insert : "))
        ln.insert(data)
        #break
    elif ch==2:
        data=int(input("enter element to insert : "))
        ln.insert_at_last(data)
        #break
    elif ch==3:
        data=int(input("enter element to insert : "))
        ln.insert_after(data)
        #break

    elif ch==4:
        data=int(input("enter element to insert"))
        ln.search(data)
        #break

    elif ch==5:
        ln.delete_first()
        #break

    elif ch==6:
        ln.delete_last()
        #break

    elif ch==7:
        ln.delete_item()
        #break
    elif ch==8:
        ln.display()
        #break
    elif ch==9:
        break
    else:
        print("!!!enter a valid choice")



        


    
        
        





        
        
        
