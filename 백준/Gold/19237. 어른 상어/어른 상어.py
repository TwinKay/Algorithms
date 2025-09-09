# 쫓겨나도 냄새는 남아있는가? -> o
# 냄새가 다른 상어와 중복되는 일이 있는가? -> x
import sys

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

delta_x = [None,0,0,-1,1]
delta_y = [None,-1,1,0,0]

N,M,K = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

shark_first_directs = list(map(int, sys.stdin.readline().split()))

shark_infos = {}
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            # key: 좌표 / value: [[상어id,방향(1-based)]]
            shark_infos[(j,i)] = [[graph[i][j],shark_first_directs[graph[i][j]-1]]] # 처음에 중복 X

shark_to_direct = {}
for shark_id in range(1,M+1):
    shark_to_direct[shark_id] = [None]
    for direct in range(1,5):
        # key: 상어id / value: (2dim) 상어 현재 direct로 접근하여 4가지의 우선순위 direct list
        shark_to_direct[shark_id].append(list(map(int, sys.stdin.readline().split())))

# (3dim) -> 마지막 차원 [상어id, 최대 유지 시간]
smell_graph = [] # 냄새 기록용 [상어id, time(부터 사라짐)]
for i in range(N):
    smell_graph.append([])
    for j in range(N):
        smell_graph[i].append([])

# 첫 냄새 뿌리기
for key in shark_infos.keys():
    x,y = key
    shark_id = shark_infos[key][0][0]
    smell_graph[y][x] = [shark_id,0+K]


def find_next_info(shark_id,direct,x,y):
    direct_lst = shark_to_direct[shark_id][direct]

    for k in direct_lst:
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        if not is_valid(dx,dy):
            continue
        if (not smell_graph[dy][dx]) or (smell_graph[dy][dx][1] < time):
            return dx,dy,k

    for k in direct_lst:
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        if not is_valid(dx,dy):
            continue
        if smell_graph[dy][dx][0] == shark_id:
            return dx,dy,k


def move(shark_infos):
    new_shark_infos = {}
    # key: 좌표 / value: [[상어id,방향(1-based)]]
    for key in shark_infos.keys():
        x,y = key
        shark_id,direct = shark_infos[key][0]

        dx,dy,next_direct = find_next_info(shark_id,direct,x,y)
        if (dx,dy) in new_shark_infos.keys():
            new_shark_infos[(dx,dy)].append([shark_id,next_direct])
        else:
            new_shark_infos[(dx,dy)] = []
            new_shark_infos[(dx,dy)].append([shark_id,next_direct])

        # 냄새 기록은 먹은 다음에 기록 -> 동시에!!!!!!!!!!
        # smell_graph[dy][dx] = [shark_id,time+K]

    return new_shark_infos


def out(shark_infos):
    for key in shark_infos.keys():
        if len(shark_infos[key]) >= 2:
            shark_infos[key].sort()
            shark_infos[key] = [shark_infos[key][0]]
    return shark_infos

def spread_smell(smell_graph,shark_infos):
    for key in shark_infos.keys():
        x,y = key
        shark_id = shark_infos[key][0][0]
        smell_graph[y][x] = [shark_id, time+K]
    return smell_graph

time = 0
while True:
    time += 1
    if time == 1001:
        break

    # 우선순위 중 아무 냄새가 없는 (시간이 (t+K)보다 같거나 크면) 칸 우선
    # 우선순위 중 본인의 냄새 칸 우선
    shark_infos = move(shark_infos)
    # 쌓인 dict를 가장 낮은 번호만 유지
    shark_infos = out(shark_infos)
    # 냄새 뿌리기
    smell_graph = spread_smell(smell_graph,shark_infos)

    #################################################################
    # print(f'time: {time}')
    # temp = []
    # for i in range(N):
    #     temp.append([0]*N)
    # for key in shark_infos.keys():
    #     x,y = key
    #     temp[y][x] = shark_infos[key][0][0]
    # print("상어 위치:")
    # for t in temp:
    #     print(t)
    # print('냄새 정보')
    # for s in smell_graph:
    #     print(s)
    # print("=======================================")
    ###########################################################################

    # 만약 key가 1개면 break -> 1개 라는건 곧 1번만 남았다는 것
    if len(shark_infos.keys()) == 1:
        break

if time == 1001:
    print(-1)
else:
    print(time)