import sys

while True:
    is_bal = True
    s = sys.stdin.readline().rstrip()
    if s == ".":
        break
    
    stack = []
    for c in s:
        if c in ["[","("]:
            stack.append(c)
        elif c == "]":
            if len(stack) == 0:
                is_bal=False
                break
            if (stack[-1]=="["):
                stack.pop()
            else:
                is_bal=False
                break
                
        elif c == ")":
            if len(stack) == 0:
                is_bal=False
                break
            if (stack[-1]=="("):
                stack.pop()
            else:
                is_bal=False
                break
                
    if len(stack)==0 and is_bal:
        print("yes")
    else:
        print("no")