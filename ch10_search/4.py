def is_prime_with_flag(num):
    if num <= 1:
        return False
    flag = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            flag = False
            break
    return flag

class Data:
    def __init__(self, key, value):
        self.key = int(key)
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Hash:
    def __init__(self, size, collision, tres): 
        self.size = size
        self.col_max = collision
        self.table = [None] * self.size
        self.tres = tres
        self.ele = 0
    
    def __str__(self):
        ans = ""
        for i in range(self.size):
            ans += f"#{i+1}	{self.table[i]}\n"
        ans += "----------------------------------------" 
        return ans

    def hashFunction(self, key):
        return key % self.size

    def add(self, data, datas, idx):
        self.ele += 1
        # print(self.ele, int(self.tres * self.size))
        if self.ele >= (self.tres * self.size):
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash(data, datas)
        else:
            self.table[idx] = Data(idx, data)

    def rehash(self, data, datas):
        self.ele = 0
        if self.size < 2:
            self.size = 2

        else :
            s = self.size * 2 + 1
            while not is_prime_with_flag(s):
                s += 2
            self.size = s
        self.table = [None]*self.size
        # print(self.size)
        for d in datas:
            self.condition(d, datas)
            if d == data:
                break
    
    def condition(self, data, datas):
        idx = self.hashFunction(data)
        if self.table[idx] == None:
            self.add(data, datas, idx)
        else:
            idx = self.collision(data)
            if idx != None:
                self.add(data, datas, idx)
            else:
                self.rehash(data, datas)
    
    def collision(self, data):
        idx = self.hashFunction(data)
        temp = idx//1
        for i in range(1, self.col_max + 1):
            if self.table[idx] == None:
                return idx
            else:
                print(f'collision number {i} at {idx}')
                idx = (temp + i**2) % self.size

        print("****** Max collision - Rehash !!! ******")
        return None




print(" ***** Rehashing *****")
inp = input("Enter Input : ").split('/')
tb_size, col_max, treshold = [int(e) for e in inp[0].split()]
inp = [int(e) for e in inp[1].split()]

hash = Hash(tb_size, col_max, treshold/100)
print("Initial Table :")
print(hash)
for i in inp:
    print(f"Add : {i}")
    hash.condition(i,inp)
    print(hash)

