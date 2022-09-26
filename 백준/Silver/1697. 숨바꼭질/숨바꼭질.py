import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
visited = [0]*100001


def bfs(n):
    deq = deque([n])
    visited[n] = 1
    while deq:
        a = deq.popleft()
        if a == k:
            print(visited[a]-1)
            break
        else:
            if 0 <= a-1 <= 100000 and visited[a-1] == 0:
                deq.append(a-1)
                visited[a-1] = visited[a] + 1

            if 0 <= a+1 <= 100000 and visited[a+1] == 0:
                deq.append(a+1)
                visited[a+1] = visited[a] + 1

            if 0 <= a*2 <= 100000 and visited[a*2] == 0:
                deq.append(a*2)
                visited[a*2] = visited[a] + 1

bfs(n)