# 시험기간

import sys

res = 0
while True:
    a = int(sys.stdin.readline())
    if a == -1:
        break
    else:
        res += a

print(res)