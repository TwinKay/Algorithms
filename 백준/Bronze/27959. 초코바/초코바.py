import sys
a,b = map(int,sys.stdin.readline().split())
if a*100>=b:
    print('Yes')
else:
    print('No')