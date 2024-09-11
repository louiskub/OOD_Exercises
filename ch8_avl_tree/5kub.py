class BST:
    class BSTNode:
        def __init__(self, data, left=None, right=None) -> None:
            self.data = data
            self.left = left
            self.right = right

    def __init__(self, root=None) -> None:
        self.root = root if root else None

    def search_subtree(self, root, key):
        if root is None:
            return None
        if key == root.data:
            return root
        elif key < root.data:
            return self.search_subtree(root.left, key)
        else:
            return self.search_subtree(root.right, key)

    def insert(self, root, key):
        return BST._insert(root, key)

    def _insert(root, data):
        if root is None:
            return BST.BSTNode(data)
        if data < root.data:
            root.left = BST._insert(root.left, data)
        else:
            root.right = BST._insert(root.right, data)
        return root

    def delete_subtree(self, root, key):
        if root is None:
            return None
        if root.data == key:
            return None  
        if key < root.data:
            root.left = self.delete_subtree(root.left, key)
        else:
            root.right = self.delete_subtree(root.right, key)
        return root

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent + str(root.data))
            self.printTree90(root.left, indent + 1)


class AVLTree:
    class AVLNode:
        def __init__(self, data, left=None, right=None) -> None:
            self.data = data
            self.left = left
            self.right = right
            self.height = 1  # Initial height is set to 1

    def __init__(self, root=None) -> None:
        self.root = root if root else None

    def insert(self, root, data):
        return self._insert(root, data)

    def _insert(self, root, data):
        if root is None:
            return AVLTree.AVLNode(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Left heavy
        if balance < -1:
            if data < root.left.data:
                return self.right_rotate(root)  # Right Right
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)  # Left Right

        # Right heavy
        if balance > 1:
            if data > root.right.data:
                return self.left_rotate(root)  # Left Left
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)  # Right Left
        return root

    def left_rotate(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def right_rotate(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def get_height(self, root):
        return 0 if root is None else root.height

    def get_balance(self, root):
        return self.get_height(root.right) - self.get_height(root.left)

    def bst_to_avl(self, bst_root):
        sorted_values = self.inorder_traversal(bst_root)
        for val in sorted_values:
            self.root = self.insert(self.root, val)

    def inorder_traversal(self, root):
        if root is None:
            return []
        return (
            self.inorder_traversal(root.left)
            + [root.data]
            + self.inorder_traversal(root.right)
        )

    def printTree90(self, root, indent=0):
        if root is not None:
            self.printTree90(root.right, indent + 1)
            print("    " * indent + str(root.data))
            self.printTree90(root.left, indent + 1)


# Input handling
inp1, inp2 = input("Enter the val of tree and node to cut: ").split("/")
bst = BST()
for i in inp1.split():
    bst.root = bst.insert(bst.root, int(i))

print("Before cut:")
bst.printTree90(bst.root)

avl1, avl2 = AVLTree(), AVLTree()

# Convert the found subtree into an AVL tree
print("Cutted Tree:")
subtree_root = bst.search_subtree(bst.root, int(inp2))
if subtree_root:
    avl1.bst_to_avl(subtree_root)
    avl1.printTree90(avl1.root)

# Convert the remaining BST (after deletion) into an AVL tree
print("Left Tree:")
bst.root = bst.delete_subtree(bst.root, int(inp2))
if bst.root:
    avl2.bst_to_avl(bst.root)
    avl2.printTree90(avl2.root)
