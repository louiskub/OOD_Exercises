class Node:
    def __init__(self, data) -> None:
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
            self.tail.next = temp
            self.tail = temp

    def insert(self, index, data):
        if index >= self.size:
            self.append(data)
            return
        
        self.size += 1
        temp = Node(data)
        if index == 0 :
            temp.next = self.head
            self.head = temp
            return

        cur = self.head
        for i in range(index-1):
            cur = cur.next
        temp.next = cur.next
        cur.next = temp

    
    def pop(self, index = -1):
        if index == 0 :
            self.head = self.head.next
            self.size -= 1
            return
        
        if index >= self.size or index == -1:
            index = self.size-1
        cur = self.head
        for i in range(index-1):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1
        if index == self.size:
            self.tail = cur

    def remove(self, data):
        cur = self.head
        for i in range(self.size):
            if data == cur.data:
                self.pop(i)
                return
            cur = cur.next
            
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
lst.pop(5)
print(lst)

print("remove")
lst.remove(20)
lst.remove(9)
lst.remove(7)
print(lst)




