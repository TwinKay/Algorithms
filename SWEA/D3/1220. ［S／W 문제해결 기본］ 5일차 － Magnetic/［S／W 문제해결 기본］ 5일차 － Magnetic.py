'''
실행 시간: 
메모리:
시도 횟수: 1
풀이 시간: 39m 30s
'''

prt = []

graph = [[1,2],[3,4]]
def is_valid(x,y):
    return 0<=x<N and 0<=y<N

def up():
    for i in range(N):
        for j in range(N):
            dx,dy = j,i
            while True:
                if not is_valid(dx,dy-1):
                    break
                if graph[dy-1][dx] == 0:
                    graph[dy][dx],graph[dy-1][dx] = graph[dy-1][dx],graph[dy][dx]
                else:
                    break
                dy -= 1
            if dy==0 and graph[dy][dx] == 2:
                graph[dy][dx] = 0

def down():
    for i in range(N-1,-1,-1):
        for j in range(N):
            dx,dy = j,i
            while True:
                if not is_valid(dx,dy+1):
                    break
                if graph[dy+1][dx] == 0:
                    graph[dy][dx],graph[dy+1][dx] = graph[dy+1][dx],graph[dy][dx]
                else:
                    break
                dy += 1
            if dy==N-1 and graph[dy][dx] == 1:
                graph[dy][dx] = 0

T = 10
for t in range(1,T+1):
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    up()
    down()

    cnt = 0
    for j in range(N):

        is_visited_1 = False
        for i in range(N):
            if graph[i][j] == 1:
                is_visited_1 = True
            elif graph[i][j] == 2:
                if is_visited_1:
                    cnt += 1
                is_visited_1 = False
    prt.append(f'#{t} {cnt}')
print("\n".join(prt))
