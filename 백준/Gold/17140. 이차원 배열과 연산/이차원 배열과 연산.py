import sys

target_y,target_x,K = map(int, sys.stdin.readline().split())
target_x -= 1; target_y -= 1
graph = []
for _ in range(3):
    graph.append(list(map(int, sys.stdin.readline().split())))

def rotate_graph(graph):
    x, y = len(graph[0]), len(graph)
    rotate_graph = []
    for j in range(x):
        rotate_graph.append([])
        for i in range(y):
            rotate_graph[j].append(graph[i][j])

    return rotate_graph

def spread(graph):
    new_graph = []
    x,y = len(graph[0]),len(graph)
    is_rotate = False
    if x > y:
        graph = rotate_graph(graph)
        x,y = y,x
        is_rotate = True


    for i in range(y):
        dic = {}
        for j in range(x):
            num = graph[i][j]
            if num == 0:
                continue
            if num in dic.keys():
                dic[num] += 1
            else:
                dic[num] = 1

        temp = []
        for key in dic.keys():
            temp.append([dic[key],key]) # 몇번 수
        temp.sort()

        one_dim = []
        for (val,key) in temp:
            one_dim.append(key)
            one_dim.append(val)
        new_graph.append(one_dim)

    return new_graph, is_rotate

def extend(graph):
    x, y = len(graph[0]), len(graph)
    max_len = -1
    for i in range(y):
        max_len = max(max_len, len(graph[i]))
    for i in range(y):
        for j in range(max_len-len(graph[i])):
            graph[i].append(0)
    return graph

def cut(graph,cut_len):
    for i in range(len(graph)):
        for _ in range(cut_len):
            graph[i].pop()
    return graph


res = -1
time = -1
while True:
    time += 1
    if time == 101:
        break
    if 0 <= target_x < len(graph[0]) and 0 <= target_y < len(graph) and graph[target_y][target_x] == K:
        res = time
        break

    graph,is_rotate = spread(graph)
    graph = extend(graph)
    if is_rotate:
        graph = rotate_graph(graph)
        is_rotate = False # 필요 없음
    if len(graph[0]) > 100:
        cut(len(graph[0]) - 100)


print(res)