import sys

a = int(sys.stdin.readline())
b,c = map(int, sys.stdin.readline().split())
if a<=(b/c):
    print(1)
else:
    print(0)