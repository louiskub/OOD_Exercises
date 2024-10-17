# วันนี้เราจะมาทำการเรียงการ์ดกันโดยไพ่โดยพี่คิดว่าน้องๆ หน้าจะรู้จักกันแล้ว แต่พี่จะอธิบายให้ฟังอีกครั้ง โดยการ์ดนั้นแบ่งออกเป็น 2 ส่วน คือหน้าไพ่(symbol) มี 4 แบบ คือ
# ดอกจิก(Clover) ข้าวหลามตัด(Diamonds) โพแดง(Hearts) โพดำ(Spades) โดยตัวย่อ C, D, H, S ตามลำดับโดยเรียงค่าจากน้อยไปมาก
# และ อีกส่วนคือเลข (num) ประกอบด้วย เลข 2 - 9 แล้วต่อด้วย T(10) , J (jack) , Q (queen คนไทยนิยมเรียกว่า แหม่ม) , K (king) , A (ace) โดยเรียงค่าจากน้อยไปมาก
# ในเมื่อตอนนี้น้องๆรู้เกี่ยวกับการ์ดกันแล้ว การเรียงการ์ดที่จะใช้ในโจทย์ครั้งนี้นั้นมี 2 วิธี คือ
# เรียงโดย เรียงเลขก่อน (num) คือ เรียง 2 ดอกจิก 2 ข้าวหลามตัด 2 โพแดง 2 โพดำ แล้วไป 3 ดอกจิก … จนถึง A โพดำ
# เรียง ดอกก่อน(symbol) คือ 2 ดอกจิก 3 ดอกจิก … A ดอกจิก 2ข้าวหลามตัด … จนถึง A โพดำ

# Enter Input: C5,CK,H7,D2,DA,H3,S4/symbol
# โดย input จะประกอบโดยตัวอักษร 2 ตัว เช่น C5 โดยตัวแรกคือดอก แล้ว ตัวหลังคือเลข และขั้นด้วย , เป็นการ์ดใบต่อไป โดยด้านหลัง / คือรูปแบบการเรียง คือ  num หรือ symbol
# ถ้ามีการ์ดซ้ำกันให้ข้ามการ์ดใบนั้นทิ้งแล้วพิมพ์ “Error: Duplicate card found - H7”แล้วตามด้วยชื่อการ์ดใบนั้นในกรณีนี้คือ H7 
# ถ้ามีการใส่การ์ดที่ไม่มีอยู่จริง ก็ให้ข้ามการ์ดใบนั้นแล้วพิมพ์ “Error: X9 is an invalid card” พร้อมบอกชื่อการ์ดใบนั้นในกรณีนี้คือ X9 
# ถ้าไม่มีการ์ดให้เรียงไม่ว่าจะเกิดจากการที่มีแต่การ์ดแปลกๆหรือไม่มีการ์ดให้พิมพ์ ”No valid cards to sort.” ออกมา
# ***หมายเหตุ ห้ามใช้ทำสั่ง .sort() ข้อนี้อยากใช้อยากใช้วิธีใหนในการเรียงใช้ได้หมด แต่พี่แนะนำให้ลองใช้ insert sort***
# ***หมายเหตุ 2: หากอยากท้าทายโจทย์นี้ให้ยากขึ้นลองทำเป็น recursive ดู ไม่ได้บังคับไม่อยากทำก็ได้แล้วแต่น้อง***


# Have fun with sort card
# Enter Input: C5,CK,H7,D2,DA,H3,S4/symbol
# Sorted cards : C5 CK D2 DA H3 H7 S4 


def insertion(inp, typ):
    # symbol = "CDHS"
    # num = "23456789TJQKA"
    compare = ["CDHS", "23456789TJQKA"]
    swapped = False
    # dup = set()
    i = -1
    while i+1 < len(inp):
        i += 1
        # print(inp[i])
        if inp[i][0] not in compare[0] or \
            inp[i][1] not in compare[1] or len(inp[i]) > 2:
                print(f'Error: {inp[i]} is an invalid card')
                inp.pop(i)
                i -= 1
                continue
        # if inp[i] in dup:
        #     print(f'Error: Duplicate card found - {inp[i]}')
        #     i -= 1
        #     continue
        # dup.add(inp[i])
        for j in range(i, 0, -1):
            if inp[j] == inp[j-1]:
                print(f'Error: Duplicate card found - {inp[j]}')
                inp.pop(j)
                i -= 1
                break
            if compare[typ].index(inp[j][typ]) < compare[typ].index(inp[j-1][typ]) or\
                (compare[typ].index(inp[j][typ]) == compare[typ].index(inp[j-1][typ]) and \
                 compare[not typ].index(inp[j][not typ]) < compare[not typ].index(inp[j-1][not typ])):
                swapped = True
                inp[j], inp[j-1] = inp[j-1], inp[j]
            else:
                break
    # print(inp)
    if swapped:
        print("Sorted cards : ", end="")
        print(" ".join(inp))
    else :
        print("No valid cards to sort.")
        
    


print("Have fun with sort card")
inp, typ = input('Enter Input: ').split('/')
inp = inp.split(',')
if typ and inp:
    typ = 0 if typ[0] == "s" else 1
    sorted = insertion(inp, typ)
else :
    print("No valid cards to sort.")

