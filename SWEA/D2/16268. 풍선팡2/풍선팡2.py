'''
유형: 구현
주의사항:
    index 초과
    절대값 구하기
'''

prt = []

def isValid(x,y):
    return 0<=x<M and 0<=y<N

delta_X = [0,0,-1,1,0]
delta_Y = [1,-1,0,0,0]

T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    max_val = 0
    for i in range(N):
        for j in range(M):
            garu = 0
            for k in range(5):
                dx = j+delta_X[k]
                dy = i+delta_Y[k]
                if isValid(dx,dy):
                    garu += graph[dy][dx]
            max_val = max(max_val,garu)
    prt.append(f"#{t} {max_val}")
print("\n".join(prt))

