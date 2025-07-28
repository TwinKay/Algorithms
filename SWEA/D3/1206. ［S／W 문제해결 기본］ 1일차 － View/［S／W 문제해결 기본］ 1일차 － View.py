T = 10
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range(2,N-2):
        min_num = 1000 # dummy
        for j in range(i-2,i+3):
            if j == i:
                continue
            if arr[i] - arr[j] < min_num:
                min_num = arr[i] - arr[j]

        if min_num > 0:
            cnt += min_num
    print(f'#{t} {cnt}')