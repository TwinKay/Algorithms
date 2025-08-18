import sys

def is_posi():
    is_first = True
    cx,cy = -1,-1
    visited = []
    for _ in range(N):
        visited.append([False]*N)
    for query in queries:
        idx = change_idx(query)
        nx,ny = idx

        if is_first or is_can_go(cx,cy,nx,ny):
            if not visited[ny][nx]:
                is_first = False
                visited[ny][nx] = True
                cx,cy = nx,ny
                continue

        return False

    return True




def is_can_go(x1,y1,x2,y2):
    diff_x = abs(x1-x2)
    diff_y = abs(y1-y2)
    if diff_y==2 and diff_x==1:
        return True
    elif diff_y==1 and diff_x==2:
        return True
    return False


def change_idx(st):
    c1 = st[0]
    c2 = st[1]
    return [int(c2)-1, ord(c1)-ord("A")]

def is_ring():
    idx1 = change_idx(queries[0])
    idx2 = change_idx(queries[35])
    x1,y1 = idx1
    x2,y2 = idx2
    if is_can_go(x1,y1,x2,y2):
        return True
    return False

N = 6
queries = []
for _ in range(N*N):
    queries.append(sys.stdin.readline().rstrip())



if is_posi() and is_ring():
    print("Valid")
else:
    print("Invalid")

