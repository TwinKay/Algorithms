# 시험기간

import sys

l = []
for _ in range(7):
    a = int(sys.stdin.readline())
    if a%2 == 1:
        l.append(a)

if len(l) == 0:
    print(-1)
else:
    print(sum(l))
    print(min(l))