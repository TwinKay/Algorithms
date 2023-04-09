import sys

a,b,c= map(int, sys.stdin.readline().split())
if (b-a)%c == 0:
    print((b-a)//c)
else:
    print((b-a)//c+1)
