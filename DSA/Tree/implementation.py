class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()


    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()
    
    
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)
    
    def levelorder_traversal(self):
        queue = []
        queue.append(self)
        while queue:
            node = queue.pop(0)
            print(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
    def iterative_preOrder(self):
        stack = []
        stack.append(self)
        while(stack):
            node = stack.pop()
            print(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def iterative_inorder(self):
        stack = []
        stack.append(self)
        while(stack):
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            print(node.value)
            if node.left:
                stack.append(node.left)
            
    
# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)


# print("Preorder")
# root.preorder_traversal()
# print("\n")

# print("Inorder")
# root.inorder_traversal()
# print("\n")

level_order = root.preorder_traversal()



# print("Postorder")
# root.postorder_traversal()
# print("\n")

# print("Levelorder")
# root.levelorder_traversal()
# print("\n")

# print("iterative preOrder")
# root.iterative_preOrder()
print("\n")

