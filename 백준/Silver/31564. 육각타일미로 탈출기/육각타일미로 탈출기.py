import sys
from collections import deque


def switch_index(x,y):
    if y%2==0:
        return [x*2,y]
    else:
        return [x*2+1,y]

def is_valid(x,y):
    return 0<=x<2*M and 0<=y<N

delta_x = [-1,-1,1,1,-2,2]
delta_y = [-1,1,-1,1,0,0]

N,M,K = map(int, sys.stdin.readline().split())
visited = []
for _ in range(N):
    visited.append([False]*(M*2))


for _ in range(K):
    y,x = map(int, sys.stdin.readline().split())
    x,y = switch_index(x,y)
    visited[y][x] = True

end_x,end_y = switch_index(M-1,N-1)

res = -1
deq = deque()
deq.append([0,0,0])
visited[0][0] = True
while deq:
    x,y,time = deq.popleft()
    if end_x==x and end_y==y:
        res = time
        break
    for k in range(6):
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        if is_valid(dx,dy) and not visited[dy][dx]:
            deq.append([dx,dy,time+1])
            visited[dy][dx] = True

print(res)

