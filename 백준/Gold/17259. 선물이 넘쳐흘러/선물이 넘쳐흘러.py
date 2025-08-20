'''
'''
import sys

def is_valid(x,y):
    return 0<=x<B and 0<=y<B


def near_people(x,y):
    for k in range(1,4):
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        if is_valid(dx,dy):
            if graph[dy][dx] >= 0:
                return graph[dy][dx]
    return -1

delta_x = [1,0,0,-1]
delta_y = [0,1,-1,0]

B,N,M = map(int,sys.stdin.readline().split())
people_idxs = []
people_times = []
people_cool_times = [0]*N
for _ in range(N):
    y,x,time = map(int,sys.stdin.readline().split())
    people_idxs.append([x,y])
    people_times.append(time)

graph = []
for _ in range(B):
    graph.append([-1]*B)

for i in range(N):
    x,y = people_idxs[i]
    graph[y][x] = i

container_idxs = []
for i in range(B):
    container_idxs.append([i,B-1])
for i in range(B-2,-1,-1):
    container_idxs.append([B-1,i])
for i in range(B-2,-1,-1):
    container_idxs.append([i,0])

not_on_gift = M
cnt_gift = 0
trash_gift = 0
# time = 1
while cnt_gift+trash_gift < M:
    if not_on_gift > 0:
        graph[0][0] = -9
        not_on_gift -= 1

    for ci in range(len(container_idxs)):
        cx,cy = container_idxs[ci]

        if cx==0 and cy==B-1:
            if graph[cy][cx]==-9:
                p_idx = near_people(cx, cy)
                if p_idx >= 0:
                    if people_cool_times[p_idx] <= 0: # 설마 부등호 때문..?
                        graph[cy][cx] = -1
                        cnt_gift += 1
                        people_cool_times[p_idx] = people_times[p_idx]
                    else:
                        graph[cy][cx] = -1
                        trash_gift += 1
                else:
                    graph[cy][cx] = -1
                    trash_gift += 1

            continue

        if graph[cy][cx] == -9:
            # 포장 가능
            p_idx = near_people(cx,cy)
            if p_idx >=0:
                if people_cool_times[p_idx]<=0:
                    graph[cy][cx] = -1
                    cnt_gift += 1
                    people_cool_times[p_idx] = people_times[p_idx]
                    continue

            # 포장 불가능
            cpx, cpy = container_idxs[ci-1]
            graph[cpy][cpx] = -9
            graph[cy][cx] = -1

    for i in range(N):
        people_cool_times[i] -= 1



    # print(f'time: {time}')
    # print(f'not_on_gift: {not_on_gift}')
    # print(f'cnt_gift: {cnt_gift}')
    # print(f'trash_gift: {trash_gift}')
    # print(f'people_cool_times: {people_cool_times}')
    # print(f'people_times: {people_times}')
    # print("graph:")
    # for g in graph:
    #     print(*g)
    #
    # print()
    # print()
    # time += 1
print(cnt_gift)