'''
미리 만들고 쿼리에서는 출력만
'''
prt = []

def is_right(S):
    stack = []
    for s in S:
        if s == '{':
            stack.append(s)
        elif s == '(':
            stack.append(s)
        elif s == '}':
            if len(stack) == 0:
                return False
            if stack[-1] == '(':
                return False
            stack.pop()
        elif s == ')':
            if len(stack) == 0:
                return False
            if stack[-1] == '{':
                return False
            stack.pop()
    if len(stack) != 0:
        return False
    return True

T = int(input())
for t in range(1,T+1):
    S = input().rstrip()
    if is_right(S):
        print(f"#{t} {1}")
    else:
        print(f"#{t} {0}")

