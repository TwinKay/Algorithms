'''
stack
'''
prt = []

T = int(input())
for t in range(1,T+1):
    S = list(input().rstrip())
    stack = []
    for s in S:
        if stack:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        else:
            stack.append(s)
    print(f'#{t} {len(stack)}')