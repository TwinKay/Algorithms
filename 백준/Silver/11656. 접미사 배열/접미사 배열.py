import sys

s = sys.stdin.readline().rstrip()

total = []
for i in range(len(s)):
     total.append(s[i:])

total.sort()

for i in total:
    print(i)