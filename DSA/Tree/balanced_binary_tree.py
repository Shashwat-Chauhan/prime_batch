class Node:
    def __init__(self , value):
        self.value = value
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)



def isBalanaced(root : Node):

    def findH(root : Node):
        if not root :
            return 0 
        
        leftH = findH(root.left)
        rightH = findH(root.right)

        if abs(leftH - rightH) > 1:
            return -1
        
        return max(leftH , rightH) + 1

    
    if findH(root) == -1:
        return False
    
    else:
        return True
    
ans = isBalanaced(root)
print(ans)



     