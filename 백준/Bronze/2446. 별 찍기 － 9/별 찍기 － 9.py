# 시험기간

import sys

n = int(sys.stdin.readline())

for i in range(n):
    print(' '*i, end='')
    print('*' * (2 * (n - i) - 1))

for i in range(n-1):
    print(' '*(n-i-2), end='')
    print('*'*(2*(i+1)+1))