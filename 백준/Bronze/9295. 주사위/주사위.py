import sys

T = int(sys.stdin.readline())
for t in range(T):
    a,b = map(int, sys.stdin.readline().split())
    print("Case ",end="")
    print(t+1,end="")
    print(": ",end="")
    print(a+b)