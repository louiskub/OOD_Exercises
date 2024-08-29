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



def post2inf(lst):
    s = Stack()
    for char in lst:
        if char not in "+-*/":
            s.push(char)
        else :
            temp = f"({s.pop()}{char}{s.pop()})"
            s.push(temp)
    print(s.pop())



def postcal(lst):
    stack = Stack()
    for char in lst:
        try :
            stack.push(int(char))
        except:
            num1 = stack.pop()
            num2 = stack.pop()
            if char == "+":
                stack.push(num1+num2)
            elif char == "-":
                stack.push(num2-num1)
            elif char == "*":
                stack.push(num1*num2)
            elif char == "/":
                stack.push(num2/num1)
        print(char, stack.peek(), stack.lst, sep="\t\t")
    print(stack.pop())


if __name__ == "__main__":
    inp = list(input("Infix : "))
    print(inp)
    inf2post(inp)

    # inp = list(input("Postfix : "))
    # print(inp)
    # post2inf(inp)

    # inp = input("Postfix Cal : ").split()
    # print(inp)
    # postcal(inp)