# 시험기간

import sys

res = 0
n = int(sys.stdin.readline())
for _ in range(n):
    a,b = sys.stdin.readline().split('-')
    b = int(b)
    if b <= 90:
        res += 1
print(res)