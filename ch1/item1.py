# รับจำนวนเต็ม 3 จำนวนจากแป้นพิมพ์
# เก็บในตัวแปร h, m และ s ซึ่งแทนจำนวน ชั่วโมง นาที และ วินาที


# แล้วแสดงผลเป็น วินาที
# # แสดงผลตามตัวอย่าง
# *** Converting hh.mm.ss to seconds ***
# Enter hh mm ss : 11 22 33
# 11:22:33 = 40,953 seconds

print("*** Converting hh.mm.ss to seconds ***")
hh, mm, ss = [int(i) for i in input("Enter hh mm ss : ").split(' ')]

if mm >= 60 or mm < 0:
    print(f'mm({mm}) is invalid!')
    exit()
elif ss >= 60 or ss < 0 :
    print(f'ss({ss}) is invalid!')
    exit()

ans = ss + mm*60 + hh*60*60

print(f'{hh:>02}:{mm:>02}:{ss:>02} = ' + "{:,}".format(ans) + " seconds")
