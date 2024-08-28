import sys

class Stack:
    def __init__(self, list = None):
        if list == None:
            list = []
        self.lst = list
    
    def __len__(self):
        return len(self.lst)

    def items(self):
        return self.lst

    def push(self, data):
        self.lst.append(data)
    
    def pop(self):
        if not self.isEmpty():
            return self.lst.pop()
    
    def peek(self):
        if not self.isEmpty():
            return self.lst[-1]
    
    def isEmpty(self):
        return len(self.lst) == 0
    
    def size(self):
        return len(self.lst)



class Queue:
    def __init__(self, lst = None):
        if lst == None:
            lst = []
        self.lst = lst
    def __str__(self):
        return ''.join([str(i) for i in self.lst])
    
    def __len__(self):
        return len(self.lst)

    def items(self):
        return self.lst
    
    def push(self, data):
        self.lst.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.lst.pop(0)
        
    def top(self):
        if not self.isEmpty():
            return self.lst[0]
        
    def isEmpty(self):
        return len(self.lst) == 0

if __name__ == "__main__":
    a = Queue()
    b = Queue()
    a.push(1)
    a.push(2)
    a.push(3)
    a.push(4)
    a.push(5)
    print(a, b)