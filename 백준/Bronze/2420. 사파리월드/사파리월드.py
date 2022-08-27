import sys

a,b = map(int,sys.stdin.readline().split())
c = a-b
if c < 0:
    c = -c
print(c)