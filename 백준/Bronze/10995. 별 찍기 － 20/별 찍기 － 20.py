# 시험기간

import sys

n = int(sys.stdin.readline())

l = ['*']
for i in range(n-1):
    l.append('*')

for i in range(n):
    if i%2 == 0:
        print(' '.join(l))
    else:
        print(' '+' '.join(l))