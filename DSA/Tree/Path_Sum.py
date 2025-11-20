# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

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
root.left.left.right = Node(9)


class Solution:
    def hasPathSum(self, root : Node , targetSum: int) -> bool:
        flag = False
        def check(node , target):
            nonlocal flag

            if not node:
                return False
            
            if flag:
                return True
            
            if not node.left and not node.right:
                if target == node.value:
                    flag = True
            
            if node.left:
                check(node.left , target - node.value)
            
            if node.right:
                check(node.right , target - node.value)

            return flag
        
        ans = check(root , targetSum)
        return ans
               
sol = Solution()
target = 3
print("Path with target sum exists:", sol.hasPathSum(root , target))













