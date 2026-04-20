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


def diameter(root : Node):
    maxi = 0

    def findH(root : Node):
        nonlocal maxi
        if not root :
            return 0 

        leftH = findH(root.left)
        rightH = findH(root.right)

        curr_diameter = leftH + rightH
        maxi = max(maxi , curr_diameter)

        return 1 + max(leftH , rightH)
    print(root.val)     
    findH(root)

    return maxi

print(diameter(root))

