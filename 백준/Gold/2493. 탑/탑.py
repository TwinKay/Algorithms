'''
아이디어:
stack 및 index 저장을 통한 해결
'''

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

stack = []
res = []
for idx,a in enumerate(arr):
    idx += 1
    if stack:
        while stack:
            if stack[-1][0] < a:
                stack.pop()
            else:
                break
        if stack:
            res.append(stack[-1][1])
            stack.append([a,idx])
        else:
            stack.append([a,idx])
            res.append(0)
    else:
        stack.append([a,idx])
        res.append(0)
print(*res)