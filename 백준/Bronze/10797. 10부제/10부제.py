import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in l:
    if i == n:
        cnt += 1
print(cnt)