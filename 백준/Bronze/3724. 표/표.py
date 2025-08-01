import sys

T = int(sys.stdin.readline())
for _ in range(T):
    M,N= map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))

    max_col = 1
    max_val = 1
    for i in range(N):
        max_val *= graph[i][0]

    for j in range(1,M):
        val = 1
        for i in range(N):
            val *= graph[i][j]
        if val >= max_val:
            max_val = val
            max_col = j+1
    print(max_col)
