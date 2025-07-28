'''
아이디어:
stack
'''

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
res = []
for a in arr[::-1]:
    if stack:
        while stack:
            if stack[-1] <= a:
                stack.pop()
            else:
                break

        if stack:
            res.append(stack[-1])
            stack.append(a)
        else:
            res.append(-1)
            stack.append(a)

    else:
        res.append(-1)
        stack.append(a)

# res도 거꾸로
print(*res[::-1])
