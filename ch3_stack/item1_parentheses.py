# ให้น้องๆเขียนโปรแกรมรับ input เป็นวงเล็บ โดยมีรูปแบบดังนี้  วงเล็บเปิด :  (  กับ  [    วงเล็บปิด :  )  กับ  ]   โดยให้หาว่าถ้าหากนำวงเล็บมาจับคู่กัน จะครบทุกคู่หรือไม่  โดยให้แสดงผลลัพธ์ออกมาเป็นจำนวนวงเล็บที่จะต้องเติมหากวงเล็บมีไม่ครบคู่   แต่ถ้าหากครบคู่ให้แสดงคำว่า  Perfect  ออกมาด้วย


s = input('Enter Input : ')
stack = []
ans = 0
for letter in s:
    if letter in '([{' :
        stack.append(letter)
        
    elif letter in ')]}': 
        if not stack:
            ans += 1
            continue
        temp = stack[-1] + letter
        if temp in '()[]{}':
            stack.pop()
        else :
            ans += 1
            
        # else 

if ans or stack:
    print(ans+len(stack))
else :
    print(0)
    print("Perfect ! ! !")