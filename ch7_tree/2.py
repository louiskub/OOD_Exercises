# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ และหาค่าที่น้อยกว่าค่าที่รับเข้ามาของ Binary Search Tree

# ***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()


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
        ans = ""
        if node.left:
            ans += self.dfs(node.left, data)
        if node.data < data:
            ans += str(node.data) + " "
        if node.right:
            ans += self.dfs(node.right, data)
        return ans


T = BST()
inp, num = input('Enter Input : ').split('|')
inp = [int(i) for i in inp.split()]
num = int(num)

root = T.insert(inp[0])
for i in range(1, len(inp)):
    T.insert(inp[i])
T.printTree(root)
print("--------------------------------------------------")
print(f"Below {num} : ", end="")
ans = T.dfs(T.root, num)
if ans == "":
    print("Not have")
else :
    print(ans)