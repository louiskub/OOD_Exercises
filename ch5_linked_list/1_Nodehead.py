class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class List:
    def __init__(self) -> None:
        temp = Node(None)
        self.head = temp
        self.tail = temp
        self.size = 0

    def show(self):
        now = self.head
        while now.next != None:
            print(now.next.data, end=" ")
            now = now.next

    def add_head(self, data):
        node = Node(data)
        self.head.next = node
        self.size += 1

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
    
    
s = input('Enter Input : ').split()
lst = List()
# node = []
for i in s:
    lst.append(i)

print("Linked list now is ", end="")
lst.show()

now = lst.head.next
count = 0
while now!= None and now.next != None:
    nested = now.next
    while True:
        if nested and nested.data == now.data:
            lst.remove(nested)
            count += 1
        if nested == lst.tail or nested == None:
            break
        nested = nested.next
    now = now.next

print()
print(f"there are {count} duplicates that been remove")
print("Remove duplicates Linked list ", end="")
lst.show()
# print(lst.head.data, lst.tail.data)