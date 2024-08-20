from stack_implement import Stack, Queue

def prec(c):
    if c == "^":
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else :
        return -1
        

def inf2post(lst):
    stack = Stack()
    ans = ""
    for i in lst:
        if i.isalpha() or i.isnumeric():
            ans += str(i)
        elif i == '(':
            stack.push(i)
        elif i == ')':
            while not stack.isEmpty() and stack.peek()!='(':
                ans += str(stack.pop())
            stack.pop()
        else :
            while not stack.isEmpty() and prec(i) <= prec(stack.peek()):
                ans += str(stack.pop())
            stack.push(i)
    while not stack.isEmpty():
        ans += str(stack.pop())
    print(ans)


inp = list(input("Infix : "))
print(inp)
inf2post(inp)
