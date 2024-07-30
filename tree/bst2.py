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


    def min_value(self,temp):
        current=temp
        while current.left is not None:
            current=current.left
        return current.item

    def max_value(self,temp):
        current=temp
        while current.right is not None:
            current=current.right
        return current.item

    def delete(self,data):
        self.root=rdelete(self.root,data)


    def rdelete(self,root,data):
        if root is None:
            return root
        if data<root.data:
            root.left=self.rdelete(root.left,data)
        elif data>root.data:
            root.right=self.rdelete(root.right,data)
        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left
            root.item=self.min_value(root.right)
            self.rdelete(root.right,root.item)
            return root

        
        






        
    

b=BST()
b.insert(10)
b.insert(20)
b.insert(5)
b.insert(3)
print(b.search(10))
print(b.postorder())







            


            





        
        









        
