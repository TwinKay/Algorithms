import sys

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

delta_x = [0,-1,0,1]
delta_y = [1,0,-1,0]

N = int(sys.stdin.readline())
queries = list(sys.stdin.readline().rstrip())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

ari_x = 0; ari_y = 0; ari_direct = 0
zombie_idxs = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'O':
            continue
        elif graph[i][j] == 'Z':
            zombie_idxs.append([j,i,0])
            graph[i][j] = 'O'

shine = []
for _ in range(N):
    shine.append([False]*N) # 형광등 관리용

is_dead = False
for query in queries:
    if is_dead:
        break
    if query == 'L':
        ari_direct += 3
    elif query == 'R':
        ari_direct += 1
    else:
        dx = ari_x + delta_x[(ari_direct+4)%4]
        dy = ari_y + delta_y[(ari_direct+4)%4]

        if is_valid(dx,dy):
            if graph[dy][dx] == 'S':
                for a in range(-1,2):
                    for b in range(-1,2):
                        if is_valid(dx+b,dy+a):
                            shine[dy+a][dx+b] = True


            ari_x = dx
            ari_y = dy

    for zombie_idx in zombie_idxs:
        x, y, direct = zombie_idx
        if x==ari_x and y==ari_y and not shine[y][x]:
            is_dead = True
            break


    new_zombie_idxs = []
    for zombie_idx in zombie_idxs:
        if is_dead:
            break

        x,y,direct = zombie_idx
        dx = x + delta_x[direct%4]
        dy = y + delta_y[direct%4]
        if is_valid(dx,dy):
            new_zombie_idxs.append([dx,dy,direct])
        else:
            new_zombie_idxs.append([x,y,direct+2])

    for zombie_idx in new_zombie_idxs:
        x, y, direct = zombie_idx
        if x==ari_x and y==ari_y and not shine[y][x]:
            is_dead = True
            break
    zombie_idxs = new_zombie_idxs

if is_dead:
    print("Aaaaaah!")
else:
    print("Phew...")
