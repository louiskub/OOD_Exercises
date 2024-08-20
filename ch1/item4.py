# เขียนภาษา Python เพื่อวาดรูปหัวใจ ซึ่งจะรับ input เป็นขนาดของรูปหัวใจ โดย input จะมีค่าตั้งแต่ 2 ขึ้นไป
# *** Fun with Drawing ***
# Enter input : 5
# ....*.......*....
# ...*+*.....*+*...
# ..*+++*...*+++*..
# .*+++++*.*+++++*.
# *+++++++*+++++++*
# .*+++++++++++++*.
# ..*+++++++++++*..
# ...*+++++++++*...
# ....*+++++++*....
# .....*+++++*.....
# ......*+++*......
# .......*+*.......
# ........*........


print("*** Fun with Drawing ***")
n = int(input('Enter input : '))
rows = (3*n)-2
cols = (4*n)-3 
for row in range(1, rows+1):
    for col in range(1, cols+1):
        if row <=n and (col == n+(row-1) or col == n-(row-1) or 
                        col == 3*n-2+(row-1) or col == 3*n-2-(row-1)):
            print("*", end="")
        elif row >= n and (col == row-n+1 or col ==cols-(row-n)):
            print('*', end="")
        elif row <=n and ((col > n-row+1 and col < n+row-1) or 
                        (col > 3*n-2-row+1) and col < 3*n-2+(row-1)):
            print('+', end="")
        elif row >= n and col > row-n+1 and col < cols-(row-n):
            print('+', end="")
        else :
            print('.', end="")


    print('')