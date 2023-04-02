import sys

l = []
a,b,c = map(int, sys.stdin.readline().split())
if a >= b and a <= c:
    print(a)
elif a > c:
    print(c)
else:
    print(b)