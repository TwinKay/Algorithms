'''
아이디어:
stack
'''

import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if stack:
        while stack:
            if stack[-1] <= n:
                stack.pop()
            else:
                break
        stack.append(n)
    else:
        stack.append(n)
print(len(stack))