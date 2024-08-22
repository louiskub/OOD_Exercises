# ให้นักศึกษาเขียนฟังก์ชันที่ทำงานเหมือนกับฟังก์ชัน len() เพื่อหาความยาวของ string และแสดงผลดังตัวอย่าง(print ตัวอักษรตามด้วยเครื่องหมายพิเศษสลับกันคู่คี่)

# ****ห้ามใช้คำสั่ง len, for, while, do while, split*****

# หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว

s = input("Enter Input : ")
# "abcd"

def recur(i):
    try:
        if i%2 == 0:
            print(s[i]+"*", end="")
        else :
            print(s[i]+"$", end="")
        return recur(i+1)
    except:
        return i

print(recur(0))