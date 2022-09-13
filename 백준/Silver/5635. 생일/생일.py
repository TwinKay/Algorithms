# 힙으로 재밌게 풀어보기

import sys
import heapq

heap_1 = []
heap_2 = []

n = int(sys.stdin.readline())

for _ in range(n):
    a,b,c,d = sys.stdin.readline().split()
    b=int(b);c=int(c);d=int(d)
    heapq.heappush(heap_1, (-d,-c,-b,a))
    heapq.heappush(heap_2, (d,c,b,a))

print(heap_1[0][3])
print(heap_2[0][3])