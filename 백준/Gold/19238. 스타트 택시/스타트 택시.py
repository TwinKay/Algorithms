import sys
from collections import deque

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def find_near_person_id(taxi_x,taxi_y): # return: id, 거리 (못가면 -1 -1)
    visited = []
    for _ in range(N):
        visited.append([0]*N)


    res_id,res_time = -1,float('inf')
    deq = deque()
    deq.append([taxi_x,taxi_y,0])
    visited[taxi_y][taxi_x] = 1
    while deq:
        x,y,time = deq.popleft()
        if time > res_time:
            break
        if graph[y][x] >= 0: # 손님이면
            if time == res_time:
                res_x = start_idxs[res_id][0]
                res_y = start_idxs[res_id][1]
                if res_y == y:
                    if res_x < x:
                        continue
                    else:
                        res_id = graph[y][x]
                elif res_y < y: # res 유지
                    continue
                else:
                    res_id = graph[y][x]
            elif time < res_time:
                res_id, res_time = graph[y][x], time
            # return graph[y][x], time # 손님 id , 시간
        for k in range(4):
            dx = x + delta_x[k]
            dy = y + delta_y[k]
            if not is_valid(dx,dy):
                continue
            if graph[dy][dx] == -1: # 벽이면
                continue
            if visited[dy][dx]:
                continue
            deq.append([dx,dy,time+1])
            visited[dy][dx] = 1
    return res_id,res_time

def bfs(start_x,start_y,end_x,end_y): # return return: 거리 (못가면 -1)
    visited = []
    for _ in range(N):
        visited.append([0]*N)

    deq = deque()
    deq.append([start_x,start_y,0])
    visited[start_y][start_x] = 1
    while deq:
        x,y,time = deq.popleft()
        if x==end_x and y==end_y: # 손님의 도착지면
            return time

        for k in range(4):
            dx = x + delta_x[k]
            dy = y + delta_y[k]
            if not is_valid(dx,dy):
                continue
            if graph[dy][dx] == -1: # 벽이면
                continue
            if visited[dy][dx]:
                continue
            deq.append([dx,dy,time+1])
            visited[dy][dx] = 1
    return -1

# 우선순위에 의해
delta_x = [0,-1,1,0]
delta_y = [-1,0,0,1]

N,M,energy = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

y,x = map(int, sys.stdin.readline().split())
y -= 1; x -= 1 # 1-based

start_idxs = []
end_idxs = []
for _ in range(M):
    sy,sx,ey,ex = map(int, sys.stdin.readline().split()) # 1-based
    start_idxs.append([sx-1,sy-1])
    end_idxs.append([ex-1,ey-1])

# -2: 이동가능 -1: 벽 0: 손님 출발지 index(손님 id)->출발지는 모두 달라서 가능
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = -2
        else:
            graph[i][j] = -1
for i in range(M):
    graph[start_idxs[i][1]][start_idxs[i][0]] = i

res = -1
for _ in range(M): # 손님만큼 운행
    person_id, time = find_near_person_id(x,y) # 가까운 손님 찾기
    if person_id == -1: # 갈 수 없으면
        break
    energy -= time
    # if energy < 0: # 연료 부족, 나중에 체크해도 가능 근데 미리 한번 보자
    #     break

    # 택시 위치 update
    x,y = start_idxs[person_id][0],start_idxs[person_id][1]

    time = bfs(x,y,end_idxs[person_id][0],end_idxs[person_id][1]) # 도착지 찾기
    if time == -1: # 못가면
        break
    energy -= time
    if energy < 0: # 연료 부족
        break
    energy += time*2 # 충전
    # 택시 위치 update
    x,y = end_idxs[person_id][0],end_idxs[person_id][1]

    # 데려다주면 그래프 빼주기
    graph[start_idxs[person_id][1]][start_idxs[person_id][0]] = -2
else: # 운행 마치면
    res = energy

print(res)