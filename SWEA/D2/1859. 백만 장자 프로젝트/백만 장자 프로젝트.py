T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    price_arr = [0]*10001
    for a in arr:
        price_arr[a] += 1

    cnt = 0
    for i in range(N-1):
        m = 10000
        for j in range(m,0,-1):
            if price_arr[j] != 0:
                m = j
                break

        if arr[i] < m:
            cnt += m-arr[i]

        price_arr[arr[i]] -= 1

    print(f"#{t} {cnt}")