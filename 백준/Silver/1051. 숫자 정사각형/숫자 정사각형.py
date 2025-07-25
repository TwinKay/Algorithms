'''
유형: 구현
주의사항:
    큰 정사각형에서 작은 정사각형으로 구현
    없는 경우 조건이 없다..?
'''
import sys

N,M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,list(sys.stdin.readline().rstrip()))))

length = min(N,M)
flag = False
while length>0:
    if flag:
        break
    for i in range(N-length+1):
        if flag:
            break
        for j in range(M-length+1):
            if graph[i][j]==graph[i+length-1][j+length-1]==graph[i][j+length-1]==graph[i+length-1][j]:
                print(length*length)
                flag = True
                break
    length -= 1
