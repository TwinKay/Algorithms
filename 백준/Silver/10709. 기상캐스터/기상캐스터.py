'''
유형: 시뮬레이션
주의사항:
    index 초과
'''
import sys

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().strip()))

def distCloud(x,y):
    dist = 0
    while x>=0: # 왼쪽 끝까지
        if graph[y][x] == 'c':
            return dist
        x -= 1
        dist += 1
    return -1 # 왼쪽 끝까지 구름이 없다면

res = []
for i in range(N):
    res.append([])
    for j in range(M):
        res[i].append(distCloud(j,i))

for r in res:
    print(*r)