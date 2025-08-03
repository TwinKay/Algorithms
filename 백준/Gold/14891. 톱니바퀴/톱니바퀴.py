'''
아이디어:
deque를 통한 회전
'''

import sys
from collections import deque

def check_left(deq):
    return deq[6]

def check_right(deq):
    return deq[2]

def find_connected():
    connected_arr = [False,False,False]
    deq1_right = check_right(deq1)
    deq2_left = check_left(deq2)
    deq2_right = check_right(deq2)
    deq3_left = check_left(deq3)
    deq3_right = check_right(deq3)
    deq4_left = check_left(deq4)
    if deq1_right != deq2_left:
        connected_arr[0] = True
    if deq2_right != deq3_left:
        connected_arr[1] = True
    if deq3_right != deq4_left:
        connected_arr[2] = True
    return connected_arr

def rotate_deq(deq,direct):
    if direct:
        temp = deq.pop()
        deq.appendleft(temp)
    else:
        temp = deq.popleft()
        deq.append(temp)

def rotate_total(deq_num,direct):
    connected_arr = find_connected()
    if deq_num == 1:
        rotate_deq(deq1,direct)
        if connected_arr[0]:
            rotate_deq(deq2,not direct)
        else:
            return
        if connected_arr[1]:
            rotate_deq(deq3, direct)
        else:
            return
        if connected_arr[2]:
            rotate_deq(deq4,not direct)
        else:
            return

    elif deq_num == 2:
        rotate_deq(deq2,direct)
        if connected_arr[0]:
            rotate_deq(deq1,not direct)
        if connected_arr[1]:
            rotate_deq(deq3,not direct)
        else:
            return
        if connected_arr[2]:
            rotate_deq(deq4, direct)
        else:
            return

    elif deq_num == 3:
        rotate_deq(deq3,direct)
        if connected_arr[2]:
            rotate_deq(deq4,not direct)
        if connected_arr[1]:
            rotate_deq(deq2,not direct)
        else:
            return
        if connected_arr[0]:
            rotate_deq(deq1,direct)
        else:
            return
        
    elif deq_num == 4:
        rotate_deq(deq4,direct)
        if connected_arr[2]:
            rotate_deq(deq3,not direct)
        else:
            return
        if connected_arr[1]:
            rotate_deq(deq2, direct)
        else:
            return
        if connected_arr[0]:
            rotate_deq(deq1,not direct)

# 0번: 12시  2번: 3시  6번: 9시
deq1 = deque(list(map(int, list(sys.stdin.readline().rstrip()))))
deq2 = deque(list(map(int, list(sys.stdin.readline().rstrip()))))
deq3 = deque(list(map(int, list(sys.stdin.readline().rstrip()))))
deq4 = deque(list(map(int, list(sys.stdin.readline().rstrip()))))

query_num = int(sys.stdin.readline())
for _ in range(query_num):
    deq_num, direct = map(int, sys.stdin.readline().split())
    if direct == 1:
        direct = True
    else:
        direct = False

    rotate_total(deq_num,direct)

res = 0
if deq1[0] == 1:
    res += 1
if deq2[0] == 1:
    res += 2
if deq3[0] == 1:
    res += 4
if deq4[0] == 1:
    res += 8
print(res)

