import sys

N, M, K = map(int, sys.stdin.readline().split())
result = min(M, K) + min(N - M, N - K)
print(result)