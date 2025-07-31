'''
아이디어:
bfs를 통한 풀이
범위는 B까지만 확인
만들 수 없다면 -1
string 연산(1을 오른쪽 추가)보다는 *10+1로 효율
메모리 초과 조심 -> visited 배열 필요가 없네..?
'''

import sys
from collections import deque

A,B = map(int, sys.stdin.readline().split())

deq = deque()
deq.append([A,1]) # num, 연산 횟수
res = -1 # 답 없다면 그대로 -1
while deq:
    cur = deq.popleft()
    num = cur[0]
    cnt = cur[1]

    if num == B: # B 만나면
        res = cnt
        break

    n1 = num*2
    n2 = num*10 + 1 # 오른쪽 1추가
    if n1 <= B:
        deq.append([n1,cnt+1])
    if n2 <= B:
        deq.append([n2,cnt+1])

print(res)