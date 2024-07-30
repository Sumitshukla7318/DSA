
class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

root=Node(10)
b1=Node(20)
b2=Node(30)
b3=Node(40)
b4=Node(50)
b5=Node(60)
root.left=b1
root.right=b2
root.left.left=b3
root.left.right=b4
root.right.left=b5

stk=[]
current=root
while stk or current:
    if current is not None:
        stk.append(current)
        current=current.left
    else:
        current=stk.pop()
        print(current.data)
        current=current.right
