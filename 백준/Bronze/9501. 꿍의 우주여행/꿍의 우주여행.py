T = int(input().strip())
for _ in range(T):
    N, D = map(int, input().split())
    cnt = 0
    for _ in range(N):
        v, f, c = map(int, input().split())
        if D * c <= f * v:
            cnt += 1
    print(cnt)