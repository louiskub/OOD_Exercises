# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

# เขียน Recursive เพื่อหาว่าเลขตั้งแต่ 0 จนถึง ( 2^(input) ) - 1 นั้นมีตัวอะไรบ้าง  หากเป็นเลขติดลบให้แสดงผลเป็น Only Positive & Zero Number ! ! ! 

# *** ตัวอย่างเช่น ถ้าหาก input = 2 ก็ต้องแสดงผลลัพธ์เป็น 00 , 01 , 10 , 11


def fun(num): # 0000
    txt = f"{int(num):0{nums}b}"
    if len(txt) > nums:
        return
    print(txt)
    fun(num+1)


global nums 
nums = int(input("Enter Number : "))
if nums < 0 :
    print("Only Positive & Zero Number ! ! !")
elif nums == 0 :
    print(nums)
else :
    fun(0)
