# ให้น้องๆรับ input เป็น list และ k โดยให้สร้าง Binary Search Tree จาก list ที่รับมา และหลังจากนั้นให้ทำการดูว่าใน Tree มีค่าไหนที่มากกว่าค่า k หรือไม่ ถ้ามีให้ทำการคูณ 3 เพิ่มเข้าไป


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

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
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def dfs(self, node, data):
        if node.left:
            self.dfs(node.left, data)
        if node.data > data:
            node.data = node.data*3
        if node.right:
            self.dfs(node.right, data)


T = BST()
inp, num = input('Enter Input : ').split('/')
inp = [int(i) for i in inp.split()]
num = int(num)

root = T.insert(inp[0])
for i in range(1, len(inp)):
    T.insert(inp[i])
T.printTree(root)
print("--------------------------------------------------")
T.dfs(T.root, num)
T.printTree(root)