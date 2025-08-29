import sys

delta_x = [1,0,-1,0]
delta_y = [0,-1,0,1]

N = 101 # 입력이랑 다르고, 100기준으로 101임
visited = []
for _ in range(N):
    visited.append([0]*N)

K = int(sys.stdin.readline())
for dragon_id in range(K):
    x,y,direct,gen = map(int, sys.stdin.readline().split())

    dragon_path = []
    dragon_path.append([x,y])
    dragon_path.append([x+delta_x[direct],y+delta_y[direct]])

    for _ in range(gen):
        next_dragon_path = [dp for dp in dragon_path]
        tail_x,tail_y = dragon_path.pop()
        for x,y in dragon_path[::-1]:
            new_x = tail_x - (y-tail_y)
            new_y = tail_y + (x-tail_x)
            next_dragon_path.append([new_x,new_y])

        dragon_path = next_dragon_path


    for path_x,path_y in dragon_path:
        visited[path_y][path_x] = 1

cnt = 0
for i in range(N-1):
    for j in range(N-1):
        if visited[i][j] == visited[i+1][j] == visited[i][j+1] == visited[i+1][j+1] == 1:
            cnt += 1

print(cnt)