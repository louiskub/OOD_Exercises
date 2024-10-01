class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right
        self.height = self.setHeight()

    def __str__(self):
        return str(self.data)

    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a,b)
        return self.height

    def getHeight(self, node):
        return -1 if node == None else node.height

    def balanceValue(self):      
        return self.getHeight(self.right) - self.getHeight(self.left)



class AVLTree:
    def __init__(self, root = None):
        self.root = root if root else None

    def add(self, data):
        self.root = AVLTree._add(self.root, int(data))

    def _add(root, data):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = AVLTree._add(root.left, data)
        else:
            root.right = AVLTree._add(root.right, data)
        root.setHeight()
        balace = root.balanceValue()
        
        # Right rotate   right > left
        if balace > 1 :
            if data > root.right.data:
                print("Left Left Rotation")
                return AVLTree.rotateLeft(root)
            else:
                print("Right Left Rotation")
                root.right = AVLTree.rotateRight(root.right)
                return AVLTree.rotateLeft(root)

        # Left rotate  left > right
        if balace < -1 :
            if data < root.left.data:
                print("Right Right Rotation")
                return AVLTree.rotateRight(root)
            else:
                print("Left Right Rotation")
                root.left = AVLTree.rotateLeft(root.left)
                return AVLTree.rotateRight(root)
        
        return root

    def rotateLeft(x) :
        y = x.right
        if y == None:
            return x
        x.right = y.left
        y.left = x
        x.setHeight()
        y.setHeight()
        return y

    def rotateRight(x) :
        y = x.left
        if y == None:
            return x
        x.left = y.right
        y.right = x
        x.setHeight()
        y.setHeight()
        return y


    def postOrder(self):
        AVLTree._postOrder(self.root)

    def _postOrder(node):
        if not node is None:
            AVLTree._postOrder(node.left)
            AVLTree._postOrder(node.right)
            print(node.data, end=" ")

    def printTree(self):
        AVLTree._printTree(self.root)

    def _printTree(node , level=0):
        if not node is None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)

print(" *** AVL Tree Insert Element ***")
myTree = AVLTree() 
data = input("Enter Input : ").split()
for e in data:
    print("insert :",e)
    root = myTree.add(e)
    myTree.printTree()
    print("====================")

myTree.root = AVLTree.rotateLeft(myTree.root)
myTree.printTree()
print("====================")
myTree.root = AVLTree.rotateRight(myTree.root)
myTree.printTree()

