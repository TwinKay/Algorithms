import sys

l = []
for _ in range(3):
    l.append(int(sys.stdin.readline()))
l.sort()
print(l[1])