import sys

total = []
for _ in range(int(sys.stdin.readline())):
    a,b = map(int, sys.stdin.readline().strip().split())
    total.append([a,b])

total = sorted(total, key=lambda x: x[0])
total = sorted(total, key=lambda x: x[1])

clock = 0
t = 0

for i in total:
    if i[0] >= clock:
        clock = i[1]
        t += 1

print(t)