def recur(n):
    if n == 0:
        print("end")
        return
    print(n)
    recur(n-1)
    
def recur_depth_first(n):
    if n == 0:
        print("end")
        return
    recur_depth_first(n-1)
    print(n)

# recur(3)
# recur_depth_first(1)

def stair(i, n):    # 0 10
    if i == n:
        return
    
    if n > 0 :
        print("_"*(n-i-1) + "#"*(i+1) )
        stair(i+1, n)

    elif n < 0 :
        stair(i-1, n)
        j, k = abs(i), abs(n)
        print("_"*(k-j-1) + "#"*(j+1) )

stair(0, 4)
print()
stair(0, -4)


