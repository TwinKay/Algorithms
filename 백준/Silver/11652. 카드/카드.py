import sys
import heapq

n = int(sys.stdin.readline())
total = {}

for _ in range(n):
    a = int(sys.stdin.readline())
    if a in total.keys():
        total[a] += 1
    else:
        total[a] = 1

result = []
for k,v in total.items():
    heapq.heappush(result, (-v,k))

print(result[0][1])