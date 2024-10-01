class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, size, collision): 
        self.size = size
        self.col_max = collision
        self.table = [[None] for _ in range(size)]
    
    def __str__(self):
        ans = ""
        for i in range(self.size):
            ans += f"#{i+1}	{self.table[i][0]}\n"
        ans += "---------------------------" 
        return ans

    def hashFunction(self, key):
        ans = 0
        for i in key:
            ans += ord(i)
        return ans % self.size

    def add(self, data):
        # print(data)
        key, val = data
        idx = self.hashFunction(key)
        temp = idx//1

        for i in range(1, self.col_max + 1):
            if self.table[idx][0] == None:
                new_data = Data(key, val)
                self.table[idx][0] = new_data
                return
            else:
                print(f'collision number {i} at {idx}')
                idx = (temp + i**2) % self.size
        print("Max of collisionChain")

    def isFull(self):
        for i in self.table:
            if i[0] == None:
                return False
        return True
        


print(" ***** Fun with hashing *****")
inp = input("Enter Input : ").split('/')
tb_size, col_max = [int(e) for e in inp[0].split()]
inp = inp[1].split(',')
hash = Hash(tb_size, col_max)
for i in inp:
    d = i.split()
    if hash.isFull():
        print('This table is full !!!!!!')
        break
    else:
        hash.add(d)
        print(hash)