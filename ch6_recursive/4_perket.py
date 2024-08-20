sour, bitt = [], []

def perket(cur, val_s, val_b):
    # print(cur, val_s, val_b)
    if cur == len(sour):
        if val_s == 1 and val_b == 0:
            return 1000000000
        return abs(val_s - val_b)
    return min(perket(cur+1, val_s*sour[cur], val_b+bitt[cur]), 
            perket(cur+1, val_s, val_b))  #ใช้กับไม่ใช้



s = input('Enter Input : ').split(',')
for i in s:
    temp = i.split()
    sour.append(int(temp[0]))
    bitt.append(int(temp[1]))
# print(sour, bitt)
print(perket(0, 1, 0))
