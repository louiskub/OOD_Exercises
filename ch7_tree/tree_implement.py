class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = Tree._insert(self.root, data)
    
    def _insert(root, data):
        if root is None:
            return Node(data)
        
        if data > root.data:
            root.right = Tree._insert(root.right, data)
        elif data <= root.data:
            root.left = Tree._insert(root.left, data)

        return root

    def delete(self, data):
        self.root = Tree._delete(self.root, data)
    
    def get_successor(root):
        cur = root.right
        while cur and cur.left:
            cur = cur.left
        return cur

    def _delete(root, data):
        if root is None:
            return None
        
        if data > root.data:
            root.right = Tree._delete(root.right, data)
        elif data < root.data:
            root.left = Tree._delete(root.left, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                suc = Tree.get_successor(root)
                root.data = suc.data
                root.right = Tree._delete(root.right, suc.data)
        return root


    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
        



tree = Tree()
tree.insert(10)
tree.insert(5)
# tree.insert(3)
# tree.insert(2)
# tree.insert(4)

tree.insert(8)
tree.insert(7)
tree.insert(9)


tree.insert(15)
tree.insert(13)
tree.insert(12)
tree.insert(14)

tree.insert(18)
tree.insert(17)
tree.insert(19)

tree.printTree(tree.root)

print("\n\nNew Tree")
tree.delete(10)
tree.printTree(tree.root)

