T = int(input())
for t in range(1,T+1):
    N,M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    # arr1의 길이가 더 길거나 같도록 변경
    if N<M:
        N,M = M,N
        arr1,arr2 = arr2,arr1

    max_val = -1
    for i in range(N-M+1): # 비교 횟수
        sum_val = 0
        for j in range(M):
            sum_val += arr1[j+i] * arr2[j] # 막대가 더 긴 arr1만 j만큼 idx 변경
        max_val = max(max_val,sum_val)

    print(f'#{t} {max_val}')