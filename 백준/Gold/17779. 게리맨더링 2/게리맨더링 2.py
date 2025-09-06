import sys
from collections import deque

N = int(sys.stdin.readline())
person_graph = []
for _ in range(N):
    person_graph.append(list(map(int, sys.stdin.readline().split())))

delta_x = [0,1,-1,0]
delta_y = [-1,0,0,1]

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def draw_line(graph,direct,y,x):
    num = direct+1
    while True:
        dx = x + delta_x[direct]
        dy = y + delta_y[direct]
        if not is_valid(dx,dy):
            break
        graph[dy][dx] = num

        x,y = dx,dy
    return graph

def bfs(graph,visited,group_id,x,y):
    deq = deque()
    deq.append([x,y])
    visited[y][x] = group_id
    while deq:
        x,y = deq.popleft()
        if graph[y][x]:
            continue
        for k in range(4):
            dx = x + delta_x[k]
            dy = y + delta_y[k]
            if not is_valid(dx,dy):
                continue
            if visited[dy][dx]:
                continue
            if not graph[dy][dx] in [0,group_id]:
                continue
            deq.append([dx,dy])
            visited[dy][dx] = group_id

def get_diff(x,y,d1,d2):
    x-=1; y-=1
    graph = []
    for _ in range(N):
        graph.append([0]*N)

    for i in range(d1+1):
        graph[x+i][y-i] = 5
    for i in range(d2+1):
        graph[x+i][y+i] = 5
    for i in range(d2+1):
        graph[x+d1+i][y-d1+i] = 5
    for i in range(d1+1):
        graph[x+d2+i][y+d2-i] = 5
    graph = draw_line(graph,0,x,y)
    graph = draw_line(graph,1,x+d2,y+d2)
    graph = draw_line(graph,2,x+d1,y-d1)
    graph = draw_line(graph,3,x+d2+d1,y+d2-d1)

    visited = []
    for _ in range(N):
        visited.append([0]*N)

    bfs(graph,visited,1,0,0)
    bfs(graph,visited,3,0,N-1)
    bfs(graph,visited,2,N-1,0)
    bfs(graph,visited,4,N-1,N-1)

    # print("graph")
    # for g in graph:
    #     print(g)
    # print("visited")
    # for v in visited:
    #     print(v)
    # print("=========================")

    cnt_arr = [0,0,0,0,0]
    for i in range(N):
        for j in range(N):
            cnt_arr[visited[i][j]] += person_graph[i][j]

    return max(cnt_arr)-min(cnt_arr)


min_diff = float('inf')
for y in range(1,N+1):
    for x in range(1,N+1):
        for d1 in range(1,N+1):
            for d2 in range(1,N+1):
                if 1<=x<x+d1+d2<=N and 1<=y-d1<y<y+d2<=N:
                    diff = get_diff(x,y,d1,d2)
                    min_diff = min(min_diff,diff)
print(min_diff)