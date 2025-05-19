import sys

input = sys.stdin.readline
K = int(input())
for t in range(1, K+1):
    n, s, d = map(int, input().split())
    max_dist = s * d
    total = 0
    for _ in range(n):
        di, vi = map(int, input().split())
        if di <= max_dist:
            total += vi
    print(f"Data Set {t}:")
    print(total)
    print()