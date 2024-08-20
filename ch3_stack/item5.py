# จงเขียนโปรแกรมโดยใช้ stack เพื่อรับตัวเลขฐาน 10 แล้วเปลี่ยนเป็นเลขฐาน 2 แล้วให้แสดงผลดังตัวอย่าง
def dec2bin(token):
    stack = []
    while token != 0:
        stack.append(token%2)
        token = int(token/2)
    stack.reverse()
    s = ''
    for i in stack:
        s += str(i)
    return s

print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))