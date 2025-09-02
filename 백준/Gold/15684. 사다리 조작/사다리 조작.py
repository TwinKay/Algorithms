import sys
from itertools import combinations

def is_valid(x,y):
    return 0<=x<2*N-1 and 0<=y<H

delta_x = [-1,1,0]
delta_y = [0,0,1]

N,M,H = map(int, sys.stdin.readline().split())

graph = []
for _ in range(H):
    graph.append([0]*(2*N-1))

already_garo = set()
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    a-=1;b-=1
    already_garo.add((b*2+1,a)) # 중간 위치, 가로선 위치
    graph[a][b*2+1] = 1


for i in range(H):
    for j in range(0,2*N-1,2):
        graph[i][j] = 1

cands = []
for i in range(H):
    for j in range(1,2*N-1,2):
        if (j,i) not in already_garo:
            cands.append((j,i))

res = -1
is_find = False
for cand_num in range(len(cands)+1):
    if is_find:
        break
    if cand_num > 3:
        break
    for comb in combinations(cands,cand_num):
        for c in comb:
            graph[c[1]][c[0]] = 1

        is_can = True
        for c in comb:
            if is_valid(c[0]-2,c[1]):
                if graph[c[1]][c[0]-2] == 1:
                    is_can = False
                    break
            if is_valid(c[0]+2,c[1]):
                if graph[c[1]][c[0]+2] == 1:
                    is_can = False
                    break

        if not is_can:
            for c in comb:
                graph[c[1]][c[0]] = 0
            continue

        is_find = False
        for first_x in range(0,2*N,2):
            first_y = 0
            x,y = first_x,first_y
            # visited = set()
            # visited.add((x,y))
            while y < H: # 끝 도착
                for k in range(3):
                    dx = x + delta_x[k]
                    dy = y + delta_y[k]
                    if not is_valid(dx,dy):
                        continue
                    if graph[dy][dx] == 0:
                        continue
                    if k != 2: # visited 안쓰고 점프
                        dx = x+delta_x[k]*2
                        dy = y+1

                    # if (dx,dy) in visited:
                    #     continue
                    # visited.add((dx,dy))
                    x,y = dx,dy
                    break
                x,y = dx,dy
            # 같은지 판별 break or 계속
            if x != first_x:
                break
        else:
            is_find = True

        if is_find:
            res = cand_num
            break

        for c in comb: # 원복
            graph[c[1]][c[0]] = 0

print(res)
