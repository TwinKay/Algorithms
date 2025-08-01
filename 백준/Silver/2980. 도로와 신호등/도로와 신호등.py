import sys

N,L = map(int, sys.stdin.readline().split())
L += 1

info_arr = []
for _ in range(L):
    info_arr.append([])

for n in range(N):
    D,R,G = map(int, sys.stdin.readline().split())
    info_arr[D] = [R,G]

time = 0
idx = 0
while True:
    if not info_arr[idx]: # 신호등 x
        idx += 1
        time += 1
    else:
        mod = time%sum(info_arr[idx])
        if mod < info_arr[idx][0]:  # 빨간불
            time += 1
        else:
            idx += 1
            time += 1

    if idx == L-1:
        break
print(time)