import sys

N, X = map(int, sys.stdin.readline().split())
latest_start = -1

for _ in range(N):
    S, T = map(int, input().split())
    if S + T <= X:
        latest_start = max(latest_start, S)

print(latest_start)
