import sys

n, score, p = map(int, sys.stdin.readline().split())

if n == 0:
    print(1)
else:
    total = list(map(int,sys.stdin.readline().split()))

    if n == p and score <= total[-1]:
        print(-1)
    else:
        total.append(score)
        total.sort(reverse=True)

        print(total.index(score)+1)