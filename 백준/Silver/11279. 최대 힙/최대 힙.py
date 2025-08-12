'''
아이디어:
튜플을 통한 max heap 구현
'''
import sys
from heapq import heappush,heappop

N = int(sys.stdin.readline())
pq = []
for _ in range(N):
    query = int(sys.stdin.readline())
    if query != 0: # 출력하는 경우
        heappush(pq, (-query,query)) # 음수 기준
    else:
        if len(pq) == 0:
            print(0)
        else:
            print(heappop(pq)[1])

