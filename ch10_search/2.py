def bi_search(l, r, arr, x):
    if l >= len(arr):
        return "No First Greater Value"
    if l > r :
        return arr[r+1]
    mid = (l+r)//2
    if arr[mid] == x:
        return arr[mid+1]
    elif x > arr[mid]:
        return bi_search(mid+1, r, arr, x)
    else:
        return bi_search(l, mid-1, arr, x)


inp = input('Enter Input : ').split('/')
arr, kk = sorted(list(map(int, inp[0].split()))), list(map(int, inp[1].split()))
# print(arr)
for k in kk:
    print(bi_search(0, len(arr) - 1, arr, k))