import sys

k,n,m = map(int, sys.stdin.readline().split())

cnt = k*n-m

if cnt < 0:
    print(0)
else:
    print(cnt)