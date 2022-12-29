import sys

n = int(sys.stdin.readline())
for _ in range(n):
    a = sys.stdin.readline()
    l = list(map(int, sys.stdin.readline().split()))
    print(sum(l))