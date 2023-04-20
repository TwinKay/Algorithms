import sys
n = int(sys.stdin.readline())
for _ in range(n):
    a,b,c = map(int, sys.stdin.readline().split())
    if b >= c:
        print(0)
    else:
        if a == 1:
            a = 1
        elif a == 2:
            a = 3
        else:
            a = 5
        print((c-b)*a)