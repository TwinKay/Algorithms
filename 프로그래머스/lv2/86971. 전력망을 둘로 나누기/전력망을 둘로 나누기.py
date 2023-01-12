def solution(n, wires):
    from collections import deque
    
    res = []
    for k in range(len(wires)):
        graph = []
        for _ in range(n+1):
            graph.append([])

        for l,i in enumerate(wires):
            if k==l:
                pass
            else:
                a,b = i
                graph[a].append(b)
                graph[b].append(a)
        
        visited = [False]*len(graph)

        cnt = 0
        deq = deque([])
        deq.append(1)
        visited[1] = True
        while deq:
            x = deq.popleft()
            for i in graph[x]:
                if visited[i] == False:
                    deq.append(i)
                    visited[i] = True
            cnt += 1

        res.append(abs(cnt-(n-cnt)))
    res.sort()

    return res[0]