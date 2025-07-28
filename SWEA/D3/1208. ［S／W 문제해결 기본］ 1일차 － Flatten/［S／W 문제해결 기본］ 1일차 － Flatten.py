# 우선순위 큐를 통한 flat
# 높이가 음수로 잠시 되어도 괜찮음

import heapq as hq

T = 10
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_heap = []
    for a in arr:
        hq.heappush(max_heap, [-a,a]) # max heap 구현을 위함, 보통 튜플로 사용

    for _ in range(N):
        temp = hq.heappop(max_heap)[1]
        hq.heappush(max_heap, [1-temp,temp-1]) # N만큼 위에서 한개씩 제거 후 재삽입

    min_heap = []
    for i in max_heap:
        hq.heappush(min_heap, i[1]) # max heap에서 min heap 변환

    for _ in range(N):
        temp = hq.heappop(min_heap)
        hq.heappush(min_heap, temp+1) # N만큼 위에서 한개씩 추가 후 재삽입

    print(f'#{t} {max(min_heap)-min(min_heap)}')

