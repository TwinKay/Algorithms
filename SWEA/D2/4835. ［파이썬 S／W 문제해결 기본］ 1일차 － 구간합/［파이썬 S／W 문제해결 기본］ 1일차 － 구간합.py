'''
sliding window
'''
res = []

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    sum_val = 0
    for i in range(M):
        sum_val += arr[i]
    max_val = sum_val
    min_val = sum_val

    for i in range(M, N):
        sum_val += arr[i]
        sum_val -= arr[i - M]

        if sum_val > max_val:
            max_val = sum_val
        if sum_val < min_val:
            min_val = sum_val
    res.append(f'#{t} {max_val - min_val}')
print('\n'.join(res))