import sys

delta_x = [0,1,1,1,0,-1,-1,-1]
delta_y = [-1,-1,0,1,1,1,0,-1]

N,Q,K = map(int, sys.stdin.readline().split())

graph = []
for i in range(N):
    graph.append([])
    for j in range(N):
        graph[i].append([])

for _ in range(Q):
    y,x,m,s,d = map(int, sys.stdin.readline().split())
    graph[y-1][x-1].append((m,d,s)) #질량 방향 속력

def is_union_direct(lst):
    a = lst[0]%2
    for b in lst[1:]:
        if a != b%2:
            return False
    return True

for _ in range(K):
    for _ in range(N):
        new_graph = []
        for i in range(N):
            new_graph.append([])
            for j in range(N):
                new_graph[i].append([])
    #
    # 자신의 방향 d로 속력 s칸만큼 이동
    for y in range(N):
        for x in range(N):
            if graph[y][x]:
                for i in range(len(graph[y][x])):
                    m,d,s = graph[y][x][i]
                    dx = (x + delta_x[d]*s)%N
                    dy = (y + delta_y[d]*s)%N
                    new_graph[dy][dx].append((m,d,s))#질량 방향 속력

    for y in range(N):
        for x in range(N):
            if len(new_graph[y][x]) < 2:
                continue
            sum_m = 0
            d_lst = []
            sum_s = 0
            for (m,d,s) in new_graph[y][x]:
                sum_m += m
                d_lst.append(d)
                sum_s += s
            new_m = sum_m//5

            if new_m <= 0:
                new_graph[y][x] = []
                continue
            new_s = sum_s//len(new_graph[y][x])
            new_graph[y][x] = []
            if is_union_direct(d_lst):
                for direct in range(0,7,2):
                    new_graph[y][x].append((new_m,direct,new_s))
            else:
                for direct in range(1,8,2):
                    new_graph[y][x].append((new_m,direct,new_s))

    graph = new_graph

res = 0
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            for k in range(len(graph[i][j])):
                res += graph[i][j][k][0]
print(res)