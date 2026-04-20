class Node:
    def __init__(self, val):
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


def levelorder_traversal(root):
    queue = [root]

    while(queue):
        elem = queue.pop(0)
        print(elem.val)
        if elem.left:
            queue.append(elem.left)
        if elem.right:
            queue.append(elem.right)

levelorder_traversal(root)


    