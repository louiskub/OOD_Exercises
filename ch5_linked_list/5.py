# เขียนโปรแกรมคลุกคำ (scramble) สร้าง singly linked list ของคำในจดหมาย scramble จดหมายโดยทำคล้ายตัด ไพ่และกรีดไพ่ ผู้รับจดหมาย descramble กรีดกลับและตัดกลับจนได้จดหมายฉบับเดิมที่อ่านได้(หากออกแบบดีๆ สามารถ scramble กี่ครั้งก็ได้ ขึ้นแรกให้ทำ ครั้งเดียวก่อน)  

# ***** รูปแบบ input *****

# แบ่งเป็น 2 ฝั่ง ได้แก่ ฝั่งซ้าย (Linked List เริ่มต้น  ความยาวขั้นต่ำของ Linked List รับประกันว่าขั้นต่ำคือ 10)  |  ฝั่งขวา BottomUp กับ Riffle โดยการแทนด้วย B กับ R ซึ่งการรับ R กับ B สามารถสลับที่กันได้ เช่น   R 40,B 60  <->  B 60,R 40

# 1.  B   < percentage >  :  bottomUp ตัด ยกส่วนบน (lift) ออกตาม % input ที่รับเข้ามา นำส่วนล่างมาซ้อนทับส่วนบน

# 2.  R   < percentage >  :  riffleShuffle กรีด (จากด้านบน) lift ตาม % นำ node ของแต่ละลิสต์มาสลับกันทีละ node จากต้นลิสต์ ส่วนเกินนำมาต่อท้าย

# ***** ถ้าหากคิดเปอร์เซ็นของความยาว Linked List แล้วได้ทศนิยม ให้ปัดลงทั้งหมด *****

# ***** การแสดงผลมี Pattern เป็น   Bottomup  ->  Riffle  ->  Deriffle  -> Debottomup นะครับ


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def appendHead(self,value):
        self.head = self.tail = Node(value)

    def appendLast(self,value):
        self.size += 1
        if self.head is None:
            self.appendHead(value)
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next
    
    def cut(self, percent):
        left = int(self.size * percent / 100)
        right = self.size - left

        left_list = List()
        now = left_list.head = self.head
        left_list.size = left
        for i in range(left-1):
            now = now.next
        left_list.tail = now

        right_list = List()
        right_list.head = now.next
        right_list.tail = self.tail
        right_list.size = right
        
        return left_list, right_list

    def printLL(self):
        s = ""
        now = self.head
        for i in range(self.size):
            s += str(now.value) + " "
            now = now.next
        return s

def createLL(LL):
    new_list = List()
    for i in range(len(LL)):
        new_list.appendLast(LL[i])
    return new_list

def printLL(h: List):
    return h.printLL()

def SIZE(h: List):
    return h.size

def riffle(lst1, lst2, r):
    temp = List()
    now = lst2.head
    for i in range(lst2.size):
        temp.appendLast(now.value)
        now = now.next
    now = lst1.head
    for i in range(lst1.size):
        temp.appendLast(now.value)
        now = now.next

    temp1, temp2 = temp.cut(r)
    now1, now2 = temp1.head, temp2.head
    count1, count2 = 0, 0

    s = ""
    for i in range(temp.size):
        if count1 < temp1.size:
            s += now1.value + " "
            now1 = now1.next
            count1 += 1
        if count2 < temp2.size:
            s += now2.value + " "
            now2 = now2.next
            count2 += 1
    return s


def scarmble(lst: List, b, r):
    lst1, lst2 = lst.cut(b)
    print(f"BottomUp {b:.3f} % : {lst2.printLL()}{lst1.printLL()}")
    print(f"Riffle {r:.3f} % : {riffle(lst1, lst2, r)}")
    print(f"Deriffle {r:.3f} % : {lst2.printLL()}{lst1.printLL()}")
    print(f"Debottomup {b:.3f} % : {lst.printLL()}")
        

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]))
    print('-' * 50)