# รับ input จำนวนเต็มสองจำนวน หากผลคูณของทั้งสองจำนวนมีค่าเกิน 1000 ให้ show ผลรวมของจำนวนทั้งสอง แต่หากผลคูณมีค่าน้อยกว่าหรือเท่ากับ 1,000 ให้ show ผลคูณของจำนวนทั้งสอง
# *** multiplication or sum ***
# Enter num1 num2 : 20 30
# The result is 600


print("*** multiplication or sum ***")
n, m= [int(i) for i in input("Enter num1 num2 : ").split(' ')]

mult = n*m
if mult > 1000:
    print(f'The result is {n+m}')
else :
    print(f'The result is {mult}')