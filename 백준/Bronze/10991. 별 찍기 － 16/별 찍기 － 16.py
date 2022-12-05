# 시험기간

import sys

n = int(sys.stdin.readline())

for i in range(n):
    print(' '*(n-i-1), end='')
    l = ['*']*(i+1)
    print(' '.join(l))