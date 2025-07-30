'''
실행시간:
메모리:
풀이시간: 19:30~
아이디어: boolean 배열으로 겹치기
'''
import sys

graph = []
for _ in range(100):
    graph.append([False]*100)

N = int(sys.stdin.readline())
for _ in range(N):
    a,b = map(int, sys.stdin.readline().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            graph[i][j] = True
cnt = 0
for i in range(100):
    for j in range(100):
        if graph[i][j]:
            cnt += 1
print(cnt)