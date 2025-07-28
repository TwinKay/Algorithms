res = []

T = int(input())
for t in range(1,T+1):
    N = int(input())
    graph = []

    for i in range(10):
        graph.append([])
        for j in range(10):
            graph[i].append([])
            graph[i][j] = [False,False]

    for _ in range(N):
        r1,c1,r2,c2,color = map(int,input().split()) # 1: 빨강 2: 파랑
        
        # 마지막 depth는 color 저장용
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                if color == 1:
                    graph[i][j][0] = True
                else:
                    graph[i][j][1] = True
    cnt = 0
    for i in range(10):
        for j in range(10):
            if graph[i][j][0] and graph[i][j][1]:
                cnt += 1

    res.append(f"#{t} {cnt}")
print("\n".join(res))
