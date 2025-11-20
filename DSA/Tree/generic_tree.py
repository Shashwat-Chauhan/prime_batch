from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def level_order_traversal(root):
        if root is None:
            return

        queue = deque()
        queue.append(root)

        while queue:
            current = queue.popleft()
            print(current.data, end=' ')
            
            for child in current.children:
                queue.append(child)

root = TreeNode(10)
for i in range(10):
    node = TreeNode(i)
    root.children.append(node)

root.level_order_traversal()

