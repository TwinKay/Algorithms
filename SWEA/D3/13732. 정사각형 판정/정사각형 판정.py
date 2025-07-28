T = int(input())
for t in range(1,T+1):
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(input().rstrip()))

    x1,y1,x2,y2 = -1,-1,-1,-1
    is_find = False
    for i in range(N):
        if is_find:
            break
        for j in range(N):
            if graph[i][j] == "#":
                x1,y1 = j,i
                is_find = True
                break

    is_find = False
    for i in range(N-1,-1,-1):
        if is_find:
            break
        for j in range(N-1,-1,-1):
            if graph[i][j] == "#":
                x2,y2 = j,i
                is_find = True
                break

    cnt_sharp = 0
    for i in range(y1,y2+1):
        for j in range(x1,x2+1):
            if graph[i][j] =='#':
                cnt_sharp += 1

    is_yes = True
    if y2-y1 != x2-x1:
        is_yes = False

    if cnt_sharp != (y2-y1+1)*(x2-x1+1):
        is_yes = False
    if is_yes:
        print(f"#{t} yes")
    else:
        print(f"#{t} no")
