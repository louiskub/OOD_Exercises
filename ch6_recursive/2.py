# ให้นักศึกษาเขียนฟังก์ชันที่ทำงานเหมือนกับฟังก์ชัน len() เพื่อหาความยาวของ string และแสดงผลดังตัวอย่าง(print ตัวอักษรตามด้วยเครื่องหมายพิเศษสลับกันคู่คี่)

# ****ห้ามใช้คำสั่ง len, for, while, do while, split*****

# หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว


s = input("Enter Input : ")

def length(txt):     
    try :
        if txt%2 == 0 :
            print(s[txt]+"*", end="")
        else :
            print(s[txt]+"~", end="")
        return length(txt+1)
    except :
        return txt

print("\n",length(0), sep="")
#ตรง print(เป็นแค่ตัวอย่างสามารถแก้ไขได้)