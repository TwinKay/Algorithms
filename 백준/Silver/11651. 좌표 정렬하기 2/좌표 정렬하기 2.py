import sys

n = int(sys.stdin.readline())
total = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    total.append([b, a])

total.sort()

for i in range(n):
    print(total[i][1], total[i][0])