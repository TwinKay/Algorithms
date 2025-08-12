'''
아이디어:
튜플을 통한 abs heap 구현
+ 음수가 더 높은 순위
'''
import sys
from heapq import heappush,heappop

N = int(sys.stdin.readline())
pq = []
for _ in range(N):
    query = int(sys.stdin.readline())
    if query != 0: # 출력하는 경우
        heappush(pq, (abs(query),query)) # 절대값, 동일 시 자동으로 음수부터
    else:
        if len(pq) == 0:
            print(0)
        else:
            print(heappop(pq)[1])

