inp = [int(e) for e in input("Enter list  of numbers: ").split()]
st = set(inp)
num = []

for i in st:
    found = inp.count(i)
    find = inp.index(i)
    num.append([i, find, found])


for i in range(len(num)):
    swapped = False
    for j in range(len(num)-i-1):
        if num[j][2] < num[j+1][2] or (num[j][2] == num[j+1][2] and num[j][1] > num[j+1][1]):
            swapped = True
            num[j], num[j+1] = num[j+1], num[j]
    
    if not swapped:
        break

for i in num:
    print(f'number {i[0]}, total: {i[2]}')


# ar = [10, 5, 5, 7]
# print(ar.index(5))