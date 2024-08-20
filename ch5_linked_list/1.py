class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class List:
    def __init__(self, head = None) -> None:
        self.head = head
        self.tail = head
        self.size = 0

    def add_head(self, data):
        node = Node(data)
        self.head = node
        self.size += 1

    def append(self, data): 
        node = Node(data)
        self.tail.next = node
        self.tail = node
        self.size += 1

    def insert(self, index, data):
        pass

    def remove(self, index):
        if index == 0 :
            self.head = self.head.next
            self.size -= 1
        else :
            now = self.head.next
            prev = self.head
            count = 0
            while now != None:
                if count == index:
                    prev.next = now.next
                    self.size -= 1
                    break
                else :
                    prev = now
                    now = now.next
                    count += 1
        
