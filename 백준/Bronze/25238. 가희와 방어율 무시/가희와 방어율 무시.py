import sys
a,b = map(int, sys.stdin.readline().split())
c = a*(100-b)*0.01
if c >= 100:
    print(0)
else:
    print(1)