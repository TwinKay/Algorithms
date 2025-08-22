'''
bisect 사용해보기
'''
import sys
from bisect import bisect_left

M,N,L = map(int, sys.stdin.readline().split())
base_idxs = list(map(int, sys.stdin.readline().split()))
target_idxs = []
for _ in range(N):
    target_idxs.append(list(map(int, sys.stdin.readline().split())))

base_idxs.sort()

cnt = 0
for target_idx in target_idxs:
    x,y = target_idx
    dist = L - y # y 제외하고 남은 거리
    if dist < 0:
        continue  # y가 L보다 크면 못 맞춤

    left = x - dist
    right = x + dist

    i = bisect_left(base_idxs, left) # left 이상인 가장 왼쪽 사대 index

    # i가 범위 내이고(bisect_left은 없을 때 마지막 index+1),
    # 또한 사대가 right 이내면 사정거리 안
    if i < M and base_idxs[i] <= right:
        cnt += 1

print(cnt)