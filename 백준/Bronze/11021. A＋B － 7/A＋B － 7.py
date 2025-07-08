import sys

T = int(sys.stdin.readline())
for t in range(1,T+1):
    a,b = map(int, sys.stdin.readline().split())
    print(f'Case #{t}: {a+b}')