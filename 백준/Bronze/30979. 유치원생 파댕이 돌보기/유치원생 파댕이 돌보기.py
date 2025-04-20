import sys

T = int(sys.stdin.readline())
N = int(sys.stdin.readline())
F = list(map(int, sys.stdin.readline().split()))

if sum(F) >= T:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")
