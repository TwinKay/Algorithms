import sys

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,1,0,-1]
delta_y = [-1,0,1,0]

N,M = map(int, sys.stdin.readline().split())
y,x,direct = map(int, sys.stdin.readline().split())
rule_a = []
for _ in range(N):
    rule_a.append(list(map(int,list(sys.stdin.readline().rstrip()))))
rule_b = []
for _ in range(N):
    rule_b.append(list(map(int,list(sys.stdin.readline().rstrip()))))

visited = []
for i in range(N):
    visited.append([])
    for _ in range(M):
        visited[i].append([-1]*4)

graph = []
for _ in range(N):
    graph.append([1]*M)

cnt_dust = 0
cnt_move = 0
last_dust_move = 0
while True:
    if visited[y][x][direct%4] == cnt_dust:
        break
    visited[y][x][direct%4] = cnt_dust

    is_dust = False
    if graph[y][x]:
        graph[y][x] = 0
        cnt_dust += 1
        is_dust = True
        last_dust_move = cnt_move + 1

    if is_dust:
        direct = direct + rule_a[y][x]
    else:
        direct = direct + rule_b[y][x]

    dx = x + delta_x[direct%4]
    dy = y + delta_y[direct%4]

    cnt_move += 1

    if not is_valid(dx,dy):
        break

    x,y = dx,dy

print(last_dust_move)