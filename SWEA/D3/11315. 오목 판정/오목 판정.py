'''
유형: 구현, 브루트포스
주의사항:
    5이상도 YES
'''
def isValid(x,y):
    return 0<=x<N and 0<=y<N

def isOmok():
    for k in range(4): # 가로 세로 대각선 2개
        for i in range(N):
            for j in range(N):
                cnt_o = 0
                for l in range(5):
                    dx = j + delta_x[k]*l
                    dy = i + delta_y[k]*l
                    if isValid(dx,dy) and graph[dy][dx] == 'o':
                        cnt_o += 1
                if cnt_o == 5:
                    return True

    return False


prt = []

delta_x = [1,0,1,-1]
delta_y = [0,1,1,1]

T = int(input())
for t in range(1,T+1):
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(input().rstrip()))

    if isOmok():
        prt.append(f"#{t} YES")
    else:
        prt.append(f"#{t} NO")

print("\n".join(prt))
