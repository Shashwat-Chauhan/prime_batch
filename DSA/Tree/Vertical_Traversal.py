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

def vertical_traversal(root):
    
    nodes = []
    queue = [(0 , 0 , root)]
    
    while(queue):
        col , row , node = queue.pop(0)
        nodes.append((col, row , node.value))

        if node.left:
            queue.append((col - 1 , row + 1 , node.left))
        
        if node.right:
            queue.append((col + 1, row + 1,node.right))
    
    nodes.sort()
    result = []
    col_grp = []
    prev_col = nodes[0][0]
    for col , row , val in nodes:
        if col != prev_col:
            result.append(col_grp)
            col_grp = []
            prev_col = col

        col_grp.append(val)
    
    result.append(col_grp)
       
    return result

print(vertical_traversal(root))


