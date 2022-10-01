# L,R에서 문자열로 접근해서 시간초과..? -> 수식으로
# 시간초과2 -> result[n]도 저장해서 사용
# 시간초과3 -> result 없애고 하나로 추가
# 시간초과4 -> n으로 바로 계산
# 시간초과5
# 시간초과6 -> 채점 현황보니 애초에 python3로는 못 푸는 문제.......... -> pypy로

import sys
from collections import deque

def bfs(a,b):
    visited = [False] * 10001
    deq = deque([[a,'']])
    visited[a] = True

    while deq:
        n , route = deq.popleft()
        if n == b:
            return route
        else:
            #D
            n_d = n*2%10000
            if visited[n_d] == False:
                deq.append([n_d,route+'D'])
                visited[n_d] = True

            #S
            n_s = n-1
            if visited[n_s] == False:
                if n_s == -1:
                    n_s = 9999
                deq.append([n_s,route+'S'])
                visited[n_s] = True

            #L
            n_l = n%1000*10 + n//1000
            if visited[n_l] == False:
                deq.append([n_l,route+'L'])
                visited[n_l] = True

            #R
            n_r = n%10*1000 + n//10
            if visited[n_r] == False:
                deq.append([n_r,route+'R'])
                visited[n_r] = True


for i in range(int(sys.stdin.readline())):
    a,b = map(int, sys.stdin.readline().split())

    print(bfs(a,b))