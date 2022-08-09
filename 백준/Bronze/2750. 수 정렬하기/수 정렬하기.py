import sys

n = int(sys.stdin.readline())
result = []
for i in range(n):
    result.append(int(sys.stdin.readline()))
result.sort()

for j in result:
    print(j)