import sys
from itertools import combinations

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,M,G,R = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

spread_idxs = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            spread_idxs.append((j,i))
            # graph[i][j] = 1

def spread(green_spread_idxs, red_spread_idxs):
    flower_set = set()
    visited = []
    for _ in range(N):
        visited.append([0]*M)

    for g_idx in green_spread_idxs:
        visited[g_idx[1]][g_idx[0]] = 1
    for r_idx in red_spread_idxs:
        visited[r_idx[1]][r_idx[0]] = 1

    # 시간 조금이라도 줄일라고 red는 lst로 관리
    while green_spread_idxs and red_spread_idxs:
        next_green_spread_idxs = set()
        next_red_spread_idxs = set()

        for x,y in green_spread_idxs:
            for k in range(4):
                dx = x + delta_x[k]
                dy = y + delta_y[k]
                if not is_valid(dx,dy):
                    continue
                if visited[dy][dx]:
                    continue
                if graph[dy][dx] == 0:
                    continue
                next_green_spread_idxs.add((dx,dy))
                # visited 나중에 처리

        for x,y in red_spread_idxs:
            for k in range(4):
                dx = x + delta_x[k]
                dy = y + delta_y[k]
                if not is_valid(dx,dy):
                    continue
                if visited[dy][dx]:
                    continue
                if graph[dy][dx] == 0:
                    continue
                next_red_spread_idxs.add((dx,dy))
                # visited 나중에 처리

        # 같은 초에 도착한 칸 = 꽃
        inter = next_green_spread_idxs & next_red_spread_idxs
        if inter:
            flower_set |= inter
            next_green_spread_idxs -= inter
            next_red_spread_idxs -= inter
            # 꽃 칸은 방문 처리해서 다시는 못 들어오게
            for x, y in inter:
                visited[y][x] = 1

        for g_idx in next_green_spread_idxs:
            visited[g_idx[1]][g_idx[0]] = 1
        for r_idx in next_red_spread_idxs:
            visited[r_idx[1]][r_idx[0]] = 1

        green_spread_idxs = next_green_spread_idxs
        red_spread_idxs = next_red_spread_idxs

    return len(flower_set)


res_max = 0
for comb1 in combinations(spread_idxs,G+R):
    for comb2 in combinations(comb1,G):
        green_spread_idxs = set()
        red_spread_idxs = set()
        for c in comb2:
            green_spread_idxs.add(c)
        for c in comb1:
            if c not in green_spread_idxs:
                red_spread_idxs.add(c)

        flower_cnt = spread(green_spread_idxs, red_spread_idxs)
        res_max = max(res_max,flower_cnt)

print(res_max)