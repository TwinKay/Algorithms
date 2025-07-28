'''
아이디어:
stack
'''
res = []

import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
target = 0
stack = []
for i in range(1,N+1):
    while stack:
        if stack[-1] == arr[target]:
            stack.pop()
            res.append('-')
            target += 1
        else:
            break
    stack.append(i)
    res.append('+')
is_res = True
for s in stack[::-1]:
    if s != arr[target]:
        is_res = False
    target += 1
    res.append('-')
if is_res:
    print("\n".join(res))
else:
    print("NO")