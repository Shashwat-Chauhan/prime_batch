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
root.left.left.left = Node(9)

def max_depth(node):
    if not node:
        return 0
    
    maxi = 0

    left_sum = max_depth(node.left)
    right_sum = max_depth(node.right)
    maxi = max(maxi , left_sum , right_sum)

    return 1 + max(left_sum , right_sum)

max_depth_of_tree = max_depth(root)
print(max_depth_of_tree)
