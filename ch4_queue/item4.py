# ณ ร้านกาแฟแห่งหนึ่งมีบาริสต้า 2 คน จะมีลูกค้าเข้ามาในร้านเวลา (si) บาริสต้าจะทำกาแฟให้ลูกค้าแต่ละคนในเวลา (pi) ที่ต่างกัน ดังนั้นจะมีคนที่รอคิวอยู่ แสดงลำดับลูกค้าที่ได้กาแฟ และคนที่รอคิวเพื่อจะสั่งกาแฟนานที่สุดรอกี่นาที ถ้าไม่ต้องรอคิวเลยให้แสดง No waiting


# ตัวอย่างข้อมูลเข้า
# Log : 0,3/0,7/2,3/7,7/10,5/10,1
# คำอธิบาย
# ลูกค้าคนที่ 1 เข้ามาในเวลาที่ 0 และสั่งกาแฟที่ทำนาน 3 นาที 
# ลูกค้าคนที่ 2 เข้ามาในเวลาที่ 0 และสั่งกาแฟที่ทำนาน 7 นาที 
# ลูกค้าคนที่ 3 เข้ามาในเวลาที่ 2 และสั่งกาแฟที่ทำนาน 3 นาที 
# ลูกค้าคนที่ 4 เข้ามาในเวลาที่ 7 และสั่งกาแฟที่ทำนาน 7 นาที 
# ลูกค้าคนที่ 5 เข้ามาในเวลาที่ 10 และสั่งกาแฟที่ทำนาน 5 นาที 
# ลูกค้าคนที่ 6 เข้ามาในเวลาที่ 10 และสั่งกาแฟที่ทำนาน 1 นาที 



# ไทม์ไลน์
# เวลา(t)    เหตุการณ์
# 0    ลูกค้าคนที่ 1 และ 2 เข้ามาในร้านและสั่งกาแฟ
# 2    ลูกค้าคนที่ 3 เข้ามาในร้าน
# 3    ลูกค้าคนที่ 1 ได้กาแฟ ลูกค้าคนที่ 3 สั่งกาแฟหลังจากรอคิวไป 1 นาที
# 6    ลูกค้าคนที่ 3 ได้กาแฟ
# 7    ลูกค้าคนที่ 2 ได้กาแฟ ลูกค้าคนที่ 4 เข้ามาในร้านและสั่งกาแฟ
# 10    ลูกค้าคนที่ 5 และ 6 เข้ามาในร้าน ลูกค้าคนที่ 5 สั่งกาแฟ
# 14    ลูกค้าคนที่ 4 ได้กาแฟ ลูกค้าคนที่ 6 สั่งกาแฟหลังจากรอคิวไป 4 นาที
# 15    ลูกค้าคนที่ 5 และ 6 ได้กาแฟ


# ผลลัพธ์ 
# Time 3 customer 1 get coffee  
# Time 6 customer 3 get coffee  
# Time 7 customer 2 get coffee  
# Time 14 customer 4 get coffee  
# Time 15 customer 5 get coffee  
# Time 15 customer 6 get coffee  
# The customer who waited the longest is : 6
# The customer waited for 4 minutes


print(" ***Cafe***")
log = [[int(k) for k in e.split(',')] for e in input('Log : ').split('/')]
q1, q2 = [], []
q1t, q2t = 0, 0
wait, wait_cust = 0, 0
customer = 1

for l in log:
    
    if q1t <= q2t:
        if q1t > l[0]:
            if q1t-l[0] > wait:
                wait = q1t-l[0]
                wait_cust = customer
            l[0] = q1t
        q1t = l[0] + l[1]
        q1.append(l)
    else :
        if q2t > l[0]:
            if q2t-l[0] > wait:
                wait = q2t-l[0]
                wait_cust = customer
            l[0] = q2t
        q2t = l[0] + l[1]
        q2.append(l)
    l.append(customer)
    customer += 1
# print(q1, q2, wait_cust, wait, sep="\n")


while q1 or q2 :
    t1 = 100000
    t2 = 100000
    if q1:
        t1 = q1[0][0] + q1[0][1]
    if q2:
        t2 = q2[0][0] + q2[0][1]
    
    if t1 < t2 or (t1 == t2 and q1[0][2] < q2[0][2]):
        print(f"Time {t1} customer {q1[0][2]} get coffee ")
        q1.pop(0)

    else:
        print(f"Time {t2} customer {q2[0][2]} get coffee ")
        q2.pop(0)

if wait == 0 :
    print("No waiting")
else :
    print(f"The customer who waited the longest is : {wait_cust}")
    print(f"The customer waited for {wait} minutes")