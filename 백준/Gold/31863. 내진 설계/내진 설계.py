def is_valid(x,y):
    return 0<=x<M and 0<=y<N


def get_affect_indexes(idxs,is_first):
    affect_idxs = []
    for x,y in idxs:
        for k in range(4):
            length = 0
            max_length = None
            if is_first:
                max_length = 2
            else:
                max_length = 1
            while True:
                if length == max_length:
                    break
                dx = x + delta_x[k] * (length+1)
                dy = y + delta_y[k] * (length+1)
                if not is_valid(dx,dy):
                    break
                if graph[dy][dx] == 1:
                    break
                affect_idxs.append([dx,dy])
                length += 1
    return affect_idxs

def get_down_building_indexes(affect_idxs):
    next_jijin_idxs = []
    for x,y in affect_idxs:
        if building_graph[y][x] >= 1:
            building_graph[y][x] -= 1
            if building_graph[y][x] == 0:
                next_jijin_idxs.append([x,y])
    return next_jijin_idxs

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,M = map(int, input().split())
origin_graph = []
for _ in range(N):
    origin_graph.append(list(input()))

graph = []
building_graph = []
for _ in range(N):
    graph.append([0]*M)
    building_graph.append([0]*M)

jijin_idxs = []
for i in range(N):
    for j in range(M):
        if origin_graph[i][j] == '@':
            jijin_idxs.append([j,i])
        elif origin_graph[i][j] == '|':
            graph[i][j] = 1
        elif origin_graph[i][j] == '*':
            building_graph[i][j] = 1
        elif origin_graph[i][j] == '#':
            building_graph[i][j] = 2

affect_idxs = get_affect_indexes(jijin_idxs,True)
down_building_idxs = get_down_building_indexes(affect_idxs)
while True:
    if not down_building_idxs:
        break
    affect_idxs = get_affect_indexes(down_building_idxs,False)
    down_building_idxs = get_down_building_indexes(affect_idxs)

before_cnt_building,after_cnt_building = 0,0
for i in range(N):
    for j in range(M):
        if origin_graph[i][j] in ['*','#']:
            before_cnt_building += 1
        if building_graph[i][j]:
            after_cnt_building += 1
print(before_cnt_building-after_cnt_building,after_cnt_building)