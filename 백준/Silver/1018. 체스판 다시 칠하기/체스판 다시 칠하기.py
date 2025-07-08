import sys

N,M = map(int, sys.stdin.readline().split())
graph = []
for i in range(N):
    s = sys.stdin.readline().rstrip()
    graph.append([])
    for j in range(M):
        graph[i].append(s[j])

chess1 = []
chess2 = []
res = 100
temp = True
for i in range(8):
    if temp:
        chess1.append(["W","B","W","B","W","B","W","B"])
        chess2.append(["B","W","B","W","B","W","B","W"])
        temp = False
    else:
        chess1.append(["B","W","B","W","B","W","B","W"])
        chess2.append(["W","B","W","B","W","B","W","B"])
        temp = True

for i in range(N-8+1):
    for j in range(M-8+1):
        cnt = 0
        for y in range(i,i+8):
            for x in range(j,j+8):
                if graph[y][x] != chess1[y-i][x-j]:
                    cnt += 1
        if cnt<res:
            res = cnt
            
        cnt = 0
        for y in range(i,i+8):
            for x in range(j,j+8):
                if graph[y][x] != chess2[y-i][x-j]:
                    cnt += 1
        if cnt<res:
            res = cnt
            
print(res)