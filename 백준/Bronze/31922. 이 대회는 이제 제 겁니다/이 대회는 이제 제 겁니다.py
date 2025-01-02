import sys

a,b,c = map(int, sys.stdin.readline().split())
if a+c>b:
    print(a+c)
else:
    print(b)