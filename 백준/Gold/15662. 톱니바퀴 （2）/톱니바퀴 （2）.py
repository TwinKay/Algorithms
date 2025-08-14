import sys
from collections import deque

def get_right(deq_num):
    return deqs[deq_num][2]

def get_left(deq_num):
    return deqs[deq_num][6]

def get_connect_info():
    info = [False]*(N-1)
    for i in range(N-1):
        a = get_right(i)
        b = get_left(i+1)
        if a!=b:
            info[i] = True
    return info

def rotate_total(deq_num,direct):
    connect_info = get_connect_info()

    deqs[deq_num].rotate(direct)
    nav_direct = -direct
    for i in range(deq_num,N-1): # 오른쪽으로
        if not connect_info[i]:
            break
        deqs[i+1].rotate(nav_direct)
        nav_direct = -nav_direct

    nav_direct = -direct
    for i in range(deq_num-1,-1,-1): # 왼쪽으로
        if not connect_info[i]:
            break
        deqs[i].rotate(nav_direct)
        nav_direct  = -nav_direct



N = int(sys.stdin.readline())
deqs = []
for _ in range(N):
    deqs.append(deque(list(map(int,list(sys.stdin.readline().rstrip())))))

Q = int(sys.stdin.readline())
for q in range(Q):
    num,direct = map(int, sys.stdin.readline().split())
    rotate_total(num-1,direct)

cnt = 0
for deq in deqs:
    if deq[0] == 1:
        cnt += 1

print(cnt)