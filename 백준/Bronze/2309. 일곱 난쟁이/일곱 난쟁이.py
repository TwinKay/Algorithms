import sys

nan = []
for _ in range(9):
    nan.append(int(sys.stdin.readline()))

total = sum(nan)

for i in range(9):
    for j in range(9):
        if i<j:
            if total - nan[i] - nan[j] == 100:
                res = [i,j]
temp = []
for i in range(9):
    if i not in res:
        temp.append(nan[i])

temp.sort()
for i in temp:
    print(i)