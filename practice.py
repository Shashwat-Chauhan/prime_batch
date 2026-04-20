class Node:
    def __init__(self , val):
        self.left = None
        self.right = None
        self.val = val
    

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




def preorder_traversal(root):
    print(root.val)
    if root.left:
        preorder_traversal(root.left)
    if root.right:
        preorder_traversal(root.right)
        
# preorder_traversal(root)


def pre1(root):
    if not root:
        return 

    print(root.val)
    pre1(root.left)
    pre1(root.right)



def post1(root):
    if not root:
        return 
    
    post1(root.left)
    post1(root.right)
    print(root.val)

# post1(root)


def postorder_traversal(root : Node):
    if root.left:
        postorder_traversal(root.left)

    if root.right:
        postorder_traversal(root.right)
    
    print(root.val)

# postorder_traversal(root)


def inorder_traversal(root : Node):

    if root.left:
        inorder_traversal(root.left)
    
    print(root.val)

    if root.right:
        inorder_traversal(root.right)


def inorder1(root):
    if not root:
        return

    inorder1(root.left)
    print(root.val)
    inorder1(root.right)

# inorder_traversal(root)
# inorder1(root)



def max_depth(root : Node):
    if not root:
        return

    if not root.left and not root.right:
        return 1
    
    return max(max_depth(root.left) , max_depth(root.right)) + 1

ans = max_depth(root)
print(ans)
