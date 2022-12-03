# 시험기간

import sys

n = int(sys.stdin.readline())

for i in range(n):
    print('*'*(i+1), end='')
    print('')

for i in range(n-1):
    print('*'*(n-i-1), end='')
    print('')