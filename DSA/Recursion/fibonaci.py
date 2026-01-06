class Node:
    def __init__(self , val):
        self.left = None
        self.val = val
        self.right = None
    


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

def levelOrderTraversal(root):
    if not root:
        return []

    queue = [root]
    res = []

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
        
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
            
        res.append(level)
    
    return res

ans = levelOrderTraversal(root)
print(ans)