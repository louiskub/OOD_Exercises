# วันหนึ่งนายที่มาก่อน y แต่หลัง w อยากลองทดสอบเสียงจึงไล่คีย์โน้ต โด เร มี ฟา ซอน ลา ที แต่เขาไม่ชอบที่ร้องซ้ำคีย์เดิม และมีคีย์อยู่ในหัวใจ แต่คนอื่นในจักรวาลมักจะให้คีย์ที่ไม่ถูกใจเขา เขาจึงอยากวอนขอให้โปรแกรมเมอร์ระดับจักรวาลช่วยเขียนโปรแกรมนี้ขึ้นมา โดยการทำงานมีดังนี้

# อินพุทแรก จะรับคีย์โน้ตโดยสามารถซ้ำกันได้ และคั่นด้วยช่องว่าง

# อินพุทที่สอง จะรับ serie of operation และจะคั่นด้วยคอมม่า โดยมี 3 รูปแบบดังนี้

# D(Delete) : ให้ทำการลบตัวหลังสุดของ LinkedList

# R(Rename) : ให้เปลี่ยนคีย์โน้ตตัวหลังสุดของ LinkedList ตามที่ป้อนมา เช่น R mi แปลว่า เปลี่ยนจาก … เป็น mi

# A(Add) : ให้เพิ่มคีย์โน้ตตามที่ป้อมมา เช่น A mi แปลว่า เพิ่มโน้ต mi ต่อท้าย LinkedList



# ด้วยการรับมาในครั้งเดียว แบ่ง อินพุททั้ง 2 ด้วยเครื่องหมาย / 

# ให้แสดงผล LinkedList 3 ครั้ง โดยมีรูปแบบเป็นไปตาม Test Case

# ก่อนจะทำตาม operation ต่างๆที่ป้อนมา

# หลังจากทำตาม operation

# LinkedList ที่ไม่มีข้อมูลซ้ำกัน


# สามารถเพิ่มโค้ดในบรรทัดที่เขียนว่า #CODE HERE หรือเพิ่ม method ในคลาส LinkedList ได้


# ****Note****

# -หากมี Error เกิดขึ้นในระหว่างที่ทำ operation ให้แสดงคำว่า Error!!! ทันที

# -ถ้า LinkedList ว่าง ให้แสดงคำว่า LinkedList is empty!




# *******ห้ามใช้ List! ให้ใช้ class Node ในการทำ Linked List เท่านั้น*********


class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

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

    def removeLast(self):
        if self.size == 1:
            self.head = self.tail = None
            self.size -= 1
        elif self.size > 1:
            now = self.head
            while now.next != self.tail:
                now = now.next
            now.next = None
            self.tail = now
            self.size -= 1
        else :
            print("Error!!!")

    def rename(self, newName):
        if self.size == 0:
            print("Error!!!")
            return
        self.tail.value = newName

    def printList(self):
        if self.size == 0:
            print("Linklist is empty!")
            return
        s = ""
        now = self.head
        for i in range(self.size-1):
            s += now.value + " -> "
            now = now.next
        s += now.value
        print(s)

    def printListWithNoDuplicate(self):
        if self.size == 0:
            print("Linklist is empty!")
            return
        s = ""
        now = self.head
        for i in range(self.size-1):
            if now.value not in s:
                s += now.value + " -> "
            now = now.next
        if now.value not in s:
            s += now.value
        else :
            s = s[:-4]
        print(s)


def convertToLinkList(ls):
    ans = List()
    for i in ls:
        ans.appendLast(i)
    return ans


print("*** My Favourite Keynote ***")
inputl = input("Enter Input / List of operation : ").split('/')
listSong = [ele for ele in inputl[0].strip().split(' ')]
operations = [ele for ele in inputl[1].strip().split(", ")]
myLinkList = convertToLinkList(listSong)
myLinkList.printList()
# #CODE HERE
for i in operations:
    if i[0] == 'D':
        myLinkList.removeLast()
    elif i[0] == 'R':
        myLinkList.rename(i[2:])
    else :
        myLinkList.appendLast(i[2:])
# print(operations)
myLinkList.printList()
myLinkList.printListWithNoDuplicate()