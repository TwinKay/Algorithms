def solution(begin, target, words):
    from collections import deque
    
    if target not in words:
        return 0
    elif begin in words:
        return 1
    visited = [0]*len(words)

    deq = deque([])
    deq.append(begin)
    w = begin
    breaker = False
    while deq:
        if breaker == True:
            break

        w = deq.popleft()
        for i in range(len(w)):
            if breaker == True:
                break
            x = w[:i]+w[i+1:]
            for n,j in enumerate(words):
                if visited[n] == 0:
                    if j[:i]+j[i+1:] == x:
                        deq.append(j)

                        if w in words:
                            visited[n] = visited[words.index(w)]+1
                        else:
                            visited[n] = 1
                        if j == target:
                            breaker = True
                            break
    
    return visited[words.index(target)]