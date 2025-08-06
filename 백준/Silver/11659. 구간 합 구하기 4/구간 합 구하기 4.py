'''
아이디어: 누적합 배열 이용
'''
import sys

N,M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
pre_sum_arr = [0] # 기본 0 넣기

sm = 0
for i in range(N):
    sm += arr[i]
    pre_sum_arr.append(sm)
    
for m in range(M):
    a,b = map(int, sys.stdin.readline().split())
    print(pre_sum_arr[b]-pre_sum_arr[a-1]) # a~b