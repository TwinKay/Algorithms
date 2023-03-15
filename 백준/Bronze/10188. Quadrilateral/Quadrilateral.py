import sys

n = int(sys.stdin.readline())
for j in range(n):
    a,b = map(int, sys.stdin.readline().split())
    for i in range(b):
        print('X'*a)
    if j != n-1:
        print('')