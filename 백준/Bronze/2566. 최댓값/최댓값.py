import sys

l = []
for _ in range(9):
    l.append(list(map(int, sys.stdin.readline().split())))

m = 0
for i in l:
    m = max(m, max(i))
print(m)
for j,i in enumerate(l):
    if m in i:
        print(j+1, i.index(m)+1)