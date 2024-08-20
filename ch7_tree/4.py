# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

# โดยมีการป้อน input ดังนี้

# i <int> = insert data

# d <int> = delete data

# หมายเหตุ การลบนั้นจะใช้หลักการของ Inorder Successor และ จำนวน parameter มีได้มากสุด 3 ตัว


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
    
    def delete_node(self, parent: Node, child: Node):
        if parent.left == child:
            parent.left = None
        elif parent.right == child:
            parent.right = None

    
    def delete(self, root, data):
        if root is None:
            print("Error! Not Found DATA")
            return
        
        if root.data > data:
            root.left = self.delete(root.left, data)
        elif root.data < data:
            root.right = self.delete(root.right, data)
        else :
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            cur = root.right
            while cur.left is not None:
                cur = cur.left
            root.data = cur.data
            root.right = self.delete(root.right, cur.data)
        return root  
        
        
        
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)



T = BST()
inp= [[j for j in k.split()] for k in input('Enter Input : ').split(',')]
i=0
for k in inp:
    # print("\ni = ", i)
    # i+=1
    if k[0] == 'i':
        print(f"insert {k[1]}")
        T.insert(int(k[1]))
        T.printTree(T.root)
    elif k[0] == 'd' :
        print(f"delete {k[1]}")
        T.root = T.delete(T.root, int(k[1]))
        T.printTree(T.root)
    