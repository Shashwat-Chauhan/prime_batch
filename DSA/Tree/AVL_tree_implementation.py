class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    # ---------- Utility Functions ----------
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

    # ---------- Rotations ----------
    def right_rotate(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        self.update_height(y)
        self.update_height(x)

        return x

    def left_rotate(self, root):
        child = root.right
        childLeft = child.left

        child.left = root
        root.right = childLeft

        self.update_height(root)
        self.update_height(child)

        return child

    # ---------- Insertion ----------
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node  # no duplicates

        self.update_height(node)
        balance = self.get_balance(node)

        # Left Left
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Right Right
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Left Right
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    # ---------- Deletion ----------
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # one child / no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # two children
            temp = self.get_min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        self.update_height(node)
        balance = self.get_balance(node)

        # Left Left
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        # Left Right
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Right
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        # Right Left
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # ---------- Search ----------
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node or node.key == key:
            return node

        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # ---------- Traversals ----------
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


# Example Usage
if __name__ == "__main__":
    avl = AVLTree()

    for val in [10, 20, 30, 40, 50, 25]:
        avl.insert(val)

    print("Inorder after insertion:", avl.inorder())

    avl.delete(30)
    print("Inorder after deletion:", avl.inorder())

    found = avl.search(25)
    print("Found 25:", found is not None)