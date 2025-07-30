'''
BFS를 통한 풀이
4방 탐색
꼭 Group ID 부여 필요 X -> visited으로 방문 안하면 된다
'''
import sys
from collections import deque

# 가능한 범위
def is_valid(x,y):
    return 0<=x<N and 0<=y<N

# 4방 탐색
delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N = int(sys.stdin.readline())
graph = []
visited = []
for _ in range(N):
    graph.append(list(map(int, list(sys.stdin.readline().rstrip()))))
    visited.append([False]*N)

res = [] # 정답 넣을 list
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]: # 집, 방문 X 경우만
            cnt = 0
            deq = deque()
            deq.append([j,i])
            visited[i][j] = True
            while deq:
                cur = deq.popleft()
                cnt += 1
                for k in range(4):
                    dx = cur[0] + delta_x[k]
                    dy = cur[1] + delta_y[k]
                    if is_valid(dx,dy) and graph[dy][dx] == 1 and not visited[dy][dx]: # 가능한 범위, 집, 방문 X
                        deq.append([dx,dy])
                        visited[dy][dx] = True
            res.append(cnt)
            
res.sort() # 정답 정렬해서 제출
print(len(res))
for r in res:
    print(r)