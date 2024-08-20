# # ให้นักศึกษาเขียนโปรแกรมภาษา Python โดยใช้ Function ในการแสดงตำแหน่งของ List ในตำแหน่งที่หารเลขใดๆลงตัว จาก String

# def mod_position(arr, s):
#     //Code Here

# Input ตำแหน่งที่แรกเป็นค่าใน String ที่นำเข้ามา

# Input ตำแหน่งที่สองเป็นตัวเลขที่ทำการบอกว่าจะแสดงที่ตำแหน่งที่หารตัวเลขนั้นๆลงตัว เช่นถ้าใส่เลข 3 และ String มีค่าเป็น ABCDEFG ก็จะแสดงตำแหน่งที่ 3 คือ C กับตำแหน่งที่ 6 คือ F 


print("*** Mod Position ***")
str, n = input('Enter Input : ').split(',')
str = " " + str
ans = []
for i in range(1, len(str)):
    if i%int(n) == 0:
        ans += str[i]

print(ans)
