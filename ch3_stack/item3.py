# จงเขียนโปรแกรมโดยใช้ Stack เพื่อคำนวณหา ค่าของนิพจน์แบบ postfix 

# โดยให้แสดงผลลัพธ์ตามตัวอย่าง


print(" ***Postfix expression calcuation***")
# s = input('Enter Postfix expression : ').split()
s = [e if e in "+-*/" else int(e) for e in input('Enter Postfix expression : ').split()]
stack = []
cal = 0
for i in s:

    if not isinstance(i, str):
        stack.append(i)
    else :
        num1 = stack.pop()
        num2 = stack.pop()
        if i == '+':
            cal = num1 + num2
        elif i == '-':
            cal = num2 - num1
        elif i == '*':
            cal = num1 * num2
        elif i == '/':
            cal = num2 / num1
        stack.append(cal)
    # print(cal, stack)

print(f"Answer :  {cal:.2f}")
