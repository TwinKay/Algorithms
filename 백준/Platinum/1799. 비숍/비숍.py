'''
아이디어:
1. 비숍을 무조건 넣어야하는 곳에 미리 넣어서 최적화
    -> 최악의 경우(모두 1인 그래프)에서는 오히려 속도 저하 가능성..?
2. 대각선을 row,col로 변경해서 row 단위로 전개하며 col만 보도록 최적화
'''
import sys


def is_valid(x,y):
    '''
    가능한 범위인지 확인하는 함수
    :param x: (int) x좌표
    :param y: (int) y좌표
    :return: (boolean) True: 가능한 범위
    '''
    return 0<=x<N and 0<=y<N


def is_can(x,y):
    '''
    비숍을 무조건 넣을 수 있는 곳인지 확인하는 함수
    :param x: (int) x좌표
    :param y: (int) y좌표
    :return: (boolean) True: 초기에 넣고 시작할 수 있으면
    '''
    for k in range(4):
        dx = x + delta_x[k]
        dy = y + delta_y[k]
        while True:
            if not is_valid(dx,dy):
                break
            if graph[dy][dx] == 1: # 다른 비숍과 충돌
                return False
            dx += delta_x[k]
            dy += delta_y[k]
    return True


def dfs(row,cnt):
    '''
    새로운 그래프 기준으로 백트래킹하여 놓을 수 있는 최대 비숍을 구하는 함수
    :param (int) row: 기준 행
    :param (int) cnt: 현재 놓을 수 있는 비숍 수
    :return: (None) -> global max_bishop으로 갱신
    '''
    global max_bishop
    if cnt + (new_N-row) <= max_bishop: # 남은 row에 모두 비숍을 넣더라고 max_bishop 갱신 불가한 경우
        return

    if row == new_N: # 기저
        max_bishop = max(max_bishop,cnt)
        return

    for col in range(new_N):
        if new_graph[row][col] and not visited[col]:
            visited[col] = True
            dfs(row+1, cnt+1)
            visited[col] = False

    dfs(row+1, cnt) # 비숍 안 놓는 경우


delta_x = [1,-1,-1,1]
delta_y = [1,-1,1,-1]

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

already_bishop = 0 # 무조건 들어가는 비숍
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and is_can(j, i):
            already_bishop += 1
            graph[i][j] = 0

new_N = 2*N-1 # 새로운 그래프 기준 N
new_graph = []
for _ in range(new_N):
    new_graph.append([0]*new_N)

# 새로운 그래프 만들기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            new_i = i+j
            new_j = (N-1-i)+j
            new_graph[new_i][new_j] = 1

visited = [False]*new_N
max_bishop = 0
dfs(0, 0)

print(already_bishop + max_bishop)