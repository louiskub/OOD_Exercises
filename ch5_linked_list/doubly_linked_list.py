class Node:
    def __init__(self, data) -> None:
        self.prev = None
        self.data = data
        self.next = None
    
class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        cur = self.head
        s = []
        for i in range(self.size):
            s.append(str(cur.data))
            cur = cur.next
        return " ".join(s)

    def append(self, data):
        temp = Node(data)
        self.size += 1
        if self.head == None and self.tail == None:
            self.head = self.tail = temp
        else :
            temp.prev = self.tail
            self.tail.next = temp
            self.tail = temp

    def insert(self, index, data):
        if index >= self.size:
            self.append(data)
            return
        
        self.size += 1
        temp = Node(data)
        cur = self.head
        if index == 0:
            self.head.prev = temp
            temp.next = self.head
            self.head = temp
            return
        
        for i in range(index-1):
            cur = cur.next
        next_node = cur.next
        temp.prev = cur
        temp.next = next_node
        cur.next = temp
        next_node.prev = cur
    

    def pop(self, index = -1):
        if self.size == 1:
            self.head = self.tail = None
            self.size = 0
            return
        
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            self.head.prev = None
            return

        if index >= self.size or index == -1:
            self.size -= 1
            self.tail = self.tail.prev
            self.tail.next = None
            return

        cur = self.head
        for i in range(index-1):
            cur = cur.next
        next_node = cur.next.next
        cur.next = next_node
        next_node.prev = cur
        self.size -=1


lst = List()
for i in range(10):
    lst.append(i)
print(lst)

print("INSERT")
lst.insert(0, 10)
lst.insert(2, 20)
lst.insert(20, 50)
print(lst)

print("POP")
lst.pop()
lst.pop(0)
lst.pop(2)
print(lst)

# print("remove")
# lst.remove(20)
# lst.remove(9)
# lst.remove(7)
# print(lst)




