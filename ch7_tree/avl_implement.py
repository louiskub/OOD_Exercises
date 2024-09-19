
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = self.set_height()
    
    def __str__(self):
        return str(self.data)

    def get_height(self, node):
        return -1 if node is None else node.height

    def set_height(self):
        left = self.get_height(self.left)
        right = self.get_height(self.right)
        self.height =  1 + max(left, right)
        return self.height

    def balance(self):
        return self.get_height(self.left) - self.get_height(self.right)


class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = AVLTree._insert(self.root, data)
    
    def _insert(root, data):
        if root is None:
            return AVLNode(data)
        
        if data > root.data:
            root.right = AVLTree._insert(root.right, data)
        else:
            root.left = AVLTree._insert(root.left, data)

        root.set_height()
        balance = root.balance()

        # left > right
        if balance > 1:
            # if data < root.left.data:
            if root.left.balance() >= 0:
                return AVLTree.rotateRight(root)
            else :
                root.left = AVLTree.rotateLeft(root.left)
                return AVLTree.rotateRight(root)
            
        # right > left
        if balance < -1:
            # if data > root.right.data:
            if root.right.balance() <= 0:
                return AVLTree.rotateLeft(root)
            else :
                root.right = AVLTree.rotateRight(root.right)
                return AVLTree.rotateLeft(root)

        return root
    
    def delete(self, data):
        self.root = AVLTree._delete(self.root, data)
    
    def _delete(root, data):
        if root is None:
            return root
        
        if data > root.data:
            root.right = AVLTree._delete(root.right, data)
        elif data < root.data:
            root.left = AVLTree._delete(root.left, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            suc = AVLTree.get_successor(root)
            root.data = suc.data
            root.right = AVLTree._delete(root.right, suc.data)
                
        
        if root is None:
            return root
    
        root.set_height()
        balance = root.balance()

        # left > right
        if balance > 1:
            if root.left.balance() >= 0:
                return AVLTree.rotateRight(root)
            else :
                root.left = AVLTree.rotateLeft(root.left)
                return AVLTree.rotateRight(root)
            
        # right > left
        if balance < -1:
            if root.right.balance() <= 0:
                return AVLTree.rotateLeft(root)
            else :
                root.right = AVLTree.rotateRight(root.right)
                return AVLTree.rotateLeft(root)

        return root


    def rotateRight(root):
        y = root.left
        if y is None:
            return root
    
        root.left = y.right
        y.right = root
        root.set_height()
        y.set_height()

        return y

    def rotateLeft(root):
        y = root.right
        if y is None:
            return root
        
        root.right = y.left
        y.left = root
        
        root.set_height()
        y.set_height()
        return y

    def get_successor(root):
        root = root.right
        while root and root.left:
            root = root.left
        return root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)




tree = AVLTree()
tree.insert(15)
tree.insert(13)
tree.insert(12)
tree.insert(14)
tree.insert(8)
tree.insert(18)
tree.insert(17)
tree.insert(19)
tree.insert(7)
tree.insert(9)
tree.insert(10)
tree.insert(5)
tree.insert(3)
tree.insert(2)
tree.insert(4)

tree.printTree(tree.root)

print("\n\nNew Tree")
tree.delete(13)
tree.delete(19)
tree.delete(18)
tree.delete(15)
tree.printTree(tree.root)