T = int(input())
for t in range(1,T+1):
    N,M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(input().rstrip()))

    min_val = 5000
    for up in range(1, N-1):
        for down in range(up, N-1):
            cnt = 0
            for i in range(0,up):
                for j in range(M):
                    if graph[i][j] != "W":
                        cnt += 1

            for i in range(up,down+1):
                for j in range(M):
                    if graph[i][j] != "B":
                        cnt += 1

            for i in range(down+1,N):
                for j in range(M):
                    if graph[i][j] != "R":
                        cnt += 1
            min_val = min(min_val,cnt)
    print(f'#{t} {min_val}')
