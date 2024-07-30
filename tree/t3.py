class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

root=Node(50)
root.left=Node(30)
root.right=Node(80)
root.left.left=Node(10)
root.left.right=Node(40)
root.right=Node(80)
root.right.left=Node(70)
root.right.right=Node(100)



current=root
stk=[]
#inorder
while stk or current:
    if current is not None:
        stk.append(current)
        current=current.left
    else:
        current=stk.pop()
        print(current.data,end=',')
        current=current.right
    



current=root
stk=[]
#postorder
while stk or current:
    if current is not None:
        current=current.left
        stk.append(current)

    else:
        current=stk.pop()
        print(current.data)
        current=current.right
    






        
        
