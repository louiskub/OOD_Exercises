from stack_implement import Stack

s = input('Enter samakarn : ').split()
print(s)
stack = Stack()
cal = 0
for i in s:
    try :
        stack.push(int(i))
    except :
        num1 = stack.pop()
        num2 = stack.pop()
        if i == '+':
            cal = num2 + num1
        elif  i == '-':
            cal = num2 - num1
        elif i == '*':
            cal = num2 * num1
        elif i == '/':
            cal = num2 / num1
        stack.push(cal)
    print(i, cal, stack.lst, sep="\t\t")

print(stack.pop())
