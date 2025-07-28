'''
stack
'''

T = 10
for t in range(1,T+1):
    N,S = input().split()
    stack = []
    for s in S:
        if stack:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        else:
            stack.append(s)
    print(f'#{t} {"".join(stack)}')