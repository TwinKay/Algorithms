import sys

apt = [list(range(1,15))]
for i in range(14):
    temp = []
    sum = 0
    for j in range(14):
        sum += apt[-1][j]
        temp.append(sum)
    apt.append(temp)

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    print(apt[K][N-1])