'''
실행시간:
메모리:
풀이시간: 19:39~19:59
아이디어:
1차 - x,y의 min,max로 하다가 실제로 세어보니 내부 둘레도 포함..
2차 - 전체 돌면서 흰색일때 검은색 세기
'''
import sys

def is_valid(x,y):
    return 0<=x<N and 0<=y<N

N = 102
graph = []
for _ in range(N):
    graph.append([False]*N)

num_paper = int(sys.stdin.readline())
for _ in range(num_paper):
    a,b = map(int, sys.stdin.readline().split())
    a += 1
    b += 1
    for i in range(a,a+10):
        for j in range(b,b+10):
            graph[i][j] = True


delta_x = [0,0,-1,1]
delta_y = [1,-1,0,0]

cnt = 0
for i in range(N):
    for j in range(N):
        if not graph[i][j]:
            for k in range(4):
                dx = j+delta_x[k]
                dy = i+delta_y[k]
                if is_valid(dx,dy) and graph[dy][dx]:
                    cnt += 1
print(cnt)