import sys

n,m = map(int, sys.stdin.readline().split())

total_1 = {}
total_2 = {}
for i in range(n):
    a = sys.stdin.readline().strip()
    total_1[str(i+1)] = a
    total_2[a] = str(i+1)

for _ in range(m):
    x = sys.stdin.readline().strip()

    if x .isdigit() == True:
        print(total_1[x])
    else:
        print(total_2[x])