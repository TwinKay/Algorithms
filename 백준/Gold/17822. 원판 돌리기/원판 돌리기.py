'''
deque를 써야할 것 같지만 사실 중간 조회가 더 많아서 비효율적일 것이다. ->list pop으로 가자
'''
import sys

def rotate(baesu,direct,num):
    for i in range(1,N):
        if (i+1)%baesu != 0:
            continue
        if direct: # 반시계
            for _ in range(num):
                graph[i].append(graph[i].pop(0))
        else: # 시계
            for _ in range(num):
                graph[i].insert(0,graph[i].pop())


def find_same_index():
    idxs = set()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                continue
            for k in range(4):
                dx = (j + delta_x[k])%M
                dy = i + delta_y[k]
                if not 0<=dy<N:
                    continue
                if graph[dy][dx] == 0:
                    continue
                if graph[i][j] == graph[dy][dx]:
                    idxs.add((dx,dy))
                    idxs.add((j,i))
    return idxs

def find_average_and_remain_indexs():
    cnt = 0
    sm = 0
    idxs = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                continue
            cnt += 1
            sm += graph[i][j]
            idxs.append([j,i])
    if cnt == 0: # for zero division error
        return -1, None
    return sm/cnt, idxs

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

N,M,T = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

for t in range(T):
    x,d,k = map(int, sys.stdin.readline().split())
    rotate(x,d,k)

    same_idxs = find_same_index()
    if same_idxs:
        for same_idx in same_idxs:
            graph[same_idx[1]][same_idx[0]] = 0
    else:
        aver,idxs = find_average_and_remain_indexs()
        if not idxs: # for zero division error
            break
        for idx in idxs:
            if graph[idx[1]][idx[0]] > aver:
                graph[idx[1]][idx[0]] -= 1
            elif graph[idx[1]][idx[0]] < aver:
                graph[idx[1]][idx[0]] += 1

res = 0
for i in range(N):
    for j in range(M):
        res += graph[i][j]
print(res)