# วันหนึ่งนายที่มาก่อน y แต่หลัง w อยากลองทดสอบเสียงจึงไล่คีย์โน้ต โด เร มี ฟา ซอน ลา ที แต่เขาไม่ชอบที่ร้องซ้ำคีย์เดิม และมีคีย์อยู่ในหัวใจ แต่คนอื่นในจักรวาลมักจะให้คีย์ที่ไม่ถูกใจเขา เขาจึงอยากวอนขอให้โปรแกรมเมอร์ระดับจักรวาลช่วยเขียนโปรแกรมนี้ขึ้นมา โดยการทำงานมีดังนี้
# อินพุทแรก จะรับคีย์โน้ตโดยสามารถซ้ำกันได้ และคั่นด้วยช่องว่าง
# อินพุทที่สอง จะรับ serie of operation และจะคั่นด้วยคอมม่า โดยมี 3 รูปแบบดังนี้
# D(Delete) : ให้ทำการลบตัวหลังสุดของ LinkedList
# R(Rename) : ให้เปลี่ยนคีย์โน้ตตัวหลังสุดของ LinkedList ตามที่ป้อนมา เช่น R mi แปลว่า เปลี่ยนจาก … เป็น mi
# A(Add) : ให้เพิ่มคีย์โน้ตตามที่ป้อมมา เช่น A mi แปลว่า เพิ่มโน้ต mi ต่อท้าย LinkedList
# ด้วยการรับมาในครั้งเดียว แบ่ง อินพุททั้ง 2 ด้วยเครื่องหมาย / 
# ให้แสดงผล LinkedList 3 ครั้ง โดยมีรูปแบบเป็นไปตาม Test Case
# ก่อนจะทำตาม operation ต่างๆที่ป้อนมา
# หลังจากทำตาม operation
# LinkedList ที่ไม่มีข้อมูลซ้ำกัน
# สามารถเพิ่มโค้ดในบรรทัดที่เขียนว่า #CODE HERE หรือเพิ่ม method ในคลาส LinkedList ได้


# ****Note****
# -หากมี Error เกิดขึ้นในระหว่างที่ทำ operation ให้แสดงคำว่า Error!!! ทันที
# -ถ้า LinkedList ว่าง ให้แสดงคำว่า LinkedList is empty!




lst = [int(i) for i in input('Enter Your List : ').split()]
n = len(lst)
ans_set = set()
def recur(i, hist: list) :
    hist = hist + [lst[i]]
    if len(hist) == 3:
        sum = 0
        for j in hist:
            sum += j
        if sum == 5:
            ans_set.add(tuple(sorted(hist)))
        return
    for j in range(i+1, n):
        recur(j, hist)

for i in range(n):
    recur(i, [])
if len(ans_set) == 0:
    print("Array Input Length Must More Than 2")
else :
    # ans = set(ans)
    ans = [list(i) for i in list(ans_set)]
    print(list(ans))