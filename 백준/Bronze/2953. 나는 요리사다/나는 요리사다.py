# 시험기간

import sys

res = []
for _ in range(5):
    l = list(map(int, sys.stdin.readline().split()))
    res.append(sum(l))
print(res.index(max(res))+1, max(res))