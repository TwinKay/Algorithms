import sys

n = int(input())
total = []

for i in range(n):
    a = int(sys.stdin.readline())
    total.append(a)

total.sort()

for i in total:
    print(i)