def solution(maps):
    from collections import deque

    n = len(maps)
    m = len(maps[0])

    visited = []
    for _ in range(n):
        visited.append([False]*m)

    deq = deque([])
    deq.append([0,0,1])
    visited[0][0] = True
    while deq:
        x,y,cnt = deq.popleft()

        if x-1 != -1:
            if visited[y][x-1] == False and maps[y][x-1] == 1:
                deq.append([x-1,y,cnt+1])
                visited[y][x-1] = True

        if y-1 != -1:
            if visited[y-1][x] == False and maps[y-1][x] == 1:
                deq.append([x,y-1,cnt+1])
                visited[y-1][x] = True

        if x+1 != m:
            if visited[y][x+1] == False and maps[y][x+1] == 1:
                deq.append([x+1,y,cnt+1])
                visited[y][x+1] = True

        if y+1 != n:
            if visited[y+1][x] == False and maps[y+1][x] == 1:
                deq.append([x,y+1,cnt+1])
                visited[y+1][x] = True

        if visited[n-1][m-1] == True:
            break

    if visited[n-1][m-1] == True:
        return cnt+1
    else:
        return -1
