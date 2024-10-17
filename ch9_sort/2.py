# ให้เรียงลำดับ input จากเลขที่มีค่าซ้ำกันมากที่สุด ไป ซ้ำน้อยที่สุด
# มีเงื่อนไขว่า หากเลขที่มีจำนวนซ้ำเท่ากันให้แสดงจากเลขที่มาก่อนไปหลังเสมอ 

# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง
# Enter list  of numbers: 1 2 2 3 3 3
# number 3, total: 3
# number 2, total: 2
# number 1, total: 1



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