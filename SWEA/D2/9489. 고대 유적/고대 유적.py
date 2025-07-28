from collections import deque

delta_x1 = [-1,1]
delta_y1 = [0,0]
delta_x2 = [0,0]
delta_y2 = [-1,1]

def isValid(x,y):
    return 0<=x<M and 0<=y<N

T = int(input())
for t in range(1,T+1):
    N,M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    max_val = 0

    # 가로 먼저
    visited = []
    for _ in range(N):
        visited.append([False]*M)

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] == 1:
                deq = deque()
                deq.append([j,i])
                visited[i][j] = True
                cnt = 1
                while deq:
                    cur = deq.popleft()
                    for k in range(2):
                        dx = cur[0] + delta_x1[k]
                        dy = cur[1] + delta_y1[k]
                        if isValid(dx,dy) and not visited[dy][dx] and graph[dy][dx]==1:
                            deq.append([dx,dy])
                            visited[dy][dx] = True
                            cnt += 1
                max_val = max(max_val,cnt)


    # 세로
    visited = []
    for _ in range(N):
        visited.append([False]*M)

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] == 1:
                deq = deque()
                deq.append([j,i])
                visited[i][j] = True
                cnt = 1
                while deq:
                    cur = deq.popleft()
                    for k in range(2):
                        dx = cur[0] + delta_x2[k]
                        dy = cur[1] + delta_y2[k]
                        if isValid(dx,dy) and not visited[dy][dx] and graph[dy][dx]==1:
                            deq.append([dx,dy])
                            visited[dy][dx] = True
                            cnt += 1
                max_val = max(max_val,cnt)

    print(f"#{t} {max_val}")

