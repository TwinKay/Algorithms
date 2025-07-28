'''
유형: 구현
주의사항:
    중심 꽃가루만큼 spread
    idx 초과 조심
'''

prt = []

delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

def isValid(x,y):
    return 0<=x<M and 0<=y<N

def countGaru(x,y):
    length = graph[y][x]
    garu = length
    for k in range(4):
        for leng in range(1,length+1): # 가루 갯수만큼 터뜨리기
            dx = x + delta_x[k]*leng
            dy = y + delta_y[k]*leng
            if isValid(dx,dy):
                garu += graph[dy][dx]
    return garu

T = int(input())
for t in range(1,T+1):
    N,M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    max_val = 0
    for i in range(N):
        for j in range(M):
            max_val = max(max_val, countGaru(j,i))

    prt.append(f"#{t} {max_val}")
print("\n".join(prt))