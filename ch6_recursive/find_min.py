def recur(i, lst):
    if i == len(lst)-1:
        return lst[i]
    else :
        next_val = recur(i+1, lst)
        return min(lst[i], next_val)
    

