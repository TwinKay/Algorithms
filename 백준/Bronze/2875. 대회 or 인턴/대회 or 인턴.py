N, M, K = map(int, input().split())
max_team = min(N // 2, M)
for t in range(max_team, -1, -1):
    if N + M - 3 * t >= K:
        print(t)
        break