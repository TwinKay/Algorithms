import sys
from itertools import permutations

def is_star():
    sm1 = graph[0][4]+graph[1][3]+graph[2][2]+graph[3][1]
    if sm1 != 26:
        return False
    sm2 = graph[3][1]+graph[3][3]+graph[3][5]+graph[3][7]
    if sm2 != 26:
        return False
    sm3 = graph[0][4]+graph[1][5]+graph[2][6]+graph[3][7]
    if sm3 != 26:
        return False
    sm4 = graph[1][1]+graph[1][3]+graph[1][5]+graph[1][7]
    if sm4 != 26:
        return False
    sm5 = graph[1][1]+graph[2][2]+graph[3][3]+graph[4][4]
    if sm5 != 26:
        return False
    sm6 = graph[1][7]+graph[2][6]+graph[3][5]+graph[4][4]
    if sm6 != 26:
        return False

    return True

N = 5
M = 9
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

exist_num = set()
cand_idxs = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'x':
            cand_idxs.append([j,i])
            graph[i][j] = 100
        elif graph[i][j] != '.':
            graph[i][j] = ord(graph[i][j])-ord('A')+1
            exist_num.add(graph[i][j])

cand_nums = set(range(1,13))
cand_nums -= exist_num
cand_nums = list(cand_nums)
is_find = False
for perm in permutations(cand_nums):
    if is_find:
        break
    for idx, num in zip(cand_idxs, perm):
        graph[idx[1]][idx[0]] = num
    if is_star():
        for i in range(N):
            for j in range(M):
                if graph[i][j] != '.':
                    graph[i][j] = chr(graph[i][j]+ord('A')-1)

        for g in graph:
            print("".join(g))
        is_find = True
        break
