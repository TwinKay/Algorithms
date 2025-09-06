import sys

delta_x = [0,-1,-1,-1,0,1,1,1]
delta_y = [-1,-1,0,1,1,1,0,-1]

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def find_fish_index(id_graph,n):
    for i in range(N):
        for j in range(N):
            if id_graph[i][j] == n:
                return j,i
    return None,None

def switch_fish(id_graph,direct_graph,x1,y1,x2,y2):
    id_graph[y1][x1],id_graph[y2][x2] = id_graph[y2][x2],id_graph[y1][x1]
    direct_graph[y1][x1],direct_graph[y2][x2] = direct_graph[y2][x2],direct_graph[y1][x1]
    return id_graph,direct_graph

def move_each_fish(shark_x,shark_y,id_graph,direct_graph,n):
    x,y = find_fish_index(id_graph,n)

    if x == None: return id_graph,direct_graph
    direct = direct_graph[y][x]
    for k in range(8):
        dx = x + delta_x[(direct+k)%8]
        dy = y + delta_y[(direct+k)%8]
        if not is_valid(dx,dy):
            continue
        if dx==shark_x and dy==shark_y:
            continue
        new_direct = (direct+k)%8
        direct_graph[y][x] = new_direct
        id_graph,direct_graph = switch_fish(id_graph,direct_graph,x,y,dx,dy)
        break
    return id_graph,direct_graph

def move_fish(shark_x,shark_y,id_graph,direct_graph):
    for i in range(1,17):
        id_graph,direct_graph = move_each_fish(shark_x,shark_y,id_graph,direct_graph,i)
    return id_graph,direct_graph


# res도 같이
def move_shark(shark_x,shark_y,shark_direct,id_graph):
    can_go_idxs = [] # x,y
    x,y = shark_x,shark_y
    while True:
        dx = x + delta_x[shark_direct]
        dy = y + delta_y[shark_direct]
        if not is_valid(dx,dy):
            break
        if id_graph[dy][dx] != None:
            can_go_idxs.append([dx,dy])
        x,y = dx,dy
    return can_go_idxs

def back_track(shark_x,shark_y,shark_direct,direct_graph,id_graph,val):
    global max_res

    can_go_idxs = move_shark(shark_x,shark_y,shark_direct,id_graph)
    if not can_go_idxs:
        max_res = max(max_res,val)
        return

    for dx,dy in can_go_idxs:
        next_shark_direct = direct_graph[dy][dx]
        next_direct_graph = [g[:] for g in direct_graph]
        next_id_graph = [g[:] for g in id_graph]

        next_val = val + next_id_graph[dy][dx]
        next_direct_graph[dy][dx] = None
        next_id_graph[dy][dx] = None

        next_id_graph,next_direct_graph = move_fish(dx,dy,next_id_graph,next_direct_graph)

        back_track(dx,dy,next_shark_direct,next_direct_graph,next_id_graph,next_val)

N = 4
direct_graph = []
id_graph = []
for _ in range(N):
    direct_graph.append([])
    id_graph.append([])

for i in range(4):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(0,8,2):
        direct_graph[i].append(line[j+1]-1)
        id_graph[i].append(line[j])

shark_x,shark_y,shark_direct = 0,0,None
val = 0
val += id_graph[0][0]
id_graph[0][0] = None # 먹으면 0
shark_direct = direct_graph[0][0]
direct_graph[0][0] = None # 안전하게

id_graph,direct_graph = move_fish(shark_x,shark_y,id_graph,direct_graph) #?
max_res = -1
back_track(shark_x,shark_y,shark_direct,[g[:] for g in direct_graph],[g[:] for g in id_graph],val)

print(max_res)