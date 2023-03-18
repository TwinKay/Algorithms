import sys
import heapq as hq

n = int(sys.stdin.readline())
heap = []

l = list(map(int, sys.stdin.readline().split()))
for i in l:
    hq.heappush(heap, i)

for _ in range(n-1):
    l = list(map(int, sys.stdin.readline().split()))
    for i in l:
        if i > heap[0]:
            hq.heappop(heap)
            hq.heappush(heap, i)
print(heap[0])