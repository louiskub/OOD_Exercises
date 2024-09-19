# พี่โบ๊ทเป็นชาวสวนกำลังจะตัดกิ่งไม้ของ Binary Search Tree ออกมาเป็น ต้นไม้ย่อย ๆ 2 ต้น ก็คือ ต้นไม้ที่ถูกตัดออกมาและต้นไม้ที่เหลือจากการถูกตัด แต่ด้วยความเป็น Perfectionism ของพี่โบ๊ทเอง เขาคันไม้คันมือตัดแต่งต้นไม้ย่อย ๆ ให้เป็น AVL Tree เพื่อให้ต้นไม้ดูสวยงามมากขึ้น

# หมายเหตุ: เนื่องจาก อาทิตย์ที่แล้ว พี่ไม่ได้ออก Binary Search Tree แล้วกลัวน้อง ๆ จะเซ็งที่พี่ไม่ออกโจทย์ พี่เลยยำรวม 2 หัวข้อเป็นข้อเดียวซะเลย :>

# แต่ทั้งนี้เพื่อลดความลำบากของน้อง ๆ พี่เลยใจดีให้ Prototype Code คร่าวๆ ให้ หรือ จะเขียนใหม่ก็ได้ไม่บังคับ



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
    
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return self.root

        cur = self.root
        while True:
            if data > cur.data:
                if cur.right == None:
                    cur.right = Node(data)
                    return cur.right
                else :
                    cur = cur.right
            else:
                if cur.left == None:
                    cur.left = Node(data)
                    return cur.left
                else :
                    cur = cur.left
    def printTree(self):
        BST._printTree(self.root)

    def _printTree(root, indent=0):
        if root is not None:
            BST._printTree(root.right, indent + 1)
            print("    " * indent + str(root.data))
            BST._printTree(root.left, indent + 1)
    def find_node(self, data):
        cur = self.root
        while cur:
            if cur.data == data:
                return cur
            if cur.data < data:
                cur = cur.right
            else :
                cur = cur.left

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
                return AVLTree.rotateLeft(root)
            else:
                root.right = AVLTree.rotateRight(root.right)
                return AVLTree.rotateLeft(root)

        # Left rotate  left > right
        if balace < -1 :
            if data < root.left.data:
                return AVLTree.rotateRight(root)
            else:
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

    def _printTree(root, indent=0):
        if root is not None:
            AVLTree._printTree(root.right, indent + 1)
            print("    " * indent + str(root.data))
            AVLTree._printTree(root.left, indent + 1)

    def dfs(self):
        if not self.root:
            return
        stack = [self.root]
        ans = []
        while stack:
            cur = stack.pop()
            ans.append(cur.data)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return ans
    # def cut_tree(self, data):
    #     self.root = AVLTree._cut_tree(self.root, data)
    
    # def _cut_tree(root, data):
    #     if data == root.data:
    #         return None
    #     elif data < root.data:
    #         root.left = AVLTree._cut_tree(root.left, data)
    #     else:
    #         root.right = AVLTree._cut_tree(root.right, data)
    #     root.setHeight()
    #     return root
    
    def find_node(self, data):
        cur = self.root
        while cur:
            if cur.data == data:
                return cur
            if cur.data < data:
                cur = cur.right
            else :
                cur = cur.left
    # def find_node(self, data):
    #     return AVLTree._find_node(self.root, data)

    # def _find_node(root, data):
    #     if root.data == data:
    #         return root
    #     if data > root.data:
    #         temp = AVLTree.find_node(root.right, data)
    #     else :
    #         temp = AVLTree.find_node(root.right, data)

    #     if not isinstance(temp, list):
    #         temp = [root, temp]
    #     return temp



inp1, inp2 = input(
    "Enter the val of tree and node to cut: "
).split("/")
inp1 = [int(e) for e in inp1.split()]
before = BST()
for i in inp1:
    before.insert(int(i))
print("Before cut:")
before.printTree()


cut_tree = AVLTree()
cut_tree.root = before.find_node(int(inp2))
big = inp1
small = cut_tree.dfs()
print("hello = ",cut_tree.root.balanceValue())
if cut_tree.root.balanceValue() > 1 or cut_tree.root.balanceValue() < -1:
    print("Case1")
    cut_tree = AVLTree()
    for i in small:
        cut_tree.add(i)
print("Cutted Tree:")
cut_tree.printTree()

print("Left Tree:")

cut = list(set(big) - set(small))

new_tree = AVLTree()
for i in cut:
    new_tree.add(int(i))
new_tree.printTree()