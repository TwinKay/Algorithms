'''
graph[dy][dx] == 6:을 == '6':이라 해서 틀리고 찾는 것도 진짜 한참 찾았다 하..
'''
import sys

def is_valid(x,y):
    return 0<=x<M and 0<=y<N

delta_x = [0,1,0,-1]
delta_y = [-1,0,1,0]

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

cctv_dic = {}
cctv_dic[1] = [
    [0],
    [1],
    [2],
    [3]
]
cctv_dic[2] = [
    [1,3],
    [0,2]
]
cctv_dic[3] = [
    [0,1],
    [1,2],
    [2,3],
    [3,0]
]
cctv_dic[4] = [
    [0,2,3],
    [0,1,3],
    [0,1,2],
    [1,2,3]
]
cctv_dic[5] = [
    [0,1,2,3]
]

cctv_idxs = []
cctv_types = []
for i in range(N):
    for j in range(M):
        if 1 <= graph[i][j] <= 5:
            cctv_idxs.append([j,i])
            cctv_types.append(graph[i][j])

def back_track(n,lst):
    global min_res

    if n == len(cctv_idxs):
        visited = []
        for _ in range(N):
            visited.append([0]*M)

        for cctv_id in range(len(cctv_idxs)):
            cctv_x,cctv_y = cctv_idxs[cctv_id]
            type = cctv_types[cctv_id]
            cctv_directs = cctv_dic[type][lst[cctv_id]]

            for cctv_direct in cctv_directs:
                x,y = cctv_x,cctv_y
                while True:
                    dx = x + delta_x[cctv_direct]
                    dy = y + delta_y[cctv_direct]
                    if not is_valid(dx,dy):
                        break
                    if graph[dy][dx] == 6:
                        break
                    visited[dy][dx] = 1
                    x,y = dx,dy

        cnt = 0
        for i in range(N):
            for j in range(M):
                if not visited[i][j] and graph[i][j]==0:
                    cnt += 1

        min_res = min(min_res, cnt)
        return

    for i in range(len(cctv_dic[cctv_types[n]])):
        back_track(n+1,lst+[i])


min_res = N*M
back_track(0,[])
print(min_res)