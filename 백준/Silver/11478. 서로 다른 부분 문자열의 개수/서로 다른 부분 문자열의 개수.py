import sys

s = sys.stdin.readline().strip()
l = len(s)

result = set()

for i in range(l):
    for j in range(i,l):
        result.add(s[i:j+1])

print(len(result))