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

def boundary_traversal(root):

    def leaf_nodes(root):
        nodes = []
        def dfs(root):
            nonlocal nodes
            if not root.left and not root.right:
                nodes.append(root.value)
            
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        dfs(root)
        return nodes


    
    def left_boundary(root):
        nodes = []
        queue = [root]
        while queue:
            node = queue.pop()
            nodes.append(node.value)
            if node.left:
                queue.append(node.left)
            elif node.right:
                queue.append(node.right)
        nodes.pop()
        return nodes
    
    def right_boundary(root):
        nodes = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            nodes.append(node.value)
            if node.right:
                queue.append(node.right)
            elif node.left:
                queue.append(node.left)
        
        nodes.pop()
        nodes.reverse()
        return nodes

    ans = []

    left_nodes = left_boundary(root)
    right_nodes = right_boundary(root)
    leaf_nodes_val = leaf_nodes(root)

    ans = left_nodes + leaf_nodes_val + right_nodes
    return ans

result = boundary_traversal(root)
print(result)  
