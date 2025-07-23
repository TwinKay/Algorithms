import sys

L = int(sys.stdin.readline())
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

want_num = -1
want_cnt = -1

for i in range(N):
    a,b = arr[i]
    if b-a > want_cnt:
        want_cnt = b-a
        want_num = i+1

print(want_num)


cake = list([0]*L)
for i in range(N):
    a,b = arr[i]

    for j in range(a-1,b):
        if cake[j] == 0:
            cake[j] = i+1

cnt_arr = [0]*(N+1)
for i in cake:
    if i != 0:
        cnt_arr[i] += 1

max_value= -1
max_idx = -1

for i in range(1,N+1):
    if cnt_arr[i] > max_value:
        max_value = cnt_arr[i]
        max_idx = i

print(max_idx)
