# 시험기간
import sys

n,m = map(int, sys.stdin.readline().split())

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    new = []
    for i in range(m):
        new.append(s[m-i-1])
    print(''.join(new))