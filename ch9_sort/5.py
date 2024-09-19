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


