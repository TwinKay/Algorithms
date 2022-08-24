import sys

n = int(sys.stdin.readline())
if n % 5 == 1:
    if n == 1:
        print(-1)
    else:
        print(n//5 + 2)
elif n % 5 == 2:
    print(n//5 + 1)
elif n % 5 == 3:
    if n == 3:
        print(-1)
    else:
        print(n//5 + 3)
elif n % 5 == 4:
    print(n//5 + 2)
else:
    print(n//5)
