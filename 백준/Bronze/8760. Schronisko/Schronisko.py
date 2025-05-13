import sys

input = sys.stdin.readline
Z = int(input())
for _ in range(Z):
    W, K = map(int, input().split())
    print((W * K) // 2)
