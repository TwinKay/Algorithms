# 시험기간

import sys

n = int(sys.stdin.readline())

l = ['*']
for i in range((n-1)//2):
    l.append('*')

for i in range(n):
    if n % 2 == 1:
        print(' '.join(l))
        print(' ' + ' '.join(l[1:]))
    if n % 2 == 0:
        print(' '.join(l))
        print(' '+' '.join(l))