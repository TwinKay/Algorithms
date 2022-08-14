import sys

total = [0] * 10000

for i in range(int(sys.stdin.readline())):
    total[int(sys.stdin.readline()) - 1] += 1

for i, j in enumerate(total):
    if j != 0:
        for k in range(j):
            print(i + 1)