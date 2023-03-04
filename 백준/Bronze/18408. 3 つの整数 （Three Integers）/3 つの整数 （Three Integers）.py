import sys
l = list(map(int, sys.stdin.readline().split()))
c = l.count(1)
if c >=2:
    print(1)
else:
    print(2)