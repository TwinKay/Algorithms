# 시험기간

import sys

n = int(sys.stdin.readline())

for i in range(n):
    if i == 0:
        print(' '*(n-i-1),end='')
        print('*')
    else:
         print(' '*(n-i-1),end='')
         print('*', end='')
         print(' '*(2*i-1), end='')
         print('*')