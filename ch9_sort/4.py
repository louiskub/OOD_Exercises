def median(lst):
    if not lst:
        return
    n = len(lst)
    # print(n//2)
    if n%2 == 1:
        ans = lst[n//2]
    else :
        ans = (lst[n//2] + lst[(n//2)-1])/2
    print(f'median = {ans:.1f}')

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "xxx"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    #code here
sorted = []
for i in range(len(l)):
    k = 0
    while k < len(sorted):
        if l[i]<sorted[k]:
            break
        k += 1
    sorted.insert(k, l[i])
    print(f"list = {l[:i+1]} : ", end="")
    median(sorted)
