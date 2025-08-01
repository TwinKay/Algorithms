import sys

L,N,T = map(int,sys.stdin.readline().split())
L += 1
graph = []
for _ in range(L):
    graph.append([])

for _ in range(N):
    idx, direct = sys.stdin.readline().split()
    idx = int(idx)
    graph[idx].append(direct)

cnt = 0
for t in range(T):
    new_graph = []
    for _ in range(L):
        new_graph.append([])
    for i in range(L):
        if not graph[i]:
            continue

        for d in graph[i]:
            if d =='R':
                new_graph[i+1].append('R')
            else:
                new_graph[i-1].append('L')


    for i in range(len(new_graph[0])):
        new_graph[0][i] = 'R'

    for i in range(len(new_graph[L-1])):
        new_graph[L-1][i] = 'L'

    for g in new_graph:
        if len(g)>=2:
            cnt += 1
    graph = new_graph
print(cnt)
