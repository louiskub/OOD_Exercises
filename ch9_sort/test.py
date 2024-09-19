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
    # Sort elements inside each subset using bubble sort
    for i in range(len(inp)):
        inp[i] = bubble(inp[i])

    # Sort subsets first by length, then lexicographically
    for i in range(len(inp)):
        swapped = False
        for j in range(len(inp)-i-1):
            if len(inp[j]) > len(inp[j+1]) or (len(inp[j]) == len(inp[j+1]) and \
                (inp[j] > inp[j+1] or (inp[j] == inp[j+1] and ))):
                swapped = True
                inp[j], inp[j+1] = inp[j+1], inp[j]
        
        if not swapped:
            break
    return inp

# Input parsing and function call
num, inp = input('Enter Input : ').split('/')
num = int(num)
inp = [int(e) for e in inp.split()]

find_subset(inp, num)
