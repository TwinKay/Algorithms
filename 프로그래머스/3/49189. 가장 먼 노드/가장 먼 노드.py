def solution(n, edge):
    from collections import deque

    graph = []
    for _ in range(n+1):
        graph.append([])
    visited = []
    for _ in range(n+1):
        visited.append(-1)

    for i in edge:
        a,b = i
        graph[a].append(b)
        graph[b].append(a)

    deq = deque([1])
    visited[1] = 0
    while deq:
        node = deq.popleft()
        cnt = visited[node]
        for i in graph[node]:
            if visited[i] == -1:
                deq.append(i)
                visited[i] = cnt+1
    max_num = max(visited)
    res_cnt = 0
    for i in visited:
        if i == max_num:
            res_cnt += 1

    return res_cnt