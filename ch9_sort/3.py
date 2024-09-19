def insertion(inp, typ):
    # symbol = "CDHS"
    # num = "23456789TJQKA"
    compare = ["CDHS", "23456789TJQKA"]
    swapped = False
    # dup = set()
    i = -1
    while i+1 < len(inp):
        i += 1
        # print(inp[i])
        if inp[i][0] not in compare[0] or \
            inp[i][1] not in compare[1] or len(inp[i]) > 2:
                print(f'Error: {inp[i]} is an invalid card')
                inp.pop(i)
                i -= 1
                continue
        # if inp[i] in dup:
        #     print(f'Error: Duplicate card found - {inp[i]}')
        #     i -= 1
        #     continue
        # dup.add(inp[i])
        for j in range(i, 0, -1):
            if inp[j] == inp[j-1]:
                print(f'Error: Duplicate card found - {inp[j]}')
                inp.pop(j)
                i -= 1
                break
            if compare[typ].index(inp[j][typ]) < compare[typ].index(inp[j-1][typ]) or\
                (compare[typ].index(inp[j][typ]) == compare[typ].index(inp[j-1][typ]) and \
                 compare[not typ].index(inp[j][not typ]) < compare[not typ].index(inp[j-1][not typ])):
                swapped = True
                inp[j], inp[j-1] = inp[j-1], inp[j]
            else:
                break
    # print(inp)
    if swapped:
        print("Sorted cards : ", end="")
        print(" ".join(inp))
    else :
        print("No valid cards to sort.")
        
    


print("Have fun with sort card")
inp, typ = input('Enter Input: ').split('/')
inp = inp.split(',')
if typ and inp:
    typ = 0 if typ[0] == "s" else 1
    sorted = insertion(inp, typ)
else :
    print("No valid cards to sort.")

