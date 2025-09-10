import sys

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def init_direct(direct):
    arr = [None,3,1,2,0]
    return arr[direct]

def get_path():
    visited = []
    for _ in range(N):
        visited.append([0] * N)

    x,y,direct = 0,0,0
    visited[y][x] = 1
    path = [[x, y]]
    while True:
        dx = x + delta_x[direct]
        dy = y + delta_y[direct]
        if not is_valid(dx,dy):
            direct = (direct+1)%4
            continue
        if visited[dy][dx]:
            direct = (direct+1)%4
            continue
        if dx == N//2 and dy==N//2:
            break
        path.append([dx,dy])
        visited[dy][dx] = 1
        x,y = dx,dy

    return path[::-1]

def get_id_graph(path):
    graph = []
    for _ in range(N):
        graph.append([0]*N)

    for id,(x,y) in enumerate(path):
        graph[y][x] = id

    graph[N//2][N//2] = None

    return graph

def get_stone_lst(stone_graph,path):
    lst = []
    for x,y in path:
        if not stone_graph[y][x]:
            break
        lst.append(stone_graph[y][x])

    return lst

def shoot(direct,S,id_graph,stone_lst):
    direct = init_direct(direct)

    remove_ids = [0]*(N*N) # idx가 id -> set 보다 효율 up
    x,y = N//2,N//2
    for s in range(1,S+1):
        dx = x + delta_x[direct]*s
        dy = y + delta_y[direct]*s
        if not is_valid(dx,dy): # 사실 is valid 필요 X -> 제한에 범위 내로만 주어짐
            break

        remove_ids[id_graph[dy][dx]] = 1

    new_stone_lst = []
    for i in range(len(stone_lst)):
        if not remove_ids[i]:
            new_stone_lst.append(stone_lst[i])
        # else:
            # remove_cnt[stone_lst[i]] += 1 # 이거는 count 아님

    return new_stone_lst

def get_group_info(stone_lst):
    info_lst = []

    i = 0
    color = -1
    cnt = 0
    while True:
        if i == len(stone_lst):
            if color != -1: # 여기는 생각도 못했네.. 아래는 처리했으면서..
                info_lst.append([color, cnt])
            break
        if stone_lst[i] != color:
            if color != -1: # i가 1부터 하지말고 0부터하고 이렇게 해야 아무것도 없을때 방어적 프로그래밍 할 수 있음
                info_lst.append([color,cnt])
            color = stone_lst[i]
            cnt = 1
        else:
            cnt += 1

        i += 1

    return info_lst

def bomb(stone_lst):
    is_bomb = False
    stone_info = get_group_info(stone_lst)
    new_stone_lst = []
    for info in stone_info:
        color,cnt = info
        if cnt >= 4:
            remove_cnt[color] += cnt
            is_bomb = True
        else:
            for _ in range(cnt):
                new_stone_lst.append(color)
    return new_stone_lst,is_bomb

def spread(stone_lst):
    stone_info = get_group_info(stone_lst)
    new_stone_lst = []
    for info in stone_info:
        color,cnt = info
        new_stone_lst.append(cnt)
        new_stone_lst.append(color)
        if len(new_stone_lst) >= N*N-1:
            break
    return new_stone_lst[:N*N-1]

delta_x = [1,0,-1,0]
delta_y = [0,1,0,-1]

N,M = map(int, sys.stdin.readline().split())
stone_graph = []
for _ in range(N):
    stone_graph.append(list(map(int, sys.stdin.readline().split())))

path = get_path()
id_graph = get_id_graph(path)
stone_lst = get_stone_lst(stone_graph,path)

remove_cnt = [None,0,0,0]
for m in range(M):
    d,s = map(int, sys.stdin.readline().split())
    stone_lst = shoot(d,s,id_graph,stone_lst)
    while True:
        stone_lst,is_bomb = bomb(stone_lst)
        if not is_bomb: # 이제 더이상 터지는게 없을 때까지
            break
    stone_lst = spread(stone_lst)

print(remove_cnt[1]+remove_cnt[2]*2+remove_cnt[3]*3)