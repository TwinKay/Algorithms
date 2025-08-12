'''
아이디어:
heap arr를 만들어서 해결
-> heap arr의 각 heap은 해당 초밥 type을 원하는 사람들의 idx를 인자로 갖는다
'''
import sys
from heapq import heappush,heappop

SUSHI_MAX_TYPE = 200_001 # 초밥의 종류
N,M = map(int, sys.stdin.readline().split())
pq_arr = []
for _ in range(SUSHI_MAX_TYPE):
    pq_arr.append([])

for i in range(N):
    sushi_info = list(map(int, sys.stdin.readline().split()))
    for j in range(1,len(sushi_info)): # 첫번째는 갯수
        heappush(pq_arr[sushi_info[j]],i) # 초밥 pq에 사람 idx 넣기

res_arr = [0]*N
sushies = list(map(int, sys.stdin.readline().split()))
for sushi in sushies:
    if pq_arr[sushi]: # 없다면 초밥 버리기
        s = heappop(pq_arr[sushi])
        res_arr[s] += 1
print(*res_arr)