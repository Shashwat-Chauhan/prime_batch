class Node:
    def __init__(self , val):
        self.left = None
        self.val = val
        self.right = None

    

def Inorder(root):
    res = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    dfs(root)
    return res


def postOrder(root):
    res = []

    def dfs(node):
        if node is None:
            return
        
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)
    
    dfs(root)
    return res


def preOrder(root):
    res = []

    def dfs(node):
        if node is None:
            return
        
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return res



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


traversal = Inorder(root)
print(traversal)


traversal2 = postOrder(root)
print(traversal2)


traversal3 = preOrder(root)
print(traversal3)