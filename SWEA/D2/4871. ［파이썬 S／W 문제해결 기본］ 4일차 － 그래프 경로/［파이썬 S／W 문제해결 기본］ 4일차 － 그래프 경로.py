'''
아이디어:
recu으로 dfs
'''
 
def dfs(c):
    global is_find
    visited[c] = True
    if G == c:
        is_find = True
        return
    for n in graph[c]:
        if not visited[n]:
            dfs(n)
 
T = int(input())
for t in range(1,T+1):
    graph = []
    V,E = map(int, input().split())
    for _ in range(V+1):
        graph.append([])
    for _ in range(E):
        node_a,node_b = map(int, input().split())
        graph[node_a].append(node_b)
 
    S,G = map(int, input().split()) # start target
 
    visited = [False]*(V+1)
 
    is_find = False
    dfs(S)
 
    if is_find:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')