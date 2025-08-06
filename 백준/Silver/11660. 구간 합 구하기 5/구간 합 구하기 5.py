'''
아이디어: 누적합 2차원 배열 이용
풀이시간: 40분
시도횟수: 1회
실행시간: 
메모리:
'''
import sys

N,M = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

pre_sum = [] # 누적합 배열
pre_sum.append([0]*(N+1))
for _ in range(1,N+1):
    pre_sum.append([0])

for i in range(1,N+1):
    for j in range(1,N+1):
        sm = arr[i-1][j-1] + pre_sum[i-1][j] + pre_sum[i][j-1] - pre_sum[i-1][j-1]
        pre_sum[i].append(sm)

for _ in range(M):
    y1,x1,y2,x2 = map(int, sys.stdin.readline().split())
    ans = pre_sum[y2][x2] - pre_sum[y1-1][x2] - pre_sum[y2][x1-1] + pre_sum[y1-1][x1-1]
    print(ans)