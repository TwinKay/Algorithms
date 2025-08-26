import sys

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def move_cloud(cloud_idxs,direct, dist):
    moved_cloud_idxs = set()
    for x,y in cloud_idxs:
        dx = x + cloud_delta_x[direct]*dist
        dy = y + cloud_delta_y[direct]*dist
        dx %= N
        dy %= N
        moved_cloud_idxs.add((dx,dy))
    return moved_cloud_idxs

def copy_water(moved_cloud_idxs):
    for x,y in moved_cloud_idxs:
        cnt = 0
        for k in range(4):
            dx = x + water_delta_x[k]
            dy = y + water_delta_y[k]
            if is_valid(dx,dy):
                if graph[dy][dx] > 0:
                    cnt += 1
        graph[y][x] += cnt

#                ←, ↖, ↑ ↗ →,↘ ↓ ↙
cloud_delta_x = [-1,-1,0,1,1,1,0,-1]
cloud_delta_y = [0,-1,-1,-1,0,1,1,1]

water_delta_x = [-1,-1,1,1]
water_delta_y = [-1,1,-1,1]

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

cloud_idxs = set()
cloud_idxs.add((0,N-1))
cloud_idxs.add((1,N-1))
cloud_idxs.add((0,N-2))
cloud_idxs.add((1,N-2))

for _ in range(M):
    direct, dist = map(int, sys.stdin.readline().split())
    direct -= 1

    moved_cloud_idxs = move_cloud(cloud_idxs,direct, dist)
    for x,y in moved_cloud_idxs:
        graph[y][x] += 1

    copy_water(moved_cloud_idxs)

    cloud_idxs = set()
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and (j,i) not in moved_cloud_idxs:
                cloud_idxs.add((j,i))
                graph[i][j] -= 2

res = 0
for i in range(N):
    for j in range(N):
        res += graph[i][j]

print(res)