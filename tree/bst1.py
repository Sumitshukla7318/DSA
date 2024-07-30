class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        self.root=self.rinsert(self.root,data)

    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data<root.data:
            root.left=self.rinsert(root.left,data)
        elif data>root.data:
            root.right=self.rinsert(root.right,data)
        return root


    def search(self,data):
        return self.rsearch(self.root,data)

    def rsearch(self,root,data):
        if root is None or root.data==data:
            return root

        if data<root.data:
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)



    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.data)
            self.rinorder(root.right,result)
            



    def prerder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.data)
            self.rinorder(root.left,result)
            self.rinorder(root.right,result)
    


    
    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.data)

b=BST()
b.insert(10)
b.insert(20)
b.insert(5)
b.insert(3)
print(b.search(10))
print(b.postorder())







            


            





        
        









        
