'''
잘라지는 영역 sort 후에 길이 구해서 영역 가로 세로 곱해서 구하기
중복해서 잘리는 지에 대한 설명이 없음 -> 일단 중복 처리는 하자
'''
import sys

M,N = map(int, sys.stdin.readline().split())
garo_cuts = [0,N]
sero_cuts = [0,M]
K = int(sys.stdin.readline())
for _ in range(K):
    is_sero,num = map(int, sys.stdin.readline().split())
    if is_sero:
        sero_cuts.append(num)
    else:
        garo_cuts.append(num)

sero_cuts = list(set(sero_cuts))
garo_cuts = list(set(garo_cuts))
sero_cuts.sort()
garo_cuts.sort()

max_val = -1
for i in range(len(garo_cuts)-1):
    for j in range(len(sero_cuts)-1):
        val = (garo_cuts[i+1]-garo_cuts[i]) * (sero_cuts[j+1]-sero_cuts[j])
        max_val = max(max_val, val)

print(max_val)