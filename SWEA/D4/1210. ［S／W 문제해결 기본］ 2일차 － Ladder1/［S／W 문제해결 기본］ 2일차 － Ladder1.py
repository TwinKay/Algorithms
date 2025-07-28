'''
양 옆으로 갈라져있는 경우 X
끝에서 시작해서 시작점 찾기!
'''
res = []

def is_valid(x,y):
    return 0<=x<100 and 0<=y<100

for _ in range(10):
    t = int(input())
    graph = []
    for _ in range(100):
        graph.append(list(map(int, input().split())))

    target = -1
    for i in range(100):
        if graph[99][i] == 2:
            target = i
            break

    visited = []
    for _ in range(100):
        visited.append([False]*100)
    visited[99][target] = True
    x,y = target,99
    while y>0:
        if is_valid(x+1,y) and graph[y][x+1] == 1 and not visited[y][x+1]:
            x += 1
            visited[y][x] = True
            continue
        if is_valid(x-1,y) and graph[y][x-1] == 1 and not visited[y][x-1]:
            x -= 1
            visited[y][x] = True
            continue
        y -= 1
        visited[y][x] = True
    res.append(f"#{t} {x}")
print("\n".join(res))
