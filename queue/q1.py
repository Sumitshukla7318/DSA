class q:
    def __init__(self):
        self.myq=[]

    def insert(self,data):
        
            self.myq.insert(0,data)
            #print(self.myq)

    def delete(self):
        self.myq.pop()

    def print_list(self):
        print(self.myq)
        #print(len(self.myq))

q1=q()
q1.insert(10)
q1.insert(20)
q1.insert(30)
q1.insert(40)
q1.print_list()
q1.delete()
q1.print_list()
        
