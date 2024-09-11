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

    def _gen_display(self) -> 'tuple[list, int, int, int]':
        '''
        return
        - tree image: list[str]
        - left spacing: int
        - value width: int
        - right spacing: int
        '''
        if self is None:
            return [], 0, 0, 0
        lt, lf, lv, lb = Node._gen_display(self.left)
        rt, rf, rv, rb = Node._gen_display(self.right)
        data = str(self.data)
        if not lt and not rt:
            return [data], 0, len(data), 0
        add_left, add_right = int(bool(lt)), int(bool(rt))
        line = ((' '*(lf+lv) + '/' + ' '*(lb)) * add_left +
                ' ' * len(data) +
                (' '*rf + '\\' + ' '*(rv+rb)) * add_right)
        out = [' '*(lf+lv+add_left) + '_'*lb + data +
               '_'*rf + ' '*(rv+rb+add_right), line]
        if len(lt) > len(rt):
            rt.extend([' ' * (rf+rv+rb)] * (len(lt) - len(rt)))
        elif len(lt) < len(rt):
            lt.extend([' ' * (lf+lv+lb)] * (len(rt) - len(lt)))
        for l, r in zip(lt, rt):
            out.append(l + ' '*(len(data)+add_left+add_right) + r)
        return out, (lf+lv+lb+add_left), len(data), (rf+rv+rb+add_right)

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
    
    def printTree(self):
        AVLTree._printTree(self.root)

    def _printTree(node , level=0):
        if not node is None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)



class Tree:
    def __init__(self, root = None):
        self.root = root if root else None

    def add_left(self, data):
        self.root = Tree._add_left(self.root, int(data))
    
    def _add_left(root, data):
        if not root:
            return Node(data)
        root.left = Tree._add_left(root.left, data)
        return root

    def add_right(self, data):
        self.root = Tree._add_right(self.root, int(data))
    
    def _add_right(root, data):
        if not root:
            return Node(data)
        root.right = Tree._add_right(root.right, data)
        return root
        
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
    
    def find_node(self, data):
        cur = self.root
        parent = None
        while cur:
            if cur.data == data:
                return [cur, parent]
            parent = cur
            if cur.data < data:
                cur = cur.right
            else :
                cur = cur.left
        print(f"No {data} in this tree")
        exit

    def merge_tree(self, parent, data, tree):
        if not data:
            return
        if data == self.root.data:
            self.root = tree.root
        elif parent.left.data == data:
            parent.left = tree.root
        elif  parent.right.data == data:
            parent.right = tree.root

    

# def delete_node(parent, Node):
#     if parent

def top_view(tree):
    root = tree.root
    tree_image = root._gen_display()
    print(*tree_image[0], sep='\n')
    print("-" * sum(tree_image[1:]))

def top_view_normal(tree):
    root = tree.root
    tree_image = root._gen_display()
    print(*tree_image[0], sep='\n')


data = input("Enter input: ").split(',')
rotate_node = int(data[0])
rotate_direct = data[1][0]
data = data[2].split()
myTree = AVLTree() 
print("Before")
for e in data:
    root = myTree.add(e)
top_view(myTree)




########################################################################################



tree = Tree()
tree.root = myTree.root

cut_tree = Tree()
cut_tree.root, parent = tree.find_node(rotate_node)
# top_view(cut_tree)
sort = sorted(cut_tree.dfs())
# print(sort)

cut_tree = Tree()
if rotate_direct == "l":
    sort = reversed(sort)
    for i in sort:
        cut_tree.add_left(i)
        # top_view(cut_tree)
else:
    for i in sort:
        cut_tree.add_right(i)
        # top_view(cut_tree)


tree.merge_tree(parent, rotate_node, cut_tree)
print("After")
top_view_normal(tree)



