# 시험기간

import sys

a,b,c = map(int, sys.stdin.readline().split('/'))

if a+c<b or b==0:
    print('hasu')
else:
    print('gosu')