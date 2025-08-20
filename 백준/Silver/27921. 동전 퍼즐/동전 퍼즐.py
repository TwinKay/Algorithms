import sys

def is_valid(x,y):
    return 0<=x<50 and 0<=y<50

N1,M1 = map(int,sys.stdin.readline().split())
graph1 = []
for _ in range(N1):
    graph1.append(list(sys.stdin.readline()))

cnt1 = 0
for i in range(N1):
    for j in range(M1):
        if graph1[i][j] == 'O':
            cnt1 += 1
N2,M2 = map(int,sys.stdin.readline().split())
graph2 = []
for _ in range(N2):
    graph2.append(list(sys.stdin.readline()))
cnt2 = 0
for i in range(N2):
    for j in range(M2):
        if graph2[i][j] == 'O':
            cnt2 += 1
graph = []
for i in range(50):
    graph.append(['.']*50)

for i in range(N1):
    for j in range(M1): # 으아아아아아아아아아아아아아ㅏ아ㅏ아아아 이거 N2로 썼어!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        dx = j+20
        dy = i+20
        if graph1[i][j] == 'O':
            graph[dy][dx] = 'O'


max_dup = -1
for i in range(50):
    for j in range(50):
        donot = False
        dup = 0
        for a in range(N2):
            if donot:
                break
            for b in range(M2):
                if not is_valid(j+b,i+a):
                    donot = True
                    break

                if 'O' == graph[i+a][j+b] and 'O' == graph2[a][b]:
                    dup += 1
        else:
            max_dup = max(max_dup,dup)
print(cnt2-max_dup)