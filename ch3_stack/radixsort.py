from stack_implement import Queue

inp = input('Number : ').split()
maxlen = 0
for i in range(len(inp)):
    maxlen = max(maxlen, len(inp[i]))
    inp[i] = int(inp[i])

num = [Queue() for _ in range(10)]
for i in range(maxlen):
    # sort 0-9
    for cur in inp:
        temp = int(cur / (10**i)) % 10
        num[temp].push(cur)
    
    for j in range(10):
        print(j, num[j].lst)
    print("\n")
    # reset sort
    inp = []
    for q in range(9,-1,-1):
        while not num[q].isEmpty():
            inp.append(num[q].pop())
    
print(inp)

