'''
아이디어: 단순 시뮬
주의 사항:
1. 후진이라도 방문하지 않았던 곳이 있을 수 있음 -> 후진도 visited 체크!
2. 후진은 direction이 변경되지 않는다.
3. 후진 또한 한 칸씩이다.
4. 4방향을 한 번 씩만 본 것을 체크하기 위해서는 for문 혹은 처음 direction을 기억하고 비교해야한다 -> for문으로 처리
'''
import sys

delta_x = [0,1,0,-1]
delta_y = [-1,0,1,0]

N,M = map(int, sys.stdin.readline().split())
y,x,direct = map(int, sys.stdin.readline().split())

graph = []
visited = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
    visited.append([False]*M)

visited[y][x] = True
while True:
    is_can_go = False # 후진 여부를 판단하기 위한 boolean 변수
    for _ in range(4): # 4방
        direct -= 1 # 좌회전 (+3 즉 (direct-1)+4을 하지 않은 이유는 파이썬에서 -1 % 4 = 3이기 때문

        dx = x + delta_x[direct%4]
        dy = y + delta_y[direct%4]
        if graph[dy][dx] == 0 and not visited[dy][dx]: # 방, 방문 X
            visited[dy][dx] = True
            x,y = dx,dy
            is_can_go = True
            break

    if not is_can_go: # 4방 모두 불가능 -> 후진
        dx = x + delta_x[(direct+2)%4] # direct += 2 으로 값을 변경하지 않는 것이 중요!
        dy = y + delta_y[(direct+2)%4]
        if graph[dy][dx] == 0: # 후진은 갈 수 있으면
            visited[dy][dx] = True # 필요함(후진으로 방문했어도 이전에 방문한 곳이 아닐 수도 있음)
            x,y = dx,dy
        else: # 4방 전진에 후진도 불가능하면 종료
            break

# 방문한 칸 세기
cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            cnt += 1

print(cnt)