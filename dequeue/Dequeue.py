class Dequeue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0

    def insert_front(self,data):
        self.items.insert(0,data)

    def insert_rear(self,data):
        self.items.append(data)

    def delete_front(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("empty dequeue")

    def delete_last(self):
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError("empty dequeue")


    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("empty dequeue")
            

    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("empty dequeue")



    def size(self):
        return len(self.ietms)




d1=Dequeue()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
print(d1.get_front(),d1.get_rear())
#print(d1.get_front())



    



        



        




        
        