import sys

for _ in range(3):
    n = int(sys.stdin.readline())
    res = 0
    for _ in range(n):
        res += int(sys.stdin.readline())

    if res == 0:
        print(0)
    elif res > 0:
        print('+')
    else:
        print('-')