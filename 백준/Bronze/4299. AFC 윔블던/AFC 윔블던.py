import sys

data = sys.stdin.readline().split()
S = int(data[0])
D = int(data[1])

if S < D or (S + D) % 2 != 0:
    print(-1)
else:
    x = (S + D) // 2
    y = (S - D) // 2
    if y < 0:
        print(-1)
    else:
        print(x, y)
