import sys

n = int(sys.stdin.readline())
ans = float('inf')
for _ in range(n):
    a, b = map(int, input().split())
    if a <= b and b < ans:
        ans = b
print(ans if ans != float('inf') else -1)