import sys

def eat_ground():
    for i in range(N):
        for j in range(N):
            if tree_graph[i][j]:
                alive_lst = []
                death_lst = []
                ground_val = ground_graph[i][j]

                tree_graph[i][j].sort()
                for tree_i in range(len(tree_graph[i][j])):
                    if tree_graph[i][j][tree_i] <= ground_val:
                        alive_lst.append(tree_graph[i][j][tree_i]+1)
                        ground_val -= tree_graph[i][j][tree_i]

                    else:
                        death_lst.extend(tree_graph[i][j][tree_i:])
                        break

                # for tree in tree_graph[i][j]: # 안되는 순간 바로 extend로 처리
                #     if tree <= ground_val:
                #         alive_lst.append(tree+1)
                #         ground_val -= tree
                #
                #     else:
                #         death_lst.append(tree) # 아래 바로 가능 -> 아니야 여름에 한번에 처리야

                tree_graph[i][j] = alive_lst
                for death_tree in death_lst:
                    ground_val += death_tree//2

                ground_graph[i][j] = ground_val

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def spread(): # 바로 같은 그래프에다 해도 된다. 근데 그러면 %5 비교 수가 늘어나지 않는가
    new_tree_list = [] # 새로운 나무 갯수 저장
    for i in range(N):
        new_tree_list.append([0]*N)

    for i in range(N):
        for j in range(N):
            for tree in tree_graph[i][j]:
                if tree%5 == 0:
                    for k in range(8):
                        dx = j + delta_x[k]
                        dy = i + delta_y[k]
                        if is_valid(dx,dy):
                            new_tree_list[dy][dx] += 1
    for i in range(N):
        for j in range(N):
            if new_tree_list[i][j]:
                for _ in range(new_tree_list[i][j]):
                    tree_graph[i][j].append(1)

def add_ground():
    for i in range(N):
        for j in range(N):
            ground_graph[i][j] += added_graph[i][j]


delta_x = [-1,0,1,-1,1,-1,0,1]
delta_y = [-1,-1,-1,0,0,1,1,1]

N,M,K = map(int, sys.stdin.readline().split())

ground_graph = [] # 2dim
for _ in range(N):
    ground_graph.append([5]*N)

added_graph = [] # 2 dim 매번 추가되는 양분양
for _ in range(N):
    added_graph.append(list(map(int, sys.stdin.readline().split())))

tree_graph = [] # 3dim
for i in range(N):
    tree_graph.append([])
    for _ in range(N):
        tree_graph[i].append([])

for _ in range(M):
    y,x,age = map(int, sys.stdin.readline().split())
    tree_graph[y-1][x-1].append(age)

for k in range(K):
    eat_ground() # 봄 여름
    spread() # 가을
    add_ground() # 겨울

res = 0
for i in range(N):
    for j in range(N):
        res += len(tree_graph[i][j])

print(res)