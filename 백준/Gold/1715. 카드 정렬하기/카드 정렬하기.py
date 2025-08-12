'''
아이디어:
heap을 통한 제일 작은 두 수 꺼내기
'''
import sys
from heapq import heappush,heappop

N = int(sys.stdin.readline())
pq = []
for _ in range(N):
    heappush(pq,int(sys.stdin.readline()))

res = 0
for _ in range(N-1): # N-1만 반복
    temp = heappop(pq)+heappop(pq)
    res += temp
    heappush(pq, temp)
    
print(res)
