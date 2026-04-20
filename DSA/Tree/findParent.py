class Node:
    def __init__(self , val):
        self.val = val
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
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)




def findParent(root : Node , target : int , parent : int):

    if not root : 
        return -1
    
    if root.val == target:
        return parent
    
    left_search = findParent(root.left , target , root.val)

    if left_search != -1:
        return left_search
    
    return findParent(root.right ,target , root.val)


# Find the parent of 8
ans = findParent(root , 8 , -1)
print(ans)

