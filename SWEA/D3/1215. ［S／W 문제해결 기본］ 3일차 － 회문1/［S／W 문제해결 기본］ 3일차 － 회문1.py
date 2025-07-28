'''
한 글자도 회문
'''
res = []

def is_valid(x,y):
    return 0<=x<8 and 0<=y<8

def is_hoimun_row(x,y):
    for i in range(N):
        if not is_valid(x+N-1-i,y):
            return False
        if graph[y][x+i] != graph[y][x+N-1-i]:
            return False
    return True

def is_hoimun_col(x,y):
    for i in range(N):
        if not is_valid(x,y+N-1-i):
            return False
        if graph[y+i][x] != graph[y+N-1-i][x]:
            return False
    return True

T = 10
for t in range(1,T+1):
    N = int(input())
    graph = []
    for _ in range(8):
        graph.append(list(input().rstrip()))

    cnt = 0
    for i in range(8):
        for j in range(8):
            if is_hoimun_row(j,i):
                cnt += 1
            if is_hoimun_col(j,i):
                cnt += 1
    res.append(f'#{t} {cnt}')
print('\n'.join(res))
