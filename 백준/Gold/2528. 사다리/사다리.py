'''
시뮬레이션
막대기 길이와 땅의 길이가 같을 수도 있음

'''

import sys

N, L = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    l, d = map(int, sys.stdin.readline().split())
    if d == 0:
        arr.append([0, l, 'R'])
    else:
        arr.append([L - l, L, 'L'])

time = 0
height = 0
is_end = False
while True:
    if N == 1: break
    # 올라가기
    while True:
        if arr[height + 1][0] <= arr[height][0] <= arr[height + 1][1] \
                or arr[height + 1][0] <= arr[height][1] <= arr[height + 1][1] \
                or arr[height][0] <= arr[height + 1][0] <= arr[height][1] \
                or arr[height][0] <= arr[height + 1][1] <= arr[height][1]:
            height += 1
            if height == N - 1:
                is_end = True
                break
        else:
            break

    if is_end: break
    # 막대기 이동
    for h in range(height, N):
        if arr[h][0] == 0 and arr[h][1] == L: continue
        if arr[h][2] == 'L':
            if arr[h][0] == 0:
                arr[h] = [arr[h][0] + 1, arr[h][1] + 1, 'R']
            else:
                arr[h] = [arr[h][0] - 1, arr[h][1] - 1, 'L']
        else:
            if arr[h][1] == L:
                arr[h] = [arr[h][0] - 1, arr[h][1] - 1, 'L']
            else:
                arr[h] = [arr[h][0] + 1, arr[h][1] + 1, 'R']

    time += 1

print(time)
