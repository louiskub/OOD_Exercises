# ให้น้องรับ input มา 2 อย่างโดยคั่นด้วย /

# 1. ด้านซ้าย เป็นผลลัพธ์
# 2. ด้านขวา เป็น list ของจำนวนเต็ม

# โดยผลลัพธ์ให้แสดงเป็น subset ของ input ด้านขวาที่มีผลรวมได้เท่ากับ input ด้านซ้าย และมี Pattern การแสดงผลลัพธ์ดังนี้

# 1. ให้เรียงลำดับจากขนาดของ subset จากน้อยไปมาก
# 2. ถ้าหาก subset มีขนาดเท่ากันให้เรียงลำดับจำนวนเต็มใน subset จากน้อยไปมาก

# ถ้าหากไม่มี subset ไหนที่ผลรวมเท่ากับ input ด้านซ้าย ให้แสดงว่า No Subset



# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import

# อธิบาย Test Case 1:
# Enter Input : 2/-2 3 1 -1 0 -3 2
# [2]
# [-1, 3]
# [0, 2]
# [-3, 2, 3]
# [-2, 1, 3]
# [-1, 0, 3]
# [-1, 1, 2]
# [-3, 0, 2, 3]
# [-2, -1, 2, 3]
# [-2, 0, 1, 3]
# [-1, 0, 1, 2]
# [-3, -1, 1, 2, 3]
# [-2, -1, 0, 2, 3]
# [-3, -1, 0, 1, 2, 3]



def find_subset(lst, s):
    subset = [[]]
    for num in lst:
        new_subset = [sub+[num] for sub in subset]
        subset.extend(new_subset)

    subset = find_ans(subset, s)
    subset = subset_sort(subset)
    if not subset:
        print("No Subset")
    else:
        # print("\n\n")
        for i in subset:
            print(i)

def bubble(inp):
    for i in range(len(inp)):
        swapped = False
        for j in range(len(inp)-i-1):
            if inp[j] > inp[j+1]:
                swapped = True
                inp[j], inp[j+1] = inp[j+1], inp[j]
        
        if not swapped:
            break
    return inp

def find_ans(subsets, num):
    ans = []
    for subset in subsets:
        if sum(subset) == num:
            ans.append(subset)
    return ans

def subset_sort(inp):
    for i in range(len(inp)):
        inp[i] = bubble(inp[i])


    for i in range(len(inp)):
        swapped = False
        for j in range(len(inp)-i-1):
            if compare(inp[j], inp[j+1]):
            # if len(inp[j]) > len(inp[j+1]) or (len(inp[j]) == len(inp[j+1] and inp[j][0] > inp[j+1][0]):
                swapped = True
                inp[j], inp[j+1] = inp[j+1], inp[j]
                # print(inp[j+1], inp[j])
        
        if not swapped:
            break
    return inp

def compare(lst1, lst2):
    if len(lst1) > len(lst2):
        return True
    if len(lst1) == len(lst2):
        for i in range(len(lst1)):
            if lst1[i] > lst2[i]:
                # print(f"{lst1}    {lst2}     {i}")
                return True
            if lst1[i] < lst2[i]:
                return False
    return False

num, inp = input('Enter Input : ').split('/')
num = int(num)
inp = [int(e) for e in inp.split()]
# print(num)
# print(inp)
# print("\n\n")
find_subset(inp, num)


