# รับ input เป็น list แล้วแสดงขั้นตอนของ bubble sort ตามตัวอย่าง

# ***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import**

inp = [int(e) for e in input("Enter Input : ").split()]
step = 1
for i in range(len(inp)):
    swapped = False
    for j in range(len(inp)-i-1):
        if inp[j] > inp[j+1]:
            swapped = inp[j]
            inp[j], inp[j+1] = inp[j+1], inp[j]
    
    if not swapped:
        print(f'last step : {inp} move[None]')
        break
    else:
        if i == len(inp)-2:
            print(f'last step : {inp} move[{swapped}]')
            break
        else :
            print(f'{step} step : {inp} move[{swapped}]')
        step += 1

