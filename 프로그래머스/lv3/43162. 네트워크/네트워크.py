def solution(n, computers):
    from collections import deque

    graph = []
    for _ in range(n):
        graph.append([])

    for a,i in enumerate(computers):
        for b,j in enumerate(i):
            if j==1 and a!=b:
                graph[a].append(b)

    visited = [False]*n

    def bfs(x):
        deq = deque([])
        deq.append(x)
        visited[x] = True
        while deq:
            x = deq.popleft()
            for i in graph[x]:
                if visited[i] == False:
                    deq.append(i)
                    visited[i] = True

    cnt = 0
    for i in range(n):
        if visited[i] == False:
            bfs(i)
            cnt += 1

    return cnt