import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    for i in range(n):
        a,b = map(int,sys.stdin.readline().split())
        print(a+b,a*b)