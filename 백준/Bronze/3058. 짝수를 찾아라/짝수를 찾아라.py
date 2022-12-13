# 시험기간

import sys

for _ in range(int(sys.stdin.readline())):
    l = list(map(int, sys.stdin.readline().split()))
    res = []
    for i in l:
        if i%2 == 0:
            res.append(i)

    print(sum(res), end=' ')
    print(min(res))