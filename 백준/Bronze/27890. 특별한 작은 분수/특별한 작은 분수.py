import sys

x, N = map(int, sys.stdin.readline().split())
for _ in range(N):
    if x % 2 == 0:
        x = (x // 2) ^ 6
    else:
        x = (x * 2) ^ 6
print(x)