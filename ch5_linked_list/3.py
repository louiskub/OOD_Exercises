# Arthur เป็นเด็กหนุ่มผู้หลงใหลในการเขียนโปรแกรมและการแก้ปริศนา หนึ่งวันหนึ่ง เขาได้รับ จดหมายลึกลับที่บอกว่าเขาถูกเชิญให้ไปที่เมืองปริศนา ซึ่งเป็นเมืองที่ถูกสร้างขึ้นมาจากโครงสร้างข้อมูล แบบ Linked List ทั้งหมด

# เมื่อ Arthur มาถึงเมืองปริศนา เขาพบว่าที่นี่มีการจัดการแข่งขันเขียนโปรแกรม โดยมีเป้าหมายคือ การแก้ปริศนาและช่วยเหลือผู้อยู่อาศัยในเมืองปริศนาให้พ้นจากปัญหาต่างๆ ที่เกิดขึ้นจากโครงสร้าง ข้อมูลที่ซับซ้อน Arthur ได้รับภารกิจแรกคือการแก้ปัญหาการจัดเรียงข้อมูลใน Linked List เพื่อทำให้ข้อมูลเรียงลำดับถูกต้อง

# ระดับความยาก : ง่ายคดๆ

# หมายเหตุ:

# - หลักการจัดวางคือ ตัวเลข, ตัวอักษรพิมพ์ใหญ่, ตัวอักษรพิมพ์เล็ก (คุ้นๆไหมมันคืออะไร?)
# - ไม่อนุญาตให้ใช้ .sort() เพราะตรวจ code นะจ๊ะ



class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

class List:
    def __init__(self, head = None) -> None:
        temp = Node(None)
        self.head = temp
        self.tail = temp
        self.size = 0

    def __str__(self):
        s = []
        now = self.head.next
        for i in range(self.size):
            s.append(now.data)
            now = now.next
        return " -> ".join(s)
    
    def append(self, data): 
        node = Node(data)
        self.tail.next = node
        self.tail = node
        self.size += 1
    
    def remove(self, node):
        now = self.head
        while now.next != None:
            if now.next == node:
                if now.next == self.tail:
                    now.next = None
                    self.tail = now
                else :
                    now.next = now.next.next
                self.size -= 1
                return
            now = now.next
    
    def find_index(self, data):
        now = self.head.next
        for i in range(self.size):
            if now.data == data:
                return now
            now = now.next
        return None

def function(lst: List):
    temp = List()
    now = min = lst.head.next
    while lst.size > 0 :
        if now.data < min.data :
            min = now
        if now == lst.tail:
            temp.append(min.data)
            lst.remove(min)
            now = min = lst.head.next
        else :
            now = now.next
    return temp

s = input("Enter unsorted Linked List: ").split()
lst = List()
for i in s:
    lst.append(i)
print(f"Before: {lst}")
print(f"After : {function(lst)}")
# print(f"After : {" -> ".join(new_lst.to_list())}")

