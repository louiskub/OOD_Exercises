
# จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue

# โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้

# แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ

# แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ

# ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2

# จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2]

s, number = input('Enter people and time : ').split()
s = list(s)
q1, q2 = [], []
q1_now, q2_now = 1, 1
for i in range(1, int(number)+1):
    if len(s) < 1:
        now = False
    else :
        now = s.pop(0)
    if i%3 == 1 and len(q1) > 0:    # ถ้า3นาทีให้ทำต่อ
        q1.pop(0)
    if i%2 == 0 and len(q2) > 0:    # ถ้า3นาทีให้ทำต่อ
        q2.pop(0)

    if now != False :
        if len(q1) < 5:
            q1.append(now)
        elif len(q2) < 5:
            q2.append(now)
        
    print(i, s, q1, q2)