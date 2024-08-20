# ณ เมืองแห่งหนึ่ง ที่มีชื่อว่า ... อืม (เอ้าผู้แต่งโจทย์คิดชื่อไม่ออก เอาเป็นว่าไม่ต้องสนใจก็ได้) 

# จะมีบริการคมนาคมสาธารณะ ซึ่งเป็นสิ่งที่น้องๆ พี่ๆ อาจารย์ หรือ บุคคลอื่นๆ ที่อาจจะคุณเคยกันหรือเคยนั้งก็มานั้นก็คือ "รถไฟฟ้า" นั้นเอง

# โดยแต่ละเมือง จะเปรียบเหมือน Node ของ Linked List ซึ่งรถไฟฟ้าจะมีทั้งขาไปขากลับนั้นเอง และ 

# รถไฟฟ้าขาไป ผ่านสถานีสุดท้ายของทางรถไฟฟ้าจะวนกลับมาสถานีแรก หรือในทางกลับกัน 

# รถไฟฟ้าขากลับผ่านสถานีแรกก็จะวนกลับไปสถานีสุดท้ายเช่นกัน 

# เพื่อให้ "พี่โบ๊ท" ที่เป็นชาวเมืองนี้มีรถไฟฟ้านั้นไปทำงานหรือท่องเทียวในเมืองนี้ได้สะดวกขึ้น 

# ต่อไปก็เป็นหน้าที่ของน้อง ๆ แล้วล่ะ ที่จะสานฝันให้เมืองนี้และ "พี่โบ๊ท" มี ระบบรถไฟฟ้าที่ "สมบูรณ์แบบ" ที่สร้างขึ้นมาจากน้ำมือของน้องเองๆ 


# input จะเป็น
# บรรทัดแรก จะเป็น list ของ ชื่อสถาณี
# บรรทัดสอง จะเป็น สถานีต้นทาง,สถานีปลายทาง,ทิศทางของรถไฟฟ้า(ถ้าไม่ใส่ให้แสดงผลในขาที่ระยะทางสั้นที่สุด ถ้าเกิดเท่ากัน ให้แสดงผลลัพธ์ทั้งขาไปและขากลับ)
# โดย F จะเป็น รถไฟฟ้าขาไป
#     B จะเป็น รถไฟฟ้าขากลับ
# output จะเป็น
# แสดงการเดินทางของรถไฟฟ้า,จำนวนสถานีที่จะถึงปลายทาง


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
    
    def append(self, data): 
        node = Node(data, self.head.next)
        self.tail.next = node
        self.tail = node
        self.size += 1
    
    def __str__(self):
        s = ""
        now = self.head.next
        for i in range(self.size):
            s += str(now.data) + " "
            now = now.next
        return s
        

    def find_index(self, data):
        now = self.head.next
        for i in range(self.size):
            if now.data == data:
                return now
            now = now.next
        return None


def function(town: List, start, end):
    now = start
    s = []
    while now != end:
        s.append(now.data)
        now = now.next
        if now == None:
            now = town.head
    s.append(end.data)
    return s

def traverse(town: List, route: list):
    start = town.find_index(route[0])
    end = town.find_index(route[1])
    if len(route) == 3:
        if route[2] == 'B':
            ans = ["B", function(town, end, start)[::-1]]
        else :
            ans = ["F", function(town, start, end)]
    else :
        forward = function(town, start, end)
        backward = function(town, end, start)[::-1]
        if len(forward) < len(backward):
            ans = ["F", forward]
        elif len(forward) > len(backward):
            ans = ["B", backward]
        else :
            return [["F", "->".join(forward), len(forward)-1], 
                    ["B", "->".join(backward), len(backward)-1]]
            
    return [[ans[0], "->".join(ans[1]), len(ans[1])-1]]            
print("***Railway on route***")
s, route = [e.split(',') for e in input("Input Station name/Source, Destination, Direction(optional): ").split('/')]
town = List()
for i in s:
    town.append(i)
ans = traverse(town, route)

for i in ans:
    if i[0] == "F":
        print(f"Forward Route: {i[1]},{i[2]}")
    elif i[0] == "B":
        print(f"Backward Route: {i[1]},{i[2]}")


