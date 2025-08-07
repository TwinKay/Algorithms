'''
아이디어:
분할 정복 -> N//2하면서 분할하기
첫번째 color와 다른 순간에 분할
모두 같다면 같은 color에 cnt++
'''
import sys

def recu(start_x,start_y,n):
    global cnt_blue,cnt_white
    color = graph[start_y][start_x] # 기준 color 선정
    for i in range(n):
        for j in range(n):
            x = start_x + j
            y = start_y + i
            if graph[y][x] != color: # 기준 color와 다르면 재귀 호출 후 return
                recu(start_x,start_y,n//2)
                recu(start_x+n//2,start_y,n//2)
                recu(start_x,start_y+n//2,n//2)
                recu(start_x+n//2,start_y+n//2,n//2)
                return
    if color:
        cnt_blue += 1
    else:
        cnt_white += 1
        
N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

cnt_blue = cnt_white = 0
recu(0,0,N)
print(cnt_white)
print(cnt_blue)