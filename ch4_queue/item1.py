# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ Queue ในการแก้ปัญหา



# E  <value>  ให้นำ value ไปใส่ใน Queue และทำการแสดงผล ข้อมูลปัจจุบันของ Queue

# D                 ให้ทำการ Dequeue ตัวที่อยู่หน้าสุดของ Queue ออก หลังจากนั้นแสดงตัวเลขที่เอาออกมา และ แสดงผลข้อมูล
#                     ปัจจุบันของ Queue

# ***และเมื่อจบการทำงานให้แสดงผลข้อมูลปัจจุบันของ Queue พร้อมกับข้อมูลที่ถูก Dequeue ทั้งหมดตามลำดับ
# ***ถ้าหากไม่มีข้อมูลใน Queue แล้วให้แสดงคำว่า  Empty


lst = [e.split() for e in input('Enter Input : ').split(',')]
# print(lst)
q = []
dq = []

for i in lst:
    if i[0] == 'E':
        q.append(i)
    elif i[0] == 'D' and len(q) > 0 :
            temp = q.pop(0)
            dq.append(temp)
            print(f"{temp[1]} <- ", end="")

    if len(q) == 0 :
        print("Empty")
    else :
        print(", ".join(k[1] for k in q))


if len(dq) == 0 :
    print("Empty : ", end="")
else :
    print(", ".join(k[1] for k in dq), ":", end=" ")


if len(q) == 0:
    print("Empty")
else :
    print(", ".join(k[1] for k in q))
