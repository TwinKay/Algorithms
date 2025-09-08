import sys

def get_can_put_height(graph,left,right):
    keep = 0
    for i in range(6):
        for j in range(left,right+1):
            if graph[i][j]:
                return keep
        else:
            keep = i

    return keep

def put_tile(t,x,y):
    if t==1:
        graph1_put_height = get_can_put_height(graph1,x,x)
        graph2_put_height = get_can_put_height(graph2,y,y)

        graph1[y-y+graph1_put_height][x] = 1

        graph2[x-x+graph2_put_height][y] = 1
    elif t==2:
        graph1_put_height = get_can_put_height(graph1,x,x)
        graph2_put_height = get_can_put_height(graph2,y,y+1)
        graph1[y-y+graph1_put_height][x] = 1
        graph1[y-y-1+graph1_put_height][x] = 1

        graph2[x-x+graph2_put_height][y] = 1
        graph2[x-x+graph2_put_height][y+1] = 1

    else:
        graph1_put_height = get_can_put_height(graph1,x,x+1)
        graph2_put_height = get_can_put_height(graph2,y,y)

        graph1[y-y+graph1_put_height][x] = 1
        graph1[y-y+graph1_put_height][x+1] = 1

        graph2[x-x+graph2_put_height][y] = 1
        graph2[x-x-1+graph2_put_height][y] = 1

def get_score(graph):
    score = 0
    i = 5
    while True:
        if i == -1:
            break
        for j in range(4):
            if graph[i][j] == 0:
                i -= 1
                break
        else: # 끝나도 같은 행 또 검사해야함!!!
            del graph[i]
            graph.insert(0,[0]*4)
            score += 1
    return score

def graph_clear(graph):
    cnt_clear = 0
    for i in range(2): # 최적화 가능한데 그냥 두개 다 보자
        for j in range(4):
            if graph[i][j]:
                cnt_clear += 1
                break

    for _ in range(cnt_clear):
       del graph[5]
       graph.insert(0,[0]*4)


graph1 = []
graph2 = []
for _ in range(6):
    graph1.append([0]*4)
    graph2.append([0]*4)

score = 0
N = int(sys.stdin.readline())
for n in range(N):
    t,x,y = map(int, sys.stdin.readline().split())
    put_tile(t,x,y)

    score += get_score(graph1)
    score += get_score(graph2)

    graph_clear(graph1)
    graph_clear(graph2)

cnt = 0
for i in range(6):
    for j in range(4):
        cnt += graph1[i][j]
        cnt += graph2[i][j]

print(score)
print(cnt)