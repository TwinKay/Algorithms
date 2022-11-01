# 풀이 참고.. 다시 풀어볼 것..!
import sys
import heapq

n = int(sys.stdin.readline())

lec = []
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    lec.append([a,b])
lec.sort()

heap = []
heapq.heappush(heap, lec[0][1])

for i in range(1, n):
    if lec[i][0] < heap[0]:
        heapq.heappush(heap, lec[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, lec[i][1])

print(len(heap))