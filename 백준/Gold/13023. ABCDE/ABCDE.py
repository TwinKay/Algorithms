'''
아이디어:
dfs로 depth가 5가 되는 순간이 있는지 판단하여 친구 관계 존재 유무 판단
'''
import sys

def dfs(c,depth):
    '''
    dfs를 수행하며 depth가 5가 되면 True를 반환하는 함수
    :param c: 시작하는 graph의 idx
    :return: (boolean) 기준 depth 이상 여부
    '''
    if depth == 5:
        return True
    for n in graph[c]:
        if not visited[n]:
            visited[n] = True
            if dfs(n,depth+1):
                return True
            visited[n] = False

    return False


N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append([])
visited = [False]*N
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향

is_find = False # 5depth 존재 여부
for i in range(N):
    visited[i] = True
    if dfs(i,1):
        is_find = True
        break
    visited[i] = False

if is_find:
    print(1)
else:
    print(0)