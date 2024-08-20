# อยากให้นักศึกษาช่วยหาลำดับการ Countdown จาก Input ที่รับเข้ามา โดยลำดับการ Countdown จะเป็นเลขเรียงลำดับ เช่น 2->1 , 3->2->1 โดยจะสิ้นสุดด้วย 1 เสมอ
#     โดยผลลัพธ์ให้แสดง List ของ จำนวนลำดับที่เจอ และ แต่ละลำดับเป็นอย่างไร

# *** Fun with countdown ***
# Enter List : 4 8 3 2 1 2
# [1, [[3, 2, 1]]]

def fun(lst):
    n = len(lst)
    ans = [0, []]
    for i in range(n):
        if lst[i] == 1:
            temp = [1]
            # ans[1].append([1])
            lst[i] = 1
            for j in range(i-1, -1, -1):
                if lst[j] == 1 + lst[j+1]:
                    temp.insert(0, lst[j])
                else :
                    break
            ans[1].append(temp)
            # print(temp)
    ans[0] = len(ans[1])
    return ans





print("*** Fun with countdown ***")
lst = [int(i) for i in input('Enter List : ').split()]
print(fun(lst))


