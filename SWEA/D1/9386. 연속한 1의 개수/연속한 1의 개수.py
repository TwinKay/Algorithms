T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int, input()))

    cnt = 0; max = 0
    for a in arr:
        if a == 1:
            cnt += 1
        else:
            cnt = 0
        if cnt > max:
            max = cnt

    print(f'#{t} {max}')