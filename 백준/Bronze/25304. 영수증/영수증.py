import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
total_price = 0
for _ in range(N):
    a,b = map(int, sys.stdin.readline().split())
    total_price += a*b
if X==total_price:
    print("Yes")
else:
    print("No")