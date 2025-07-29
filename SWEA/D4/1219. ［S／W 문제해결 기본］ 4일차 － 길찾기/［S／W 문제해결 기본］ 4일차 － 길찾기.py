'''
아이디어:
recu으로 dfs
'''
 
def dfs(c):
    global res
    visited[c] = True
    if c == target:
        res = 1
        return
    for n in graph[c]:
        if not visited[n]:
            dfs(n)
 
for _ in range(10):
    t,E = map(int, input().split())
    V = 100
    graph = []
    for _ in range(V):
        graph.append([])
    visited = [False]*V
    arr = list(map(int, input().split()))
    for i in range(0,len(arr),2):
        a = arr[i]
        b = arr[i+1]
        graph[a].append(b)
 
    start,target = 0,99
    res = 0
    dfs(start)
    print(f'#{t} {res}')