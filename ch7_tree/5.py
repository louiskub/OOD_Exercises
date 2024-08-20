# เมือง A มีการวางผังเมืองคล้ายกับ Binary Search Tree โดยมีเมืองหลวง/ศูนย์กลางคือ root และหัวเมืองอื่นๆคือ node ต่างๆที่ขึ้นตรงกันเป็นทอดๆไปยัง
# ศูนย์กลาง ในข้อนี้นักศึกษาจะได้รับบทเป็นขุนพลแห่งเมือง B เพื่อนำทัพไปบุกเมือง A โดยจะต้องโจมตีตั้งแต่หัวเมืองที่อยู่นอกสุด(เริ่มจากซ้าย-ไป-ขวา) ไปถึงยังศูนย์กลาง และหากเมืองหลวง A ถูกทำลายได้จะถือว่าขุนพลแห่งเมือง B นำทัพชนะในครั้งนี้ได้

# เมือง A:
# รับตัวเลขจาก input เพื่อสร้างกำลังในหัวเมืองต่างๆ ซึ่งจะถือว่าตัวเลขที่รับเข้ามาจะเเทน nodeๆ นึง (ตัวเลขตัวแรกจะถือเป็นกำลังของเมืองหลวง), (กำลังพลจะเป็นตัวเลขจำนวนเต็มเท่านั้น)
# ตัวเลขแต่ละตัวใน BST จะเเทนกำลังทั้งหมดที่เมืองนั้นๆมีต่อมาในตามลำดับ
# เมื่อแต่ละหัวเมืองจะถูกโจมตี พระราชาแห่งเมือง A ได้สั่งให้กำลังทั้งหมดของแต่ละเมืองที่มีเส้นทางไปถึงยังหัวเมืองนั้นๆ ไปรวมกำลังเพื่อช่วยป้องกันหัวเมืองนั้นๆไว้
# หน้าที่ของขุนพลเมือง B:
# รับ input เพื่อที่จะกำนดกำลังพลฝ่ายของตน ซึ่งเนื่องจากพลเมืองที่ร่วมรบนั้นมีจำนวนที่จำกัด ทำให้ขุนพลต้องแบ่งพลเมืองในการต่อสู่ศึกครั้งนี้ อีกทั้งยังไม่สามารถตีเมืองทั้งหมดได้ในรอบเดียว จึงต้องแบ่งเป็นรอบๆในการตีอีกด้วย โดยในการตีแต่ละรอบจะถูกกำหนดตามเงื่อนไขที่ขุนพลสั่ง โดยเงื่อนไขที่ขุนพลสั่งได้จะมีดังนี้ (k = จำนวนพลเมืองที่ต้องมี), (กำลังพลจะเป็นตัวเลขจำนวนเต็มเท่านั้น)
# 1. รวมกำลังพลเมือง ให้มากกว่า k และไปร่วมรบ : M
# 2. รวมกำลังพลเมือง ให้น้อยกว่า k และไปร่วมรบ : L
# 3. รวมกำลังพลเมือง ให้เท่ากับ k และไปร่วมรบ : EQ
# โดยที่ขุนพลไม่สนใจว่ากำลังในแต่หัวเมือง A นั้นมีเท่าไหร่ คิดแค่ว่าส่งไปเป็นเงื่อนไขแบบนี้คงจะชนะ

# การทำลายแต่ละหัวเมือง A:
# หากหัวเมืองที่จะถูกโจมตีรวมกำลังแล้ว ยังแพ้ให้กับเงื่อนไขกองทัพของทัพ B จะถือว่าเมืองนั้นถูกทำลาย และจะต้องแสดงเส้นทางของกำลังพล และผลลัพธ์รวมของหัวเมืองที่ถูกทำลายนั้นทาง output ด้วย และเมื่อตีเมืองใดเมืองนึงสำเร็จจะกองทัพกองนั้นจะรุกตีเมืองอื่นต่อทันที จนกว่าจะเจอเมืองที่กองทัพนั้นสู้ไม่ไหวตามเงื่อนไขที่กำหนดมา
# หากทัพ B ตีไม่ชนะ(ไม่ตรงกับเงื่อนไขของขุนพล B) จะถือว่าตีเมืองนั้นไม่สำเร็จ และจะไม่แสดงอะไรออกมาที่ output
# หากทัพโค่นเมืองหลวง A ได้จะแสดงประโยคว่า “City A has fallen!” และจะจบการรบทันที แม้ว่าขุนพลจะส่งกองทัพมาเพิ่มก็ตาม

# ตัวอย่าง
# Input :
# Enter <Create City A (BST)>/<Create conditions and deploy the army>:
# 100 70 200 34 80 300/L 250,EQ 250,M 250
# อธิบาย input:
# 100 70 200 34 80 300 : นำเลขเหล่านี้ไปสร้างเป็นเมือง A ตามหลักของ Binary Search Tree (100 = root)
# L 250,EQ 250,M 250 : การกำหนดเงื่อนไข(L, EQ, M) พร้อมกับกำลังพลของทัพ B(250, 250, 250 ตามลำดับ)
		
# Output :
# (City A) Before the war:
#        		300
#   	200
#  100
#        		80
#   	70
#        		34
# >> ผลลัพธ์จากการสร้างเมือง A ตามหลัก Binary Search Tree
# --------------------------------------------------
# Removing paths where the sum is less than 250:
# 1) 100->70->34 = 204
# --------------------------------------------------
# (City A) After the war:
#        		300
#   	200
#  100
#        		80
#   	70
# >> ผลลัพธ์จากตีเมือง A ด้วยกำลังพลน้อยกว่า 250 ทำให้เมือง 34 ที่มีกำลังผลรวมได้ 204 แตกไปในที่สุด
# --------------------------------------------------
# Removing paths where the sum is equal to 250:
# 1) 100->70->80 = 250
# --------------------------------------------------
# (City A) After the war:
#        		300
#   	200
#  100
#   	70
# >> ผลลัพธ์จากตีเมือง A ด้วยกำลังพลเท่ากับ 250 ทำให้เมือง 80 ที่มีกำลังผลรวมได้ 250 แตกไปในที่สุด
# --------------------------------------------------
# Removing paths where the sum is greater than 250:
# 1) 100->200->300 = 600
# 2) 100->200 = 300
# --------------------------------------------------
# (City A) After the war:
#  100
#   	70
# >> ผลลัพธ์จากตีเมือง A ด้วยกำลังพลมากกว่า 250 ทำให้เมือง 300 และ 200 ที่มีกำลังผลรวมได้ 600 และ 300 ตามลำดับแตกไปในที่สุด



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
        self.count = 0
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return self.root

        cur = self.root
        while True:
            if data >= cur.data:
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

    def boolean(self, mode, data, sum):
        if mode == 'L':
            return sum < data
        elif mode == 'E':
            return sum == data
        elif mode == 'M':
            return sum > data
        return False
    
    def delete(self, node, parent):
        if node == self.root:
            self.root = None
            
        elif node == parent[-1].left:
            parent[-1].left = None
        elif node == parent[-1].right:
            parent[-1].right = None
    
    def dfs(self, node, parent: list, data, sum, mode):
        if node.left:
            left =  self.dfs(node.left, parent+[node], data, sum+node.data, mode)
            # if left is None:
            #     return
        if node.right:
            right = self.dfs(node.right, parent+[node], data, sum+node.data, mode)
            # if right is None:
            #     return
        if node.left is None and node.right is None:
            if self.boolean(mode, data, sum+node.data):
                self.delete(node, parent)
                self.print_path(parent+[node])
                return 1
    
    def main_dfs(self, data, mode):
        self.count = 1
        self.dfs(self.root, [], data, 0, mode)
        if self.count == 1:
            print("No paths were removed.")
        
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def print_path(self, path: list):
        print(f"{self.count}) {'->'.join([str(e) for e in path])} = {sum([e.data for e in path])}")
        self.count += 1



T = BST()
inp = input('Enter <Create City A (BST)>/<Create conditions and deploy the army>: ').split('/')
for k in inp[0].split():
    T.insert(int(k))
print("(City A) Before the war:")
T.printTree(T.root)
temp = inp[1].split(',')
for i, k in enumerate(temp):
    print("--------------------------------------------------")
    if k[0] == 'L':
        print(f"Removing paths where the sum is less than {k[2:]}:")
        T.main_dfs(int(k[2:]), 'L')
    elif k[0] == 'E':
        print(f"Removing paths where the sum is equal to {k[3:]}:")
        T.main_dfs(int(k[3:]), 'E')
    elif k[0] == 'M':
        print(f"Removing paths where the sum is greater than {k[2:]}:")
        T.main_dfs(int(k[2:]), 'M')
    print("--------------------------------------------------")
    print("(City A) After the war:")
    if T.root is None :
        print("City A has fallen!")
        break
    T.printTree(T.root)
        

