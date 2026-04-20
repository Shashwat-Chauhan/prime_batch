class Node:
    def __init__(self , val):
        self.val = val
        self.left = None
        self.right = None
    

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right.left = Node(13)


def LCA(main_root : Node , n1 : int, n2 : int) -> Node:

    def check(root , n1 , n2):
        if not root:
            return 
        
        if root.val < n1 and root.val <n2:
            return check(root.right , n1 , n2)
        
        if root.val > n1 and root.val > n2:
            return 
            check(root.left , n1 , n2)
        
        return root

    return check(main_root , n1 , n2)


ans = LCA(root , 4 , 7)

print(ans)
print(ans.val)

