# ให้น้องๆเขียน Binary Search โดยใช้ Recursive เพื่อหาว่ามีค่านั้นอยู่ใน list หรือไม่ ถ้าหากมีให้ตอบ True หากไม่มีให้ตอบ False

# ***** อธิบาย Input
# 1. ด้านซ้าย  จะเป็น list ของ Data
# 2. ด้านขวา   จะเป็นค่าที่เราต้องการจะหา

def bi_search(l, r, arr, x):
    if l > r :
        return False
    mid = (l+r)//2

    if arr[mid] == x:
        return True
    elif x > arr[mid]:
        return bi_search(mid+1, r, arr, x)
    else:
        return bi_search(l, mid-1, arr, x)




inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))