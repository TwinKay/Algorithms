# dict 이용
import sys

n = int(sys.stdin.readline())
total = {}

for _ in range(n):
    a = sys.stdin.readline().rstrip()

    if a in total.keys():
        total[a] += 1

    else:
        total[a] = 1

m = max(total.values())
max_values = []

for k,v in total.items():
    if v == m:
        max_values.append(k)

max_values.sort()
print(max_values[0])