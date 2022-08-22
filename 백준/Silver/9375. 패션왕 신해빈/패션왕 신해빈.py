import sys

for _ in range(int(sys.stdin.readline())):

    n = int(sys.stdin.readline())
    count = []
    cloth = []

    for _ in range(n):
        a,b = sys.stdin.readline().split()

        if b not in cloth:
            cloth.append(b)
            count.append(1)

        else:
            count[cloth.index(b)] += 1

    x = 1
    for i in count:
        x *= i+1

    print(x-1)