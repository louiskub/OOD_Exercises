from stack_implement import Queue

inp = [int(e) for e in input('Number : ').split()]
print(inp)
max_len = len(str(max(inp)))

q = [Queue() for k in range(10)]
result = Queue(inp)

for i in range(max_len):
    for num in inp:
        temp = (num//(10**i)) % 10
        q[temp].push(num)
    
    for j in range(10):
        print(j, q[j].lst)

    inp = []
    # for que in range(10):
    for que in range(9,-1,-1):    #REVERSE
        while not q[que].isEmpty():
            inp.append(q[que].pop())
    print(inp)
    print("\n")

print(inp)
            

