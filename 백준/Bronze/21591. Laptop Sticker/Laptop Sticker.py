import sys
a,b,c,d = map(int,sys.stdin.readline().split())
if a-c>=2 and b-d>=2:
    print(1)
else:
    print(0)