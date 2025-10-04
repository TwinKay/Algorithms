import sys

l = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())

total = 0
for _ in range(N):
    B, L, S = sys.stdin.readline().split()
    B, S = int(B), int(S)
    L = float(L)

    if S >= 17 and L >= 2.0:
        total += l[B]

print(total)
